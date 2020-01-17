#!/usr/bin/env python  
# encoding: utf-8  

from django.db import models


class DatabaseInfo(models.Model):
    created_time = models.DateTimeField('创建的时间', auto_now_add=True)
    db_name = models.CharField('数据库名字', max_length=100, blank=False)
    instance_id = models.PositiveIntegerField('实例ID', blank=False,null=False) # PositiveIntegerField 为无符号的整数;
    instance_port = models.PositiveIntegerField('实例端口', default=3306, blank=False,
                                          null=False) # PositiveIntegerField 为无符号的整数;
    class Meta:
        ordering = ('created_time',)

class InstanceInfo(models.Model):
    created_time = models.DateTimeField('创建的时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    author = models.CharField('创建人姓名', max_length=50, blank=False)
    instance_host = models.CharField('实例地址', max_length=150, blank=False)
    instance_name = models.CharField('实例名字', max_length=100, blank=False)
    instance_port = models.PositiveIntegerField('实例端口', default=3306, blank=False,
                                          null=False) # PositiveIntegerField 为无符号的整数;
    online = models.BooleanField('在线状态', default=False, blank=False) # BooleanField 为布尔类型，在线为 True,下线为 False;
    connect_content = models.CharField('连接信息', default=None, max_length=500,
                                       null=True)
    class Meta:
        ordering = ('id',)
        unique_together = (("instance_host","instance_name", "instance_port"),)  # 两条数据的两个字段内容不可以重复

class DbTableInfo(models.Model):
    created_time = models.DateTimeField('创建的时间', auto_now_add=True)
    instance_host = models.CharField('实例地址', max_length=200, blank=False)
    instance_name = models.CharField('实例名字', max_length=100, blank=False)
    instance_port = models.PositiveIntegerField('实例端口', blank=False,
                                          null=False) # PositiveIntegerField 为无符号的整数;
    db_name = models.CharField('数据库名字', max_length=300, blank=False)
    table_name = models.CharField('表名字', max_length=300, blank=False)
    table_structure = models.TextField(verbose_name='表结构', blank=False, default='')
    table_size = models.FloatField(verbose_name='表数据空间大小,单位M',max_length=10, default=0)

    class Meta:
        unique_together = (("instance_host", "instance_name", "instance_port", "db_name", "table_name"),)# 两条数据的字段内容不可以重复