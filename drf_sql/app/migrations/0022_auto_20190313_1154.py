# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20190312_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='exec_status',
            field=models.SmallIntegerField(default=0, verbose_name='执行的状态值 0 未执行 1 执行中 2 执行成功 -1 执行失败'),
        ),
        migrations.AddField(
            model_name='worksheet',
            name='exec_timepoint',
            field=models.SmallIntegerField(default=0, verbose_name='执行的时间点 0 立即执行 1 第二天凌晨2点执行'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='exec_datetime',
            field=models.PositiveIntegerField(default=0, verbose_name='执行时间，时间戳格式,记录celery执行完成的时间点'),
        ),
    ]
