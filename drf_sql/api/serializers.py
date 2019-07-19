#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: serializers.py 
@time: 2018/12/18 12:25 PM 
"""

###简洁模式
from rest_framework import serializers
from api.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Book
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class BookSerializer(serializers.ModelSerializer):
    # created = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    class Meta:
        model = Book
        fields = "__all__"

# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

# class DatabaseInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DatabaseInfo
#         fields = ('id', 'db_host', 'db_name', 'db_port', 'author', 'online', 'connect_content')

# class WorkSheetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WorkSheet
#         fields = "__all__"

if __name__ == "__main__":
    pass 