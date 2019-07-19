#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: tasks.py 
@time: 2019/1/10 1:21 PM 
"""
# from __future__ import absolute_import
# from celery import app as celery_app
from celery import task
from .celery_tasks.crontab import DataBaseCron
from .celery_tasks.crontab import CollectTable
from .celery_tasks.asynchronous import sendmail
# from .celery_tasks.asynchronous import inception
from .celery_tasks.asynchronous import inception

# 工单服务发送邮件的异步任务
@task
def SendMail(subject, html_content,to_email):
    return sendmail.sendMail(subject, html_content,to_email)

# 实例存活状态的定时任务，没一分钟执行一次。
@task
def CheckMysqlConnect():
    return DataBaseCron.GetDBConnectInfo()

# inception 执行异步任务
@task
def ExecInception(work_id):
    return inception.runInc(work_id)

# 对数据表结构进行收集
@task
def CollectTableInfo():
    return CollectTable.run()