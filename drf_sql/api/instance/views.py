# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
###使用ViewSets重构
from rest_framework import viewsets
from rest_framework import mixins
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

from api.models import Snippet, Book, UserInfo, DatabaseInfo, WorkSheet
from api.serializers import SnippetSerializer, BookSerializer, DatabaseInfoSerializer, WorkSheetSerializer
# from rest_framework.decorators import detail_route

class SnippetViewSet(viewsets.ModelViewSet):

    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

# class BookViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
class BookViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class UserInfoViewSet(viewsets.ModelViewSet):
#     """
#     用户信息
#     """
#     authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,SessionAuthentication,BasicAuthentication)
#     permission_classes = (IsAuthenticated,)
#     queryset = User.objects.all()
#     serializer_class = UserInfoSerializer


class DatabaseInfoViewSet(viewsets.ModelViewSet):
    """
    MySQL数据库信息,端口号,host,数据库名称。
    只允许list,delete,create操作。
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = DatabaseInfo.objects.all()
    serializer_class = DatabaseInfoSerializer

class WorkSheetViewSet(viewsets.ModelViewSet):
    """
    工单信息表，查看必须带author条件
    """
    # authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    queryset = WorkSheet.objects.all()
    serializer_class = WorkSheetSerializer
    pagination_class = Pagination
    search_fields = ('author',)

class UserInfoViewSet(viewsets.ViewSet):
    """
    获取当前登陆的用户信息
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    def list(self, request, *args, **kwargs):
        is_admin = User.objects.filter(username=self.request.user.username).values('is_superuser').first()
        print is_admin
        roles = is_admin['is_superuser'] and ['admin'] or ['editor']
        print roles
        data = {
            "name": self.request.user.username,
            "roles": roles,
            # "perms": []
            "perms": request.user.get_all_permissions()
        }
        return Response(data)
