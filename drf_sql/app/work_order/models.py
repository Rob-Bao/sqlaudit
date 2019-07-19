#!/usr/bin/env python  
# encoding: utf-8

from django.db import models



class WorkSheet(models.Model):
    work_id = models.PositiveIntegerField(verbose_name='工单ID', default=0, blank=False)
    workname = models.CharField(verbose_name='工单名称', max_length=200, blank=True)
    c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    u_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    author = models.CharField(verbose_name='工单所有者', max_length=50, blank=True)
    auditor = models.CharField(verbose_name='工单设计人', max_length=50, blank=True)
    dba = models.CharField(verbose_name='管理员', max_length=50, blank=True, default='')
    work_status = models.SmallIntegerField(verbose_name='工单状态 -2 管理员驳回 -1 审核员驳回'
                                                        ' 0 审核中 1 等待管理员操作 2 等待程序处理 3 代表工单完成',
                                           default=0, blank=False)
    instance = models.CharField(verbose_name='实例名', max_length=200, blank=True)
    db_name = models.CharField(verbose_name='数据库名', max_length=50, blank=True)
    db_port = models.PositiveIntegerField(verbose_name='实例端口', default=3306, blank=False, null=False)  # PositiveIntegerField 为无符号的整数;
    db_sql = models.TextField(verbose_name='执行语句', blank=False, default='')
    work_note = models.CharField(verbose_name='工单备注', max_length=500, blank=True, default='')
    rejected_note = models.CharField(verbose_name='', max_length=500, blank=True, null=True)
    exec_way = models.SmallIntegerField(verbose_name='执行方式 0 为默认值 1 代表自动执行 2代表手动执行', default=0, blank=False)
    exec_timepoint = models.SmallIntegerField(verbose_name='执行的时间点 0 为默认值 1 立即执行 2 第二天凌晨2点执行', default=0, blank=False)

    class Meta:
        ordering = ('c_time',)

class InceptionRes(models.Model):
    work_id = models.PositiveIntegerField(verbose_name='工单ID', blank=False)
    c_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    exec_status = models.SmallIntegerField(verbose_name='执行的状态值 1 执行成功 -1执行失败', blank=False)
    stage = models.CharField(verbose_name='stage', max_length=50, default='', blank=False)
    errlevel = models.PositiveIntegerField(verbose_name='errlevel', blank=False)
    stagestatus = models.CharField(verbose_name='stagestatus', max_length=200, default='', blank=False)
    errormessage = models.TextField(verbose_name='errormessage', blank=False, default='')
    SQL = models.TextField(verbose_name='SQL', blank=False)
    Affected_rows = models.PositiveIntegerField(verbose_name='Affected_rows', default=0, blank=False)
    sequence = models.CharField(verbose_name='sequence', max_length=200, default='', blank=False)
    backup_dbname = models.CharField(verbose_name='backup_dbname', max_length=500, default='', blank=False)
    execute_time = models.CharField(verbose_name='execute_time', max_length=50, default='', blank=False)
    sqlsha1 = models.CharField(verbose_name='sequence', max_length=200, default='', blank=False)

    class Meta:
        ordering = ('c_time',)