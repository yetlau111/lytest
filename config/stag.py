# -*- coding: utf-8 -*-
import os
from config import RUN_VER
if RUN_VER == 'open':
    from blueapps.patch.settings_open_saas import *  # noqa
else:
    from blueapps.patch.settings_paas_services import  * # noqa

# 预发布环境
RUN_MODE = 'STAGING'

# 正式环境的日志级别可以在这里配置
# V2
# import logging
# logging.getLogger('root').setLevel('INFO')
# V3
# import logging
# logging.getLogger('app').setLevel('INFO')


# 预发布环境数据库可以在这里配置
#
# DATABASES.update(
#     {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'lytest',  # 数据库名
#             'USER': 'lytest',  # 数据库用户
#             'PASSWORD': 'paas@123',  # 数据库密码
#             'HOST': '10.0.5.104',  # 数据库主机
#             'PORT': '3306',  # 数据库端口
#         },
#     }
# )
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_NAME'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('MYSQL_HOST'),
        'PORT': os.environ.get('MYSQL_PORT'),
    }
}
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')