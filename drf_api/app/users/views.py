# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
###使用ViewSets重构
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserInfoSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User, Permission
from rest_framework.response import Response
from rest_framework import mixins



class Pagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class UserInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    用户相关操作
    get请求中，如果添加了username参数，将返回用户名，角色，和权限信息。
    put请求中，将对权限进行更改。主要更改审核员的权限。一共三个角色，分别为（admin,audit,user）
    """
    authentication_classes = (
        JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    # pagination_class = Pagination
    queryset = User.objects.all()
    def list(self, request, *args, **kwargs):
        # if self.request.query_params != {} and self.request.query_params['username']:
        if 'username' in self.request.query_params:
            is_admin = self.queryset.filter(username=self.request.user.username).values('is_superuser').first()
            if is_admin['is_superuser']:
                roles = ['admin']
            elif len(request.user.get_all_permissions()) > 0:
                roles = ['auditor']
            else:
                roles = ['user']
            # roles = is_admin['is_superuser'] and ['admin'] or ['editor']
            data = {
                "name": self.request.user.username,
                "roles": roles,
                "perms": request.user.get_all_permissions()
            }
            return Response(data)
        else :
            data = self.queryset.filter().values()
            return Response(data)


class UserPermsInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    权限相关
    put请求中，将对权限进行更改。主要更改审核员的权限。一共三个角色，分别为（admin,auditor,user）
    """
    authentication_classes = (
        JSONWebTokenAuthentication, TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    perms = Permission.objects.all()

    def update(self, request, *args, **kwargs): # 设置用户的权限，切换三个角色。
        data = {}
        if self.request.data['user'] == self.request.user.username:
            data['message'] = '不允许更改自己的权限'
            data['type'] = 'warning'
        else:
            data['type'] = 'success'
            user_action = self.queryset.filter(username=self.request.data['user']) # 实例化用户的操作
            myuser = User.objects.get(username=self.request.data['user'])  # 实例化该用户
            if self.request.data['role'] == 'auditor': # 变更为审核员操作
                auditperms_list = ['change_worksheet']  # 审核员权限列表
                auditPermsid = []
                user_action.update(is_superuser=0) # 降级为普通用户
                for per in auditperms_list:
                    content_type_ids = self.perms.filter(codename=per).values('content_type_id').first()
                    auditP = self.perms.filter(content_type_id = int(content_type_ids['content_type_id'])).values('id')
                    for ids in auditP:
                        auditPermsid.append(ids['id']) # 检索权限ID
                myuser.user_permissions.set(auditPermsid)  # 授权操作
                data['message'] = user_action.update(is_staff=1) == 1 and "授权为审批人成功" or user_action.update(is_staff=1)
            elif self.request.data['role'] == 'admin': # 变更为管理员操作
                data['message'] = user_action.update(is_superuser=1,is_staff=0) == 1 and "升级为管理员成功"
            elif self.request.data['role'] == 'user':
                user_action.update(is_superuser=0,is_staff=0)  # 降级为普通用户
                myuser.user_permissions.clear()
                data['message'] = '降级为使用人成功'
        return Response(data)
