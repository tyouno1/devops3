#!/usr/bin/env python
#coding:utf-8

import requests, json
import sys
sys.path.append('../')
import utils
headers={'content-type': 'application/json'}

username='admin'
password='123456'
url = 'http://127.0.0.1:4000/api/login?username=%s&passwd=%s' % (username, password)
result = json.loads(url, headers=headers)
print result
if result['code'] == 0:
    token = result['authorization']
    res = utils.validate(token, '123456') 
    res = json.loads(res)
    print json.dumps({'code':0, 'result':res})
else:
    print json.dumps({'code':1, 'errmsg':result['errmsg']}) 
