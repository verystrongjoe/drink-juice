# config.py
APP_CONFIG = {
    'HOME' : 'D:\\dev\\workspace\\juice-project',
    'HTTP_PROXY' : 'http://70.10.15.10:8080',
    'HTTPS_PROXY' : 'http://70.10.15.10:8080'
}

DATABASE_CONFIG = {
    'host': '127.0.0.1',
    'name': 'tkrapi',
    'user': 'tkrapi',
    'password': 'tkrapi',
    'init-script' : '\\init\\db\\create-table.sql'
}

CRAWL_CONFIG = {
    'ticker_list_file' : '\\data\\input\\tkrlist.txt',
    'ticker_output_csv_path'  : '\\data\\raw\\tkrcsv',
    'ticker_output_html_path'  : '\\data\\raw\\tkrhtml',
    'start_date' : '20100101',
    'end_date' : '20171028',
    'ticker' : '',
}