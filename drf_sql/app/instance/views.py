# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
###使用ViewSets重构
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import InstanceInfo
from .models import DatabaseInfo
from .models import DbTableInfo
from .serializers import InstanceInfoSerializer
from .serializers import DatabaseInfoSerializer
from .serializers import DbTableInfoSerializer
from .filters import TablesFilter
from rest_framework.pagination import PageNumberPagination
#filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from .filters import DatabaseFilter
from rest_framework.response import Response
from .action import InceptionClass
# from .action import MyConfig
# import configparser




class Pagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class InstanceInfoViewSet(viewsets.ModelViewSet):
    """
    MySQL数据库信息,端口号,host,数据库名称。
    只允许list,delete,create操作。
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = InstanceInfo.objects.all()
    pagination_class = Pagination
    serializer_class = InstanceInfoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('online',)


class DatabaseInfoViewSet(viewsets.ModelViewSet):
    """
    MySQL数据库信息,端口号,host,数据库名称。
    只允许list,delete,create操作。
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = DatabaseInfo.objects.all()
    pagination_class = Pagination
    serializer_class = DatabaseInfoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('instance_id','db_name')

class MysqlSqlCheckViewSet(viewsets.ViewSet):
    """
    MySQL SQL检查接口。
    """
    inc = InceptionClass()
    authentication_classes = (
    JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = DatabaseInfo.objects.all()
    def list(self, request, *args, **kwargs):
        param = {
            'instance_host':self.request.query_params['instance_host'],
            'instance_port':self.request.query_params['instance_port'],
            'dbname':self.request.query_params['dbname'],
            'sql':self.request.query_params['sql'],
            'execute':self.request.query_params['execute']
        }
        data = self.inc.CheckSql(**param)
        return Response(data)

class TableInfoViewSet(viewsets.ModelViewSet):
    """
    表结构信息
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = DbTableInfo.objects.all()
    serializer_class = DbTableInfoSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TablesFilter
