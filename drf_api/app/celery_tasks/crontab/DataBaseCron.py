#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: CheckMysqlConnect.py 
@time: 2019/1/10 6:46 PM 
"""
# import os
# os.environ.update({"DJANGO_SETTINGS_MODULE": "SqlAudit.settings"})

from app.instance.models import DatabaseInfo
from app.instance.models import InstanceInfo
from app.celery_tasks.apps import MysqlCon
import configparser,os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
configfile =  os.path.join(PROJECT_ROOT, 'env.txt'),

config = configparser.ConfigParser()
config.read(configfile, encoding='utf8')
blacklists = config.get('mysql_filter_dbname','blacklist')

def GetDBConnectInfo():
    blacklist = blacklists
    instance = InstanceInfo.objects.values('id','instance_host', 'instance_port')
    instance_id = [x['id'] for x in instance]
    DatabaseInfo.objects.exclude(instance_id__in=instance_id).delete()
    for row in instance:
        try:
            databases_res = MysqlCon(row['instance_host'], row['instance_port']).SqlCheck()
            exec_list = []
            for db in databases_res:
                if db['Database'] not in blacklist:
                    exec_list.append(db['Database'])
                    if not DatabaseInfo.objects.filter(instance_id=row['id'], db_name=db['Database']).values('id'):
                        DatabaseInfo.objects.create(db_name=db['Database'], instance_id=row['id'],
                                                instance_port=row['instance_port'])
            InstanceInfo.objects.filter(id=row['id']).update(online=True, connect_content='successful')
            dababases_list = DatabaseInfo.objects.filter(instance_id=row['id']).values('db_name')
            db_list = [x['db_name'] for x in dababases_list]
            no_db_list = list(set(exec_list)^set(db_list))
            for no_db in no_db_list:
                DatabaseInfo.objects.filter(db_name=no_db).delete()
            succe = "checkMysql-successful: " + row['instance_host']
            print(succe)
        except Exception as e:
            error = "checkMysql-error: " + str(row['instance_host']) + "---" + str(databases_res)
            InstanceInfo.objects.filter(id=row['id']).update(online=False, connect_content=str(databases_res))
            print(error)
    return None
if __name__ == "__main__":
    pass