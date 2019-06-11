# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190305_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheet',
            name='admin_name',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='操作员名字'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='rejected_note',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='驳回原因备注'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='work_note',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='工单备注'),
        ),
    ]
