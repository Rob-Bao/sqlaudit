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
from django.contrib.auth.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ('password','email')

if __name__ == "__main__":
    pass 