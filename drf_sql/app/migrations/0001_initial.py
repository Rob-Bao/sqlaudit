# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建的时间')),
                ('db_name', models.CharField(max_length=50, verbose_name='数据库名字')),
                ('instance_id', models.PositiveIntegerField(verbose_name='实例ID')),
                ('instance_port', models.PositiveIntegerField(default=3306, verbose_name='实例端口')),
            ],
            options={
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='InstanceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建的时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.CharField(max_length=50, verbose_name='创建人姓名')),
                ('instance_host', models.CharField(max_length=200, verbose_name='实例地址')),
                ('instance_name', models.CharField(max_length=100, verbose_name='实例名字')),
                ('instance_port', models.PositiveIntegerField(default=3306, verbose_name='实例端口')),
                ('online', models.BooleanField(default=False, verbose_name='在线状态')),
                ('connect_content', models.CharField(default=None, max_length=500, null=True, verbose_name='连接信息')),
            ],
            options={
                'ordering': ('created_time',),
            },
        ),
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_id', models.PositiveIntegerField(default=0, verbose_name='工单号,使用时间戳,不可有负数。')),
                ('workname', models.CharField(max_length=200, verbose_name='工单标题')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建的时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.CharField(max_length=50, verbose_name='创建人姓名')),
                ('auditor', models.CharField(max_length=50, verbose_name='审核员名字')),
                ('admin_name', models.CharField(max_length=50, verbose_name='操作员名字')),
                ('work_status', models.SmallIntegerField(default=0, verbose_name='工单状态; -2：代表管理员驳回，-1：代表审核员驳回，0：代表审核员审核中1：代表管理操作中，2：工单完成')),
                ('instance', models.CharField(max_length=200, verbose_name='实例地址')),
                ('db_name', models.CharField(max_length=50, verbose_name='数据库名字')),
                ('db_port', models.PositiveIntegerField(default=3306, verbose_name='实例端口')),
                ('db_sql', models.CharField(max_length=200, verbose_name='需要执行的SQL内容')),
                ('work_note', models.CharField(max_length=200, verbose_name='工单备注')),
                ('rejected_note', models.CharField(max_length=200, verbose_name='工单备注')),
            ],
            options={
                'ordering': 'updated_time',
            },
        ),
        migrations.AlterUniqueTogether(
            name='instanceinfo',
            unique_together=set([('instance_host', 'instance_name', 'instance_port')]),
        ),
    ]
