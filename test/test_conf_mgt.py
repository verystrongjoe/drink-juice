import pymysql
import config
import datetime

#from datetime import date

def connect_db(dbname):
    if dbname != config.DATABASE_CONFIG['dbname']:
        raise ValueError("Could not find DB with given name")
    conn = pymysql.connect(host=config.DATABASE_CONFIG['host'],
                           user=config.DATABASE_CONFIG['user'],
                           password=config.DATABASE_CONFIG['password'],
                           db=config.DATABASE_CONFIG['dbname'])
    return conn


#print(config.DATABASE_CONFIG['host'])
#print(config.CRAWL_CONFIG['test'])

# connect_db('company')

print(datetime.datetime.now())