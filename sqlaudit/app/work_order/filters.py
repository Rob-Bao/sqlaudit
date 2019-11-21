#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: filters.py 
@time: 2019/3/11 5:04 PM 
"""

import django_filters
from .models import WorkSheet
from .models import InceptionRes


class WorkSheetFilter(django_filters.rest_framework.FilterSet):
    """
    过滤类
    """
    sort = django_filters.OrderingFilter(fields=('c_time',))
    workname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = WorkSheet
        fields = ['workname', 'auditor', 'author', 'work_status', 'dba']

class InceptionResFilter(django_filters.rest_framework.FilterSet):
    """
    过来执行结果
    """
    class Meta:
        model = InceptionRes
        fields = ['work_id']