#!/usr/bin/env python
#coding:utf-8
from flask import request
from . import app, jsonrpc
import time, logging, utils
from auth import auth_login
import json, traceback, hashlib

# 本模块提供用户信息的增删改查，以及用户所在组，所有权限的查询

# 创建用户
@jsonrpc.method('user.create')
@auth_login
def createuser(auth_info, *arg, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    r_id = auth_info['r_id'] #string, eg:'1,2,3'
    if "1" not in r_id :     #角色: id = 1 为sa组，超级管理员
        return json.dumps({'code':1, 'errmsg':'you not admin, no power'})
    try:
        data = request.get_json()['params']
        # api端对传入端参数验证
        if 'r_id' not in data:
            return json.dumps({"code":1, "errmsg":"must need a role!"})
        if not app.config['db'].if_id_exist("role",data['r_id'].split(','))
            return json.dumps({"code":1, "errmsg":"Role not exist!"})
        if not utils.check_name(data['username']):
            return json.dumps({"code":1, "errmsg":"username must be string or num!"})
        if data['password'] != data['repwd']:
            return json.dumps({"code":1, "errmsg":"password equal repwd!"})
        elif len(data['password']) < 6:
            return json.dumps({"code":1, "errmsg":"password must over 6 string !"})
    except:

# 通过传入的条件， 通常为id，查询某条用户的信息，用于管理员修改用户信息
@jsonrpc.method('user.get')
@auth_login
def userinfo(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dump(auth_info)
    username = auth_info['username']



# 更新用户信息
@jsonrpc.method('user.update')
@auth_login
def userupdate(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dump(auth_info)
    username = auth_info['username']
    try:
        data = request.get_json()['params']
        where = data.get('where',None)
        data = data.get('data', None)
        if '1' in auth_info['r_id']:    #管理员更新用户信息
            result = app.config['db'].execute_update_sql('user', data, where)
        else:
            result = app.config['db'].execute_udpate_sql('user', data, {'username':username}, ['name','username', 'email', 'mobile'])
        if not result :
            return json.dumps({"code":1 , "errmsg": 'User not exist'})
        utils.write_log('api').info(username, 'Update user success!')
        return json.dumps({"code":0, "result":"Update user success!"})
    except:
        

