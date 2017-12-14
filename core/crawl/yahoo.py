import datetime
import os
import re
import requests
import sys
import time
# import shutil

import time
from datetime import date
import config
import core.util.time as util
import logging

class CrawlYahooTkr :

    user_agent_s = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    qurl_s = 'https://query1.finance.yahoo.com/v7/finance/download/'
    csv_type_l = ['div','history','split']

    startdate = config.CRAWL_CONFIG['start_date']
    enddate = config.CRAWL_CONFIG['end_date'] # ''1262332800'    # '1420099200' # 150101  #-631123200

    p1p2_s = '?period1='+str(util.get_unix_time(startdate))+'&period2='
    ie_s = '&interval=1d&events='
    outdirc = ''
    outdirh = ''
    tkr  = ''


    def __init__(self, ticker= ''):

        logging.info('************----- %s', config.APP_CONFIG['HOME'] + config.CRAWL_CONFIG['ticker_output_csv_path'])

        self.outdirc = config.APP_CONFIG['HOME'] + config.CRAWL_CONFIG['ticker_output_csv_path']
        self.outdirh = config.APP_CONFIG['HOME'] + config.CRAWL_CONFIG['ticker_output_html_path']

        if ticker is None or ticker == '' :
            tkr = ''
        else :
            tkr = config.CRAWL_CONFIG['TKR']

        if not os.path.exists(self.outdirc) :
            os.makedirs(self.outdirc)

        if not os.path.exists(self.outdirh) :
            os.makedirs(self.outdirh)

        self.startdate = config.CRAWL_CONFIG['start_date']
        self.enddate = config.CRAWL_CONFIG['end_date'] # ''1262332800'    # '1420099200' # 150101  #-631123200


    def download_csv(self, tkr):

        logging.debug('Starting crawling with ticker, ' , tkr)

        url1_s = 'https://finance.yahoo.com/quote/' + tkr
        url2_s = url1_s + '/history?p=' + tkr
        headers_d = {'User-Agent': self.user_agent_s}

        with requests.Session() as ssn:

            if config.APP_CONFIG['HTTP_PROXY'] is not None :
                ssn.proxies["http"] = config.APP_CONFIG['HTTP_PROXY']
            if config.APP_CONFIG['HTTPS_PROXY'] is not None :
                ssn.proxies["https"] =  config.APP_CONFIG['HTTPS_PROXY']

            tkr1_r = ssn.get(url1_s, headers=headers_d,)
            time.sleep(4)

            tkr2_r = ssn.get(url2_s, headers=headers_d)
            html_s = tkr2_r.content.decode("utf-8")

            with open(self.outdirh+ '\\' +tkr+'.html','w', encoding='utf-8') as fh:
                fh.write(html_s)

            pattern_re = r'(CrumbStore":{"crumb":")(.+?")'
            pattern_ma = re.search(pattern_re, html_s) # The crumb I want is in pattern_ma[2].
            crumb_s    = pattern_ma.group(2).replace(r'"', '')

            for type_s in self.csv_type_l:
                # d = datetime.datetime.now()
                # nowutime_s = int(time.mktime(d.timetuple()))
                nowutime_s = util.get_unix_time(self.enddate)

                csvurl_s   = self.qurl_s+tkr+self.p1p2_s+str(nowutime_s)+self.ie_s+type_s+'&crumb='+crumb_s

                # Server needs time to remember the cookie-crumb-pair it just served:
                time.sleep(4)
                csv_r  = ssn.get(csvurl_s, headers=headers_d)
                csv_s  = csv_r.content.decode("utf-8")
                csvf_s = self.outdirc+'\\'+type_s+'\\'+tkr+'.csv'
                if (csv_r.status_code == 200):

                    if not os.path.exists(self.outdirc+ '\\' + type_s+'\\'):
                        os.makedirs(self.outdirc+'\\' + type_s+'\\')
                    try :
                        os.remove(csvf_s)
                    except :
                        #print(csvf_s + ' is not exist')
                        pass

                    # I should write the csv_s to csv file:
                    with open(csvf_s,'x') as fh:
                        fh.write(csv_s)
                        print('Wrote:', csvf_s)

                else:

                    print('GET request of ',tkr, ' failed. So I am trying again...')
                    with requests.Session() as ssn2:

                        if config.APP_CONFIG['HTTP_PROXY'] is not None:
                            ssn2.proxies = {"http": config.APP_CONFIG['HTTP_PROXY']}
                        if config.APP_CONFIG['HTTPS_PROXY'] is not None:
                            ssn2.proxies = {"https": config.APP_CONFIG['HTTPS_PROXY']}


                        tkr1_r = ssn2.get(url1_s, headers=headers_d)
                        time.sleep(6) # slower this time
                        tkr2_r     = ssn2.get(url2_s, headers=headers_d)
                        html2_s    = tkr2_r.content.decode("utf-8")
                        pattern_ma = re.search(pattern_re, html2_s)
                        crumb_s    = pattern_ma.group(2).replace(r'"', '')
                        csvurl_s   = self.qurl_s+tkr+self.p1p2_s+str(nowutime_s)+self.ie_s+type_s+'&crumb='+crumb_s
                        time.sleep(6)
                        csv2_r = ssn2.get(csvurl_s, headers=headers_d)
                        csv2_s = csv_r.content.decode("utf-8")
                        if (csv2_r.status_code == 200):
                            with open(csvf_s,'w') as fh:
                                fh.write(csv2_s)
                                print('Wrote:', csvf_s)
                        else:
                            print('GET request of ',tkr, ' failed. Maybe try later.')
        'bye'