#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: test.py 
@time: 2019/3/1 12:26 PM 
"""
from action import InceptionClass

def demo():
    a = InceptionClass()
    print(a.CheckSql('rm-2ze76g4a66f5h4645747.mysql.rds.aliyuncs.com', '3306', 'zabbix', '', 0))

if __name__ == '__main__':
    demo()