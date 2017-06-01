#!/usr/bin/env python
#coding:utf-8
from flask import Flask, request, session , render_template, rediret
from . import app
import requests, json
import utils

headers = {'content-type': 'application/json'}

# 用户登录验证， 并生成token
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.args.get('passwd')
        url = "http://%s/api/login?username=%s&passwd=%s" % (app.config['api_host'],username, password)
        r = requests.get(url, headers=headers) # 请求API验证用户
        result = json.loads(r.content)
        if result['code'] == 0:
            token = result["authorization"]
            # 解密token
            res = utils.validate(token, app.config['passport_key'])
            # return: dict(username:* , uid:* , role:*)
            res = json.loads(res)
            session['author'] = token
            session['username'] = username
            return json.dumps({'code':0})
        else:
            return json.dumps({"code":1,"errmsg":result['errmsg']})

@app.route("/logout", methods=['GET','POST'])
def logout():
    if session.get('author', 'nologin'):
        return redirect('/login')
    session.pop('author',None)
    return redirect('/login')
