# -*- coding: utf-8 -*-
"""
Django settings for SqlAudit project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, datetime, sys
# import ldap3
# from django_auth_ldap.config import LDAPSearch,GroupOfNamesType
import djcelery
from celery.schedules import crontab



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # ldap setting
# AUTH_LDAP_SERVER_URI = 'ldap://172.17.116.67:389'
# AUTH_LDAP_BIND_DN = 'cn=Manager,dc=local,dc=com'
# AUTH_LDAP_BIND_PASSWORD = '0x'

# AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=Users,dc=local,dc=com",
#     ldap.SCOPE_SUBTREE, "(cn=%(user)s)")

# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Report,ou=Groups,dc=local,dc=com",
#     ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
# )
# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")


# AUTH_LDAP_USER_ATTR_MAP = {
#     "email": "mail",
#     "username": "cn",
#     "name_cn": "sn"
# }

# AUTH_LDAP_MIRROR_GROUPS = True
# AUTH_LDAP_ALWAYS_UPDATE_USER = True

# AUTHENTICATION_BACKENDS = (
#     'django_auth_ldap.backend.LDAPBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mi!uhlx6ga!wx&*lm*^tswom&6&(r1emhn!_t8kes6x206j8vb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'djcelery',
    'app',


]

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    # ),
}

JWT_AUTH = {
    'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=2), #token过期时间
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1), #token过期时间
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=600), #token过期时间
    'JWT_AUTH_HEADER_PREFIX': 'JWT',    #headers里token的前缀
    'JWT_ALLOW_REFRESH': True, #允许刷新令牌
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'SqlAudit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'https://'
# )

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)



WSGI_APPLICATION = 'SqlAudit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sqlaudit',
        'USER': 'inception_backup',
        'PASSWORD': 'ulpNC79IYdk17ZVNhk',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Harbin'

USE_I18N = True

USE_L10N = True


USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
FILE_CHARSET='utf-8'
DEFAULT_CHARSET='utf-8'

# Celery setting
djcelery.setup_loader()
BROKER_URL= 'redis://127.0.0.1:6379/0' # 配置URL
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 默认超时时间1小时
# CELERY_RESULT_BACKEND = 'redis://r-bp1b95b6c19e5c44.redis.rds.aliyuncs.com:6379/1' # 默认结果存储位置
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'Asia/Shanghai'

# Celery Crontab 定时任务配置项
# 启动方式: python3 manage.py celery worker --loglevel=info --beat
CELERYBEAT_SCHEDULE = {
    "MysqlCron": { # 检查MySQL可用性任务
        "task": "app.tasks.CheckMysqlConnect",  #执行的函数
        "schedule": datetime.timedelta(seconds=180),   # every minute 每分钟执行
        "args": ()  # 任务函数参数
    },
    "DbTableinfo": { # 每天0点，对平台所接入的实例内表结构进行收集。
        "task": "app.tasks.CollectTableInfo",  #执行的函数
        "schedule": crontab(hour=3, minute=30),   # 凌晨3点30执行
        "args": ()  # 任务函数参数
    },
}

# smtp
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.exmail.qq.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = 'monitor@lanjingren.com' # 帐号
EMAIL_HOST_PASSWORD = 'Bzh4PVjvog9puatg'  # 密码
DEFAULT_FROM_EMAIL = 'MySQL语法审核系统 <monitor@lanjingren.com>'
