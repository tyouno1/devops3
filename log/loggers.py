#coding:utf-8

import logging
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')

# 创建一个handler，用于写入日志文件，值输出debug级别以上的日志
fh = logging.FileHandler('test.log')
fh.setFormatter(formatter)

# 创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setFormatter(formatter)

# 创建一个logger命名为mylogger, %{name}s 可以调用这个名字
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

# 记录两条日志
logger.info('foobar')
logger.debug('just a test')
