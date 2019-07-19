# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "mp_sqlcheck.settings"})
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def sendMail(subject, html_content,to_email):
    try:
        ToEmail = []
        if type(to_email) != list:
            ToEmail.append(to_email)
        else:
            ToEmail = to_email
        from_email = settings.DEFAULT_FROM_EMAIL
        # subject = '来自SQL审核系统的通知'
        # text_content = '这是一封重要的邮件.'
        # html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
        msg = EmailMultiAlternatives(subject, html_content, from_email, ToEmail)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        print("Send Email Successful.")
        return "Send Email Successful."
    except Exception as e:
        print(e)
        return e

if __name__ == '__main__':
    html_content = "这是一封特别重要的邮件."
    print (sendMail(html_content,'baochengcai@lanjingren.com'))