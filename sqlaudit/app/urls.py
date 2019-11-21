#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: urls.py 
@time: 2019/1/16 2:29 PM 
"""
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from django.conf.urls import url, include
from .instance import views as instance_views
from .users import views as user_views
from .work_order import views as work_order_views


# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'instance/instanceinfo', instance_views.InstanceInfoViewSet)
router.register(r'instance/databaseinfo', instance_views.DatabaseInfoViewSet)
router.register(r'instance/checkmysql', instance_views.MysqlSqlCheckViewSet)
router.register(r'instance/tableinfo', instance_views.TableInfoViewSet)
router.register(r'workorder/workinfo', work_order_views.WorkSheetViewSet)
router.register(r'workorder/executeres', work_order_views.InceptionResViewSet)
router.register(r'user/userinfo', user_views.UserInfoViewSet)
router.register(r'perms/roleinfo', user_views.UserPermsInfoViewSet)
# router.register(r'user/userperms', user_views.UserPermsViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^user-token-get', obtain_jwt_token), #申请token令牌
    url(r'^user-token-refresh', refresh_jwt_token), #刷新token令牌
    url(r'^user-token-verify', verify_jwt_token), #验证token令牌
]
