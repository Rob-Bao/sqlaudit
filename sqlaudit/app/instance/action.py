#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: class_inception.py 
@time: 2019/2/28 3:05 PM 
"""
import pymysql
import configparser
import re,os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
configfile =  os.path.join(PROJECT_ROOT, 'env.txt'),
# configfile = "/Users/baochengcai/Code/project/mp/SqlAudit/app/env.txt"


class MyConfig(configparser.ConfigParser):
    """
    将配置文件生成字典
    """
    def to_dict(self):
        conf = dict(self._sections)
        for k in conf:
            conf[k] = dict(conf[k])
        return conf


class InceptionClass():
    """
    inception使用
    """
    def __init__(self):
        """
        初始化函数,获取配置文件内容
        """
        config = configparser.ConfigParser()
        config.read(configfile, encoding='utf8')
        self.inception_password = config.get('inception','inception_password')
        self.inception_port = config['inception']['inception_port']
        self.inception_user = config['inception']['inception_user']
        self.inception_host = config['inception']['inception_host']
        self.sql_user = config['inception']['sql_user']
        self.sql_password = config['inception']['sql_password']

    # def excludeKeyword(self, execute,sql):
    #     exclude_keyword = ['status']
    #     if execute == 0:
    #         for keyword in exclude_keyword:


    def CheckSql(self,**kwargs ):
        """
        :param instance_host: 被执行SQL的实例地址
        :param instance_port: 被执行SQL的实例端口
        :param dbname: 被执行SQL的数据库名字
        :param sql: 被执行的SQL内容
        :return: 返回inception检查的结果
        """
        result = []
        try:
            sql = """ /*--user=%s;--password=%s;--host=%s;--enable-check=1;--enable-execute=%s;--port=%s;*/\
                      inception_magic_start;\
                      use %s;\
                      %s\
                      inception_magic_commit; """\
                  %(self.sql_user,self.sql_password,kwargs['instance_host'],kwargs['execute'],int(kwargs['instance_port']),kwargs['dbname'],kwargs['sql'])
            SQL = re.sub("`","",sql)
            # SQL = SQL.encode('latin-1')
            conn = pymysql.connect(host = self.inception_host,
                                   user = self.inception_user,
                                   passwd = self.inception_password,
                                   db = '', port = int(self.inception_port),
                                   use_unicode=True,
                                   charset='utf8'
                                   )
            cur = conn.cursor()
            cur.execute(SQL)
            res = cur.fetchall()
            field_names = [i[0] for i in cur.description]
            for row in res:
                res = {}
                for i in range(11):
                    res[field_names[i]] = row[i]
                result.append(res)
            cur.close()
            conn.close()
        except pymysql.Error as e:
            Error = {}
            Error['ID'] = 1
            Error['errlevel'] = 1
            Error['SQL'] = kwargs['sql']
            Error['errormessage'] = 'Mysql Error %d' % e.args[0],e.args[1]
            result.append(Error)
        return result


# if __name__ == "__main__":
    # env = MyConfig()
    # env.read('../env', encoding="utf8")
    # env_inception = env.to_dict()['inception']
    # a = InceptionClass()
    # print(a.CheckSql('rm-2ze76g4a66f5h4645747.mysql.rds.aliyuncs.com','3306','zabbix','',0))
