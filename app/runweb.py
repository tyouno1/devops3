#/usr/bin/env python
#coding:utf-8

from web import app
import os, sys
import utils

# session 使用需要设置secret_key
app.secret_key = ''

# 导入自定义的各种配置参数，最终参数以字典形式返回
config = utils.get_config('web')

# 将参数追加到app.config字典中，就可以随意使用了
app.config.update(config)

# 实例化数据库类，并将实例化的对象导入配置
app.config['db'] = db.Cursor(config)

if __name__ == '__main__':
    app.run(host=config.get('bind', '0.0.0.0'),
        port=int(config.get(config.get('port'))),
        debug=True)
