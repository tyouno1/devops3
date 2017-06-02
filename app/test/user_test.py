#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals
import json
import requests

url = 'http:127.0.0.1:4000/api'
def login(username, password):

def rpc():
    res=login('admin','123456')
    result = json.loads(res)
    if result['code'] == 0:
        token = result['token']
        headers = {'content-type':'application/json','authorization':token}
        print token
    else:
        return result
    '''
    # create请求
    data = {
        'jsonrpc':'2.0',
        'method': 'user.create',
        'id':'1',
        'params':{
            'username': 'panda',
            'password': '123456',
            'repwd': '123456',
            'name': 'panda',
            'email': '787696332@qq.com'
            'mobile': '1211459865',
            'r_id': '1.3',
            'is_lock': 0
        }
    }

    # get 请求
    data = {
        'jsonrpc': '2.0'
        'method': 'user.get',
        'id':'1',
        'params':{
            'output': ['id','username','name','email','mobile']
            'where': {'id':2}
        }
    }

    '''
