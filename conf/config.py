# -*- coding: utf-8 -*-

# Config里面算是通用配置,子类分别定义专属配置

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass
