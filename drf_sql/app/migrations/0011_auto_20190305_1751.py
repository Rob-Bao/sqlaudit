# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190305_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksheet_test',
            name='work_id',
        ),
        migrations.AddField(
            model_name='worksheet_test',
            name='workname',
            field=models.CharField(default='', max_length=200, verbose_name='工单名称'),
        ),
    ]
