#/usr/bin/env python
#coding:utf-8

from __future__ import unicode_liternals
import json
import requests

url = "http://127.0.0.1:4000/api"
# 登录并获取token
def login(username, password):
    rep_url = "%s/login?username=%s&password=%s" % (url, username, password)
    r = request.get(rep_url)
    result = json.loads(r.content)
    if result['code'] == 0:
        token = result["authorization"]
        return json.dumps({'code':0 , 'token':token})
    else:
        return json.dumps({'code':1, 'errmsg':result['errmsg']})

def rpc():
    res = login('admin','123456')
    result = json.loads(res)
    if int(result['code']) == 0:
        token = result['token']
        headers = {'content-type':'application/json','authorization':token}
        print token
    else:
        print result
        return result
    # create 请求
    data = {
        'jsonrpc': '2.0',
        'method': 'power.create'
        'id': '1',
        'params': {
            'name': 'cdn',
            'name_cn': 'cdn刷新123'
            'url': 'http://cdn.com'
            'commnet':'cdn刷新'
         }
    }
    r = requests.post(url, headers=headers, json=data)
    print r.status_code
    print r.text

if __name__ == '__main__':
   rpc() 

