#coding:utf-8
import os

class Config:
    SECURITY_KEY = os.environ.get('SECRET_KEY')
    SALARCHEMY_COMMIT_ON_TEARDOWN = True
 
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://reboot:123456@192.168.137.101/test'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://reboot:123456@192.168.137.101/devops'

config = { #将类写成字典的形式存储
    'dev' : DevelopmentConfig,
    'pro' : ProductionConfig,
    'default': DevelopmentConfig
}
