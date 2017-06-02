#!/usr/bin/env/python
#coding:utf-8

import json
import requests

headers = {"content-type":"application/json"}
data = {"name":"wd"}
url = "http://192.168.137.101:5001/"

#r = requests.get(url, headers=headers, params=data)

# 后端使用get_json获取后，类型type为<type: 'unicode'>,需要json.loads反解后取值
r = requests.post(url, headers=headers, json=json.dumps(data))

# 后端使用get_json获取后，类型依旧是<tyep: 'dict'> 可以直接取值
#r = requests.put(url, headers=headers, json=data)

# 后端使用get_json获取后，类型依旧是<tyep: 'dict'> 可以直接取值
#r = requests.delete(url, headers=headers, json=data)
print r.status_code
print r.text

