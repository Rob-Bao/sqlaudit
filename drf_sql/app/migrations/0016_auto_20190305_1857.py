# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_delete_worksheet_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksheet',
            name='db_sql',
            field=models.TextField(default='', verbose_name=''),
        ),
    ]