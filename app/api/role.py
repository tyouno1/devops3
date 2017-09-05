#!/usr/bin/env python
#coding:utf-8

from flask import Flask
from . import app, jsonrpc
from auth import auth_login
import json, traceback
import utils

#这里是关于用户角色的增删改查及组对应的权限id2name

@jsonrpc.method('role.create')
@auth_login
def role_create(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']
        return json.dumps({'code':1, 'errmsg': 'you are not admin, no power'})
    try:
        data = request.get_json()['params']
        if not data.has_key('p_id'):
            return json.dumps({"code":1, "errmsg":"must have a p_id!"})
        if not app.config['db'].if_id_exist("power",data['p_id'].split(',')):
            return json.dumps({"code":1, "errmsg":"p_id not exist!"})
        if not utils.check_name(data['username']):
            return json.dumps({"code":1, "errmsg":"username must be string or num!"})
        app.config['db'].execute_insert_sql('role', data)
        utils.write_log('api').info('%s create role %s success' % (username, data['name']))
        return json.dumps({'code':0 , 'result': '%s create role %s success' % (username, data[name]}))
    except:
        utils.write_log('api').error('create role error' % traceback.format_exec())
        return json.dumps({'code':1 , 'errmsg': 'create role failed' })


