import MySQLdb
from utils.pathBase import DBCONFIG
from utils.pathBase import readYamlFile

mysqlConfig =readYamlFile(DBCONFIG).get('mysql')

class mysqlConn:
    def __init__(self):
        self._conn = self.mysqlConn()
        self._cursor = self._conn.cursor()

    def __enter__(self):
        self.mysqlConn()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
            self.close()

    def mysqlConn(self):
        print('mysqlConfig :',mysqlConfig)
        conn = MySQLdb.connect(**mysqlConfig)
        return conn

    def select(self, sqlCode):
        with mysqlConn() as db:
            self._cursor.execute(sqlCode)
            return self._cursor.fetchall()

    def select_one(self, sqlCode):
        self._cursor.execute(sqlCode)
        return self._cursor.fetchone()

    def update(self, sqlCode):
        # sql = MySQLdb.escape_string(sqlCode)
        self.common(sqlCode)

    def common(self, sql):
        try:
            self._cursor.execute(sql)
        except Exception as e:
            self._conn.rollback()
            self._cursor.execute(sql)
        self._conn.commit()

    def close(self):
        self._cursor.close()
        self._conn.close()

if __name__ == '__main__':
    mysqlConn()