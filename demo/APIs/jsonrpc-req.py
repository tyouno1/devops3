#!/usr/bin/env/python
#coding:utf-8
from __future__ import unicode_literals
import json
import requests

headers = {"content-type":"application/json"}
url = "http://192.168.137.101:5001/api"
data = {
    "jsonrpc": "2.0",
#    "method": "App.index",  #请求后端无参的method
#    "method": "App.name",   #请求后端指定参数的method
    "method": "App.user",    #请求后端不定参数的method,通过形式获取参数
#    "method": "App.users",    #请求后端不定参数的method,通过get_json形式获取参数
    "id": "1",
    "params":{
        "name":"wd",      # 无参数method，此处为空，指定参数的method，指标保留一条参数
        "age":"18" 
    }
}


r = requests.post(url, headers=headers, json=data)

print r.status_code
print r.text
res = json.loads(r.text)

print res
print res['result']
