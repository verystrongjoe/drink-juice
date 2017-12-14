import os
from sqlalchemy import create_engine
import config
import logging

class PostgreDB :

    _db_url = 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
    _db_connection = None

    def __init__(self):
        # 'postgres://tkrapi:tkrapi@127.0.0.1/tkrapi'
        db_host = config.DATABASE_CONFIG['host']
        db_user = config.DATABASE_CONFIG['user']
        db_pwd = config.DATABASE_CONFIG['password']
        db_name = config.DATABASE_CONFIG['name']
        db_url = 'postgres://' + db_user + ":" + db_pwd + "@" + db_host +"/" + db_name

        self._db_url = db_url
        self._db_connection = create_engine(self._db_url).connect()

    # @staticmethod
    def get_conn(self) :
        return self._db_connection

    def query(self, sql, param=[]):
        result = self.get_conn().execute(sql, param)
        # idx = 0
        # for row in result:
        #     logging.debug('[%i] : %s', idx, row)
        # return result
        return result

    def __del__(self):
        self._db_connection.close()

    def script_execution(self, file_name):
        with open(file_name, 'r') as f :
            sql_script = f.read()
            self.get_conn().execute(sql_script)
        f.closed

# db = PostgreDB()
# db.script_execution('D:\dev\workspace\juice-project\init\db\create-table.sql')
# fileName = config.APP_CONFIG['HOME']+config.DATABASE_CONFIG['init-script'];
# print(fileName)
# db.script_execution(config.APP_CONFIG['HOME']+config.DATABASE_CONFIG['init-script'])