#/usr/bin/env python
#coding:utf-8

import logging, logging.handlers
'''
    这个demo是logging模块最适合生产环境使用的方式，思路如下：
    1.通过函数，实例化logger对象(直接配置参数，或者通过配置文件加载参数即可)
    2.函数实例化logger对象之后，并将对象作为返回值，即return logger
    3.其他模块直接调用模块中的函数即可使用，非常简单方便
'''

#定义写日志的函数，返回实例化的logger对象 -- 直接配置logger参数形式
def WriteLog(log_name):
    log_filename = '/tmp/test.log'
    log_level = logging.DEBUG
    format = logging.Formatter('%(asctime)s %(filename)s - [line:%(lineno)s] - %(funcName)s %(levelname)s - %(name)s %(message)s')
    handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(format)
    logger = logging.getLogger(log_name)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger

if __name__ == '__main__':
    WriteLog('api').info('just a test') # 模块内部调用

'''
外部程序调用
import demo
def index()
    demo.WriteLog('api').info('123')

index()
'''
