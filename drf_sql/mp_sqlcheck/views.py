#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: BaoChengCai   
@contact: baochengcai@lanjingren.com
@site: http://www.meipian.cn 
@software: PyCharm 
@file: views.py 
@time: 2018/12/18 12:24 PM 
"""

from django.views.generic import View
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
import  requests

class Login(View):
    """
    使用基于类的通用视图
    """
    def get(self,request):
        return render(request, 'login.html') #高版本使用

    def post(self,request):
        PostData = request.POST
        username = PostData.get('Username')
        password = PostData.get('Password')
        res = requests.session()
        url = "http://127.0.0.1:8000/api-login/"
        data = {'username': username, 'password': password}
        resp = res.post(url,data)
        return  HttpResponse(resp)





if __name__ == "__main__":
    pass 