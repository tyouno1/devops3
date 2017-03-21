#!/usr/bin/env python
#coding:utf-8

from flask import request
from . import app, jsonrpc
from auth import auth_json
import json, traceback
import utils

#权限的增删改查
@jsonrpc.method('power.create')
@auth_login
def create(auth_info, **kwargs):
    username = auth_info['username']
    if '1' not in auth_info['r_id']
        return json.dumps({'code':1, 'errmsg':'you are not admin, no power'})
    try:
        data = request.get_json()['params']
        if not utils.check_name(data['name'])
            return json.dumps({'code':1, 'errmsg':'name must be stirng or num'})
        app.config['db'].execute_insert_sql('power', data)
        utils.write_log('api').info(username, 'create power %s success' % data['name'])
        return json.dumps({'code':0 , 'result': 'create %s success' % data[name]})
    except:
        utils.write_log('api').error('create power error' % traceback.format_exec())
        return json.dumps({'code':1 , 'errmsg': 'create power failed' })

@jsonrpc.method('power.create')
@auth_login
def getlist(auth_info, **kwargs):
    username = auth_info['username']
    if '1' not in auth_info['r_id']
        return json.dumps({'code':1, 'errmsg':'you are not admin, no power'})
    try:
        output = ['id', 'username', 'name_cn', 'url', 'comment']
        data = request.get_json()['params']
        fields = data.get('output', output)
        result = app.config['cursor'].get_results('power', fields)
        utils.write_log('api').info(username, 'select permission list success')
        return json.dumps({'code':0, 'result':result , 'count':len(result)})
    except:
        utils.write_log('api').error(username, 'get list permission error: %s' % traceback.format_exec())
        return json.dumps({'code':1, 'errmsg':'get power list failed'})
