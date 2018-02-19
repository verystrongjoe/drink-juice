import logging
import os
import sys
import config
from multiprocessing import Process, Pool
import core.crawl.yahoo as cralwer
yahoo = cralwer.CrawlYahooTkr()

def crawl(tkr='') :



    '''
    ddd
    Crawling function using yahoo finance api
    https://finance.yahoo.com/quote/IBM/
    It runs parallely to maximize usage of every cpu core
    '''
    logging.debug('crawl with tickerlist')
    # print('crawl with tickerlist')

    if tkr == '' :
        rootdir = os.path.dirname(os.path.abspath(__file__))
        fname = config.APP_CONFIG['HOME'] + config.CRAWL_CONFIG['ticker_list_file']

        content = []

        # logging.debug('tkr : ' , tkr)

        rootdir = os.path.dirname(os.path.abspath(__file__))
        fname = config.APP_CONFIG['HOME'] + config.CRAWL_CONFIG['ticker_list_file']

        content = []
        p = Pool(10)


        with open(fname) as f:
            content = [x.strip() for x in f.readlines()]

        p.map(yahoo.download_csv, content)


    else :
        yahoo.download_csv(tkr)

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Started stock prediction application...')

    home = os.environ.get('HOME', None);

    if(home is None) :
        config.APP_CONFIG['HOME'] = os.path.dirname(sys.modules['__main__'].__file__)
    else :
        config.APP_CONFIG['HOME'] = os.environ['HOME']

    logging.debug('root project path : %s', config.APP_CONFIG['HOME'])

    mode = os.environ.get('mode', None)

    if not mode:
       raise ValueError('You must have "mode" variable')

    logging.debug('mode : %s', mode)
    if mode == 'init-environment' :
        logging.debug('initialize environment ')

        import core.persist.pg as pg

        # setup db connection
        db = pg.PostgreDB()

        # drop & create table
        db.script_execution(config.APP_CONFIG['HOME']+config.DATABASE_CONFIG['init-script'])

    elif mode == 'crawl' :
        print('crawl')
        ticker = os.environ.get('ticker', None)
        if ticker is None :
            crawl()
        else:
            #crawl('BAC')
            #crawl('DIA')
            crawl(ticker)

    elif mode == 'import-to-db' :
        # csv to database
        # 위에서 수집한 csv 파일을 postgre database로 옮기는 함수
        #csv_to_db('D:\\dev\\workspace\\stock-analysis\\data\\tkrcsv')
        import core.transport.csv2db as csv2db
        csv2db.copy2db(config.APP_CONFIG['HOME']+config.CRAWL_CONFIG['ticker_output_csv_path'])

    elif mode == 'generate-features' :
        # generate features
        import core.genf as genf
        genf.genf()

    elif mode == 'learn-and-predict' :
        # learn, predict
        import core.analyze.kerastkr as kerastkr
        out_df = kerastkr.learn_predict_kerasnn('^GSPC', 6, '2017-08')
        print(out_df)

        # out_df = kerastkr.load_predict_keraslinear()
        # print(out_df)

    else :
        raise ValueError('mode is not correct')
