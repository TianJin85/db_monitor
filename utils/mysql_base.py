# encoding:utf-8
import pymysql

class MysqlBase(object):
    def __init__(self,params):
        self.params = params
        self.host = self.params['host']
        self.user = self.params['user']
        self.port = self.params['port']
        self.password = self.params['password']
        self.db = self.params.get('db','mysql')
        self.conn_conf = {
            'connect_timeout': 5,
            'use_unicode': True,
            'charset': 'utf8'
        }

    def connection(self):
        self.params.update(self.conn_conf)
        try:
            conn = pymysql.connect(host=self.host,port=int(self.port),user=self.user,password=self.password,db=self.db)
            return conn
        except Exception as e:
            print('mysql connect error:{}'.format(e))

    def query(self,sql,conn=None):
        if not conn:
            conn = self.connection()
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    def exec(self,sql,val):
        conn = self.connection()
        cur = conn.cursor()
        print('sql:' + sql)
        if val:
            cur.execute(sql, val)
        else:
            cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()

