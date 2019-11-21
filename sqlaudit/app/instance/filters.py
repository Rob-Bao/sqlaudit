#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: filter.py 
@time: 2019/2/25 4:47 PM 
"""


import django_filters
from .models import DatabaseInfo
from .models import DbTableInfo


class DatabaseFilter(django_filters.rest_framework.FilterSet):
    """
    过滤
    """
    class Meta:
        model = DatabaseInfo
        fields = ['instance_id']

class TablesFilter(django_filters.rest_framework.FilterSet):
    """
    表结构信息过滤
    """
    # instance_name = django_filters.CharFilter(lookup_expr='icontains')
    # db_name = django_filters.CharFilter(lookup_expr='icontains')
    table_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = DbTableInfo
        fields = ['instance_name','db_name','table_name']
