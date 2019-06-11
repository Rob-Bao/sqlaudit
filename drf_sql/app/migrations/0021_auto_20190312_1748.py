# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20190308_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='exec_datetime',
            field=models.PositiveIntegerField(default=0, verbose_name='执行时间，时间戳格式'),
        ),
        migrations.AddField(
            model_name='worksheet',
            name='exec_way',
            field=models.SmallIntegerField(default=0, verbose_name='执行方式 0 代表自动执行 1代表手动执行'),
        ),
    ]
