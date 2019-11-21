#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: CollectTable.py 
@time: 2019/4/8 10:35 AM 
"""
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "mp_sqlcheck.settings"})
from app.celery_tasks.apps import MysqlCon
from app.instance.models import InstanceInfo
from app.instance.models import DbTableInfo
import configparser,os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
configfile =  os.path.join(PROJECT_ROOT, 'env.txt'),

config = configparser.ConfigParser()
config.read(configfile, encoding='utf8')
blacklists = config.get('mysql_filter_dbname','blacklist')

class TableInfo():
    """
    表结构信息采集
    """
    def __init__(self):
        pass

    def GetInstanceList(self):
        """
        获取实例列表
        :return: 返回一个列表
        """
        blacklist = blacklists
        instancelist = []
        instance = InstanceInfo.objects.filter(online=1).values('instance_host','instance_name','instance_port')
        for row in instance:
            dbinfo = {}
            mydb = MysqlCon(row['instance_host'],row['instance_port']).SqlCheck()
            dbinfo['instance_host'] = row['instance_host']
            dbinfo['instance_name'] = row['instance_name']
            dbinfo['instance_port'] = row['instance_port']
            dbinfo['db_name'] = [x['Database'] for x in mydb if x['Database'] not in blacklist]
            instancelist.append(dbinfo)
        return instancelist

    def GetTableList(self):
        """
        获取table列表
        :return: 返回一个列表
        """
        instanceinfo = self.GetInstanceList()
        ins_tables = []
        for ins in instanceinfo:
            for db in ins['db_name']:
                dbs = {}
                mytable = MysqlCon(ins['instance_host'], ins['instance_port'],db).SqlInput('show tables;')
                table_list = [x[k] for x in mytable for k in x]
                dbs['instance_host'] = ins['instance_host']
                dbs['instance_name'] = ins['instance_name']
                dbs['instance_port'] = ins['instance_port']
                dbs['db_name'] = db
                dbs['table_name'] = table_list
                ins_tables.append(dbs)
        return ins_tables

    def GetTableStructure(self):
        """
        获取table表结构信息,添加表结构信息
        :return: 插入数据到app_dbtableinfo表
        """
        table_list = self.GetTableList()
        database_list = self.GetInstanceList()
        try:
            for databa in database_list:
                DbTableInfo.objects.filter(instance_host=databa['instance_host']).exclude(db_name__in=databa['db_name']).delete()
            del_instance = [x['instance_host'] for x in database_list]
            del_instance_host = list(set(del_instance))
            DbTableInfo.objects.exclude(instance_host__in=del_instance_host).delete()
            for row in table_list:
                for table in row['table_name']:
                    tableinfo = {}
                    try:
                        tb_size = MysqlCon(row['instance_host'], row['instance_port'], row['db_name']).SqlInput(
                            "select (DATA_LENGTH + INDEX_LENGTH)/1024/1024 as table_size from information_schema.tables where table_schema='%s' and table_name='%s';" % (
                            row['db_name'], table)) # 获取表空间大小。
                        if  DbTableInfo.objects.filter(instance_host=row['instance_host'],db_name=row['db_name'],table_name=table).values('table_name').first():
                            DbTableInfo.objects.filter(instance_host=row['instance_host'],db_name=row['db_name'],table_name=table).update(table_size=tb_size[0]['table_size'])
                        else:
                            tb = MysqlCon(row['instance_host'], row['instance_port'], row['db_name']).SqlInput(" show create table `%s`; "%table)
                            tableinfo['instance_host'] = row['instance_host']
                            tableinfo['instance_name'] = row['instance_name']
                            tableinfo['instance_port'] = row['instance_port']
                            tableinfo['db_name'] = row['db_name']
                            tableinfo['table_name'] = table
                            tableinfo['table_structure'] = tb[0]['Create Table']
                            tableinfo['table_size'] = tb_size[0]['table_size']
                            DbTableInfo.objects.create(**tableinfo)
                    except Exception as e:
                        print(tableinfo)
                        print(tb)
                        error = "collectTable## error: " + str(e)
                        print(error)
                finish = "collectTable## " + row['instance_name'] + ":" + row['db_name'] + " finish"
                print(finish)
                tables_list = DbTableInfo.objects.filter(instance_host=row['instance_host'],db_name=row['db_name']).values('table_name')
                tables_list = [x['table_name'] for x in tables_list]
                del_table = list(set(tables_list)^set(row['table_name']))
                for dt in del_table:
                    DbTableInfo.objects.filter(instance_host=row['instance_host'], db_name=row['db_name'],table_name=dt).delete()
        except Exception as e:
            error = "collectTable## error: " + str(e)
            print(error)

    def Execute(self):
        return self.GetTableStructure()

def run():
    demo = TableInfo()
    demo.Execute()



if __name__ == "__main__":
    demo = TableInfo()
    print(demo.GetInstanceList())