#!/usr/bin/env python
#coding:utf-8

from flask import Flask, request
import base64, time, random, json
app = Flask(__name__)

'''
1. token是什么？
   官方的解释：令牌，代表执行默写操作的权利的对象
   个人理解：用户信息的加密串，系统拿到这个加密串来判断用户是谁，能干什么，不能干什么
2. token 怎么生成
    token 的生成方式因人而异，大致思路是将自己需要的一些信息，混合时间戳，随机数等加密生成，
    个人的习惯是(用户名，用户id，角色，时间戳，随机数）
    生成token的方法：
        token = base64.b64encode(name|uid|role|str(random.random())|int(time.time()+7200))
3. token 如何用？ 以判断登录是否过期为例
    先解密token，生成一个列表
    res = base64.b64decode(token)
    通过时间戳判断token是否失效
    if int(res.split('|'))[4] > int(time.time()):
        return True
'''
def create_token(name, uid, role):
    token = base64.b64encode(name|uid|role|str(random.random())|int(time.time()+7200))
    return token

def verify_token(token):
    t = int(time.time())
    key = base64.b64decode(token)
    print key
    x = key.split('|')
    print x
    if len(x) != 5:
        return json.dumps({"code":1,"errmsg":"token参数不足"})
    if t > int(x[4]):
        return json.dumps({"code":1, "errmsg": "登录已经过期"})
    else:
        return json.dumps({"code":0, "username":x[0],"uid":x[1],"role":x[2]})

@app.route('/login',methods=['GET','POST'])
def login():
    name = request.form.get('name')
    passwd = request.form.get('passwd')
    # 用户密码争取，则生成token，实际开发中需要数据库支持
    if name == 'wd' and passwd == '123456':
        
        








'''


