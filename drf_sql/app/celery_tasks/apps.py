# -*- coding: utf-8 -*-
# from django.apps import AppConfig
import pymysql


class MysqlCon():
    """
    应用于MySQL连接；
    """
    def __init__(self, db_host, db_port, db_name='mysql' ): # 内置函数 初始化操作
        self.db_name = db_name
        self.MysqlConf = {
            'host': db_host,
            'user': 'inception',
            'passwd': 'ulpNC79IYdk17ZVNhk',
            'port': int(db_port),
            'db': self.db_name,
            'charset': 'utf8',
            'local_infile': 1,
            'unix_socket': '',
            'cursorclass': pymysql.cursors.DictCursor
        }

    def SqlCheck(self):  # 数据库check 操作；
        try:
            self.conn = pymysql.connect(**self.MysqlConf)
            self.cur = self.conn.cursor()
            sql = 'show databases;'
            self.cur.execute(sql)
            res = self.cur.fetchall()
            return res
        except pymysql.Error as e:
            return e

    def SqlInput(self,sql):  # 输入操作；
        try:
            self.conn = pymysql.connect(**self.MysqlConf)
            self.cur = self.conn.cursor()
            self.cur.execute(sql)
            res = self.cur.fetchall()
            return res
        except pymysql.Error as e:
            return e

    def __del__(self): # 内置函数 断开连接操作
        try:
            self.cur.close()
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            return None

if __name__=="__main__":
      blacklist = ['information_schema', 'mysql', 'inception']
      res= MysqlCon('ebook_rds.meipian9.cn',3306).SqlCheck()
      try:
          for i in res:
              if i['Database'] in blacklist:
                  print (i['Database'])
      except:
          print (res)

