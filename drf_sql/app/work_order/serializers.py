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
import datetime
from rest_framework import serializers
from .models import  WorkSheet
from .models import  InceptionRes
from django.contrib.auth.models import User
# email
from ..tasks import SendMail as sendMail
from ..tasks import ExecInception as execInception

# from ..sendmail import sendMail

class InceptionResSerializer(serializers.ModelSerializer):
    """
    工单执行结果
    """
    class Meta:
        model = InceptionRes
        fields = ['work_id','c_time','exec_status','errormessage','SQL']
        # exclude = ['work_id', ]  # 排除字段

class WorkSheetSerializer(serializers.ModelSerializer):
    """
    工单列表
    """
    subject_s = "SQL申请通知"
    subject_f = "SQL申请驳回通知"
    audit_mes = "<p>你有一个SQL申请需要审批，请登录SQL审核系统查看。</p><p>请点击: http://sqlaudit.meipian.cn/#/task/myapproval</p>"
    worko_mes = "<p>你有一个SQL申请被驳回，请登录SQL审核系统查看。</p><p>请点击: http://sqlaudit.meipian.cn/#/task/mytask/</p>"
    class Meta:
        model = WorkSheet
        fields = "__all__"
        # exclude = ['price',]  # 排除字段

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        auditor = validated_data['auditor']
        auditor = User.objects.filter(username=auditor).values('email').first()
        sendMail.apply_async((self.subject_s, self.audit_mes, auditor['email']))
        return instance

    def update(self, instance, validated_data):
        instances = self.Meta.model.objects.filter(id=instance.id).update(**validated_data)
        work_id = self.Meta.model.objects.filter(id=instance.id).values('work_id').first()
        if 'rejected_note' in validated_data :
            author = self.Meta.model.objects.filter(id=instance.id).values('author').first()
            author_email = User.objects.filter(username=author['author']).values('email').first()
            sendMail.apply_async((self.subject_f, self.worko_mes, author_email['email']))
        elif validated_data['work_status'] == 1:
            admins_email = []
            for admin in User.objects.filter(is_superuser=1).values('email'):
                admins_email.append(admin['email'])
            sendMail.apply_async((self.subject_s, self.audit_mes, admins_email))
        elif validated_data['work_status'] == 2:
            if validated_data['exec_way'] == 1:
                exec_time = ''
                if validated_data['exec_timepoint'] == 1:
                    exec_time = datetime.datetime.now() + datetime.timedelta(minutes=1)  # 当前时间+2分钟后执行。
                elif validated_data['exec_timepoint'] == 2:
                    now = datetime.datetime.now()
                    exec_time = now - datetime.timedelta(
                        hours=now.hour, minutes=now.minute, seconds=now.second,microseconds=now.microsecond) \
                                + datetime.timedelta(hours=26, minutes=00, seconds=00)   # 明天凌晨2:00:00开始执行
                execInception.apply_async((work_id['work_id'],),eta=exec_time)
        return instances




if __name__ == "__main__":
    pass 