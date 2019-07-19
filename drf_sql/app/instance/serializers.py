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
from .models import  DatabaseInfo,InstanceInfo,DbTableInfo


class InstanceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceInfo
        fields = "__all__"

class DatabaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseInfo
        fields = "__all__"

class DbTableInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbTableInfo
        fields = "__all__"

if __name__ == "__main__":
    pass 