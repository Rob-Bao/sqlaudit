# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
###使用ViewSets重构
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from .models import  WorkSheet
from .models import  InceptionRes
from .serializers import  WorkSheetSerializer
from .serializers import  InceptionResSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .filters import WorkSheetFilter
from .filters import InceptionResFilter
from django_filters.rest_framework import DjangoFilterBackend



class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class WorkSheetViewSet(viewsets.ModelViewSet):
    """
    工单信息表
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = WorkSheet.objects.all()
    serializer_class = WorkSheetSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = WorkSheetFilter
    ordering_fields = ('c_time',)
    # 指定默认的排序字段
    ordering = ('-c_time',) #倒序

class InceptionResViewSet(viewsets.ModelViewSet):
    """
    工单任务执行结果表
    """
    authentication_classes = (
    JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = InceptionRes.objects.all()
    serializer_class = InceptionResSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = InceptionResFilter
