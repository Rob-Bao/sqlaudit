# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-07 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190305_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseinfo',
            name='db_name',
            field=models.CharField(max_length=100, verbose_name='数据库名字'),
        ),
    ]