"""
Django settings for joyous_spring project.

Generated by 'django-admin startproject' using Django 1.11b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

超级管理员
username:twilight
password:8844248w
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%^utq1s%ru5t(tbnz3ab6-=_1(z=fg3%7!&!w-d#(oh!klh+z_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# 设置时区和文字编码
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# Application definition
# 一定要记得注册APP啊喂
INSTALLED_APPS = [
    # 'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'winter_sakura'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'joyous_spring.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'winter_sakura/templates')]  # 添加templates路径，用于寻找html模板
        ,
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

WSGI_APPLICATION = 'joyous_spring.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# 建立与数据库的连接。

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql', # 使用mysql驱动
        'NAME': 'boss',       # 数据库名
        'USER': 'kagari',       # 用户
        'PASSWORD': '8844248w', # 口令
        'HOST': 'localhost',    # 地址
        'POST': '3306',          # 端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# 添加STATIC_ROOT后在html页面中通过{{%load static%}}加载，使用{{%static + 'url'%}}对静态文件进行制指定
# 示例：<link href="{%static "css/plus.css"%}" rel="stylesheet" type="text/css">
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # 添加静态文件目录


# 媒体配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 邮件配置
EMAIL_HOST = 'smtp.qq.com'                #SMTP地址
EMAIL_PORT = 25                                 #SMTP端口
EMAIL_HOST_USER = '1213028676@qq.com'       #我自己的邮箱
EMAIL_HOST_PASSWORD = 'kmkxoboefsiibaai'                  #我的邮箱密码
EMAIL_SUBJECT_PREFIX = u'[snow_rabbit]'            #为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True                             #与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
# 管理员站点
SERVER_EMAIL = '1213028676@qq.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# 任务管理配置
# CRONJOBS = [
#     ('*/5 * * * *', 'winter_sakura.cron.test','>>/home/test.log')
# ]
# 安全配置
#
# ALLOWED_HOSTS = [
#     '192.168.1.125',  # Allow domain and subdomains
# ]
