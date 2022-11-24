# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['celery_app', 'RUN_VER', 'APP_CODE', 'SECRET_KEY', 'BK_URL', 'BASE_DIR']

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息

# SaaS运行版本，如非必要请勿修改
RUN_VER = 'open'
# SaaS应用ID
APP_CODE = 'lytest'
# SaaS安全密钥，注意请勿泄露该密钥
SECRET_KEY = '0fc5744a-8c00-4d8f-9ca6-098506fe18de'
# 蓝鲸SaaS平台URL，例如 http://paas.bking.com
BK_URL = 'http://paas.ce16.bktencent.com:80'
# BK_URL = os.getenv("BK_PAAS_HOST")
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(
    __file__)))

def get_env_or_raise(key):
    """Get an environment variable, if it does not exist, raise an exception"""
    value = os.environ.get(key)
    if not value:
        raise RuntimeError(
            (
                'Environment variable "{}" not found, you must set this variable to run this application.'
            ).format(key)
        )
    return value

# SaaS应用ID
APP_CODE = os.getenv("BKPAAS_APP_ID")
# SaaS安全密钥，注意请勿泄露该密钥
SECRET_KEY = os.getenv("BKPAAS_APP_SECRET")
# PAAS平台URL
BK_URL = os.getenv("BKPAAS_URL")
# ESB API 访问 URL
BK_COMPONENT_API_URL = os.getenv("BK_COMPONENT_API_URL")