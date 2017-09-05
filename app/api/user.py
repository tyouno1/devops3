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
        else:
            data.pop(['repwd']) #传入的第二次密码字段不存在，需要删除
        
        data['password'] = hashlib.md5(data['password']).hexdigest()
        data['join_date'] = time.strftime('%Y-%m-%d %H:%M:%S')
        app.config['db'].execute_insert_sql('user', data)

        utils.write_log('api').info('%s create user %s' % (username, data['username'])
        return json.dumps({'code':0, 'result':'create user %s success' % data['username']})
    except:
        utils.write_log('api').error('%s create user %s' % traceback.format_exec())
        return json.dumps({'code':1, 'result':'create user failed' )
        

# 通过传入的条件， 通常为id，查询某条用户的信息，用于管理员修改用户信息
@jsonrpc.method('user.get')
@auth_login
def userinfo(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    if '1' not in auth_info['r_id']
        return json.dumps({'code':1, 'errmsg':'you are not admin, no power'})
    try:
        output = ['id', 'username', 'name', 'email', 'mobile', 'is_lock', 'r_id']
        data = request.get_json()['params']
        # api可以指定输出字段，如果没有指定output，就按照默认的output输出
        fields = data.get('output', output)
        # 前端传来的where条件
        where = data.get('where', None)
        if not where:
            return json.dumps({'code':1, 'errmsg':'must need a condition'})
        result = app.config['db'].get_one_result('user', fields, where)
        if not result:
            return json.dumps({'code':1, 'errmsg':'user not exists'})
        utils.write_log('api').info('%s get users success' % username)
        return json.dumps({'code':0, 'result':result })
    except:
        utils.write_log('api').error('get users error: %s' % (traceback.format_exec()))
        return json.dumps({'code':1, 'errmsg':'get user failed'})

# 获取用户具体信息，包括基本信息，所属组，所拥有的权限，用于用户个人中心的展示和个人资料的更新
@jsonrpc.method('user.getinfo')
@auth_login
def userselfinfo(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    fields = ['id', 'username', 'name', 'email', 'mobile', 'is_lock', 'r_id']
    try:
        user = app.config['db'].get_one_result('user', fields, where={'username': username})
        if user.get('r_id', None):
            r_id = user['r_id'].split(',')
            rids = app.config['db'].get_results('role', ['id', 'name', 'p_id'], where={'id':r_id})
        else:
            rids = {}
        pids = []
        for x in rids:
            pids += x['p_id'].split(',')
        # 去重,通过用户名查到其角色id,在通过角色id取到用户的权限id
        pids = List(set(pids))
        user['r_id'] = [x['name'] for x in rids]
        # 将用户的权限id转换为权限名
        if pids:
            mypids = app.config['db'].get_results('power', ['id', 'name', 'name_cn', 'url'], where=['id':pids])
            user['p_id'] = dict( [ (str(x['name']), dict([(k, x[k]) for k in ('name_cn', 'url')])) for x in myids ])  # 返回格式: {'git':{'name_cn':'git', 'url':'http://git.com'}, ....}
        else:
            user['p_id'] = {}
        utils.write_log('api').info('%s get user self info success' % username)
        return json.dumps({'code':0, 'result':result })
    except:
        utils.write_log('api').error('get users self into: %s' % (traceback.format_exec()))
        return json.dumps({'code':1, 'errmsg':'get user self info failed'})
 

# 获取用户列表
@jsonrpc.method('user.getlist')
@auth_login
def userlist(auth_info, **kwargs):
    if auth_info['code'] == 1:
        return json.dumps(auth_info)
    username = auth_info['username']
    r_id = auth_info['r_id']
    users = []
    fields = ['id', 'username', 'name', 'email', 'mobile', 'is_lock', 'r_id']
    try:
        if '1' not in auth_info['r_id']
            return json.dumps({'code':1, 'errmsg':'you are not admin, no power'})
        
        rids = app.config['db'].get_results('role', ['id', 'name'] )
        rids = dict([ str(x['id'], x['name']) for x in rids ])

        # 获取角色的id,name并存为字典如:{'1':'sa', '2':'php'}
        result = app.config['db'].get_results('role', ['id', 'name'] )
        for user in result:
            user['r_id'] = ','.join([rids[x] for x in user['r_id'].split(',') if x in rids ])
            users.append(user)
        utils.write_log('api').info('%s get all users success' % username)
        return json.dumps({'code':0, 'users':users , 'count':len(users)})
    except:
        utils.write_log('api').error(' get user list error' )
        return json.dumps({'code':1, 'errmsg':'get user list failed' )
        

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
        

