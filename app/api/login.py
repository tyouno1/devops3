#!/usr/bin/env python
#coding:utf-8
from flask import Flask, request
from . import app
import utils
import json, time, traceback , hashlib

# 用户登录验证， 并生成token
@app.route('/api/login', methods=['GET'])
def login():
    try:
        username = request.args.get('username', None)
        passwd = request.args.get('passwd', None)
        passwd = hashlib.md5(passwd).hexdigest()
        if not (username and passwd):
            return josin.dumps({'code':1, 'errmsg':'需要输入用户名和密码'})
        result = app.config['db'].get_one_result()
        if not result:
            return
        
        if result[''] == 1:
            return json.dumps()
