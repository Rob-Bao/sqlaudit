# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20190313_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheet',
            name='exec_status',
            field=models.SmallIntegerField(default=0, verbose_name='执行的状态值 0 为默认 1 未执行 2 执行成功 -1 执行失败'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='exec_timepoint',
            field=models.SmallIntegerField(default=0, verbose_name='执行的时间点 0 为默认值 1 立即执行 2 第二天凌晨2点执行'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='exec_way',
            field=models.SmallIntegerField(default=0, verbose_name='执行方式 0 为默认值 1 代表自动执行 2代表手动执行'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='work_status',
            field=models.SmallIntegerField(default=0, verbose_name='工单状态 -2 管理员驳回 -1 审核员驳回 0 审核中 1 等待管理员审批 2 后台任务操作中 3 代表工单完成'),
        ),
    ]
