# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-22 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20190319_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instanceinfo',
            name='instance_host',
            field=models.CharField(max_length=150, verbose_name='实例地址'),
        ),
    ]
