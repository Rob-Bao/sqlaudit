#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: inception.py 
@time: 2019/3/19 10:45 AM 
"""
# from __future__ import unicode_literals
import os,re
os.environ.update({"DJANGO_SETTINGS_MODULE": "SqlAudit.settings"})
from app.work_order.models import WorkSheet
from app.instance.action import InceptionClass
from app.work_order.models import InceptionRes
from .sendmail import sendMail
from django.contrib.auth.models import User



class Inception_main:
    """
    inception 执行程序
    """
    def __init__(self,work_id):
        """
        初始化
        """
        self.work_id = int(work_id)
        self.inceptionres = InceptionRes.objects.all()
        self.worksheet = WorkSheet.objects.all()

    def readWorksheet(self):
        """
        读取任务列表
        instance 实例地址
        db_name 数据库名称
        db_port 数据库端口
        db_sql  需要执行的SQL
        exec_way 执行方式，0为自动执行，1为手动执行
        exec_timepoint 执行时段，0为立即执行，1为凌晨2点后执行
        :return: work_status =2 的执行任务内容
        """
        worksheetInfo = self.worksheet.filter(work_id=self.work_id, work_status=2).values('work_id','instance','db_name','db_port','db_sql','exec_way','exec_timepoint').first()
        return worksheetInfo

    def sendAuthorEmaiL(self):
        """
        发送邮件功能，调用task的异步任务
        :return:
        """
        author = self.worksheet.filter(work_id=self.work_id).values('author').first()
        author_email = User.objects.filter(username=author['author']).values('email').first()
        author_email = author_email['email']
        sendmail = sendMail("SQL执行完成通知","<p>你有一个SQL工单执行完成，请登录SQL审核系统查看。</p><p>请点击: http://sqlaudit.meipian.cn/#/task/mytask/</p>",author_email)
        return sendmail

    def execInception(self):
        """
        使用inception执行SQL语句
        :return:
        """
        try:
            worksheetInfo = self.readWorksheet()
            print('worksheet: ',worksheetInfo)
            inc = InceptionClass()
            print(inc)
            param = {
                'instance_host': worksheetInfo['instance'],
                'instance_port': worksheetInfo['db_port'],
                'dbname': worksheetInfo['db_name'],
                'sql': re.sub(r'`','',worksheetInfo['db_sql']),
                'execute': 1
            }
            print ('inception start----------------------')
            data = inc.CheckSql(**param)
            print('inc_res: ',data)
            print('inception end-------------------------')

            for row in data:
                del row['ID']
                row['work_id'] = worksheetInfo['work_id']
                row['exec_status'] = int(row['errlevel']) > 0 and -1 or 1
                self.inceptionres.create(**row)
            self.worksheet.filter(work_id=worksheetInfo['work_id']).update(work_status=3) # 修改执行状态，执行完成
            print('sendmail: ',self.sendAuthorEmaiL())
            result = data
        except Exception as e:
            result = e
        return result

def runInc(work_id):
    """
    执行函数
    :return: inception的执行结果
    """
    inceptionMain = Inception_main(work_id)
    return inceptionMain.execInception()



if __name__ == '__main__':
    inceptionMain = Inception_main()
    inceptionMain.readWorksheet()


