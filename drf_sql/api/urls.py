#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: urls.py 
@time: 2018/12/18 12:26 PM 
"""


###使用路由器重写urls
from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token

# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'book', views.BookViewSet)
# router.register(r'userinfo', views.UserInfoViewSet)

# API URL现在由路由器自动确定。
# 另外，我们还要包含可浏览的API的登录URL。
urlpatterns = [
    url(r'^', include(router.urls)),
#     # url(r'^userinfo', views.UserInfoViewset),
#     url(r'^user-token-get', obtain_jwt_token), #申请token令牌
#     url(r'^user-token-refresh', refresh_jwt_token), #刷新token令牌
#     url(r'^user-token-verify', verify_jwt_token), #验证token令牌
]
