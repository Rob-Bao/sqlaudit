# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-08 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20190403_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbTableInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建的时间')),
                ('instance_host', models.CharField(max_length=200, verbose_name='实例地址')),
                ('instance_name', models.CharField(max_length=100, verbose_name='实例名字')),
                ('instance_port', models.PositiveIntegerField(verbose_name='实例端口')),
                ('db_name', models.CharField(max_length=100, verbose_name='数据库名字')),
                ('table_name', models.CharField(max_length=100, verbose_name='表名字')),
                ('table_structure', models.TextField(default='', verbose_name='表结构')),
            ],
            options={
                'ordering': ('instance_name',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='dbtableinfo',
            unique_together=set([('instance_host', 'instance_name', 'instance_port', 'db_name', 'table_name')]),
        ),
    ]