#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os, os.path
import time, json
import base64
import hashlib
import traceback
import ConfigParser
import logging, logging.config

work_dir = os.path.dirname(os.path.realpath(__file__))
def get_config(section=''):
    config = ConfigParser.ConfigParser()
    service_conf = os.path.join(work_dir, 'conf/service.conf')
    config.read(service_conf)

    conf_items = dict(config.items('common')) if config.has_section('common') else {}
    # print conf_items #dict
    if section and config.has_section(section):
        conf_items.update(config.items(section))
    return conf_items


def write_log(loggername):
    log_conf=os.path.join(work_dir, 'conf/logger.conf')
    logging.config.fileConfig(log_conf)
    logger = logging.getLogger(loggername)
    return logger

def get_validate(username, uid, role, fix_pwd):
    t = int(time.time())
    return base64.b64encode('%s|%s|%s|%s|%s' % (username, t, uid, role, fix_pwd)).strip()

def validate(key, fix_pwd):
    t = int(time.time())
    key = base64.b64decode(key)
    x = key.split('|')
    if len(x) != 5:
        write_log('api').warning("token参数数量不足")
        return json.dumps({"code":1,"errmsg":"token参数不足"})
    if t > int(x[4]):
        write_log('api').warning("登录已经过期")
        return json.dumps({"code":1, "errmsg": "登录已经过期"})
    if fix_pwd == x[4]:
        write_log('api').warning("api认证通过")
        return json.dumps({"code":0, "username":x[0],"uid":x[2],"r_id":x[3]})
    else:
        write_log('api').warning("密码不正确")
        return json.dumps({"code":1, "errmsg": "密码不正确")

def getinfo(table_name, fields):
    '''
    实现查询表中任意两列，并将结果拼接为字典
    fields为list两个字段，格式为['field1','field2'],例如：['id','name'], ['name','r_id']
    结果1：两列都是字符，如：用户id2name {'1':'tom', '2': 'jerry'}
    结果2：第二列是一个列表，如：用户name2r_id: {'wd':['1','2'], 'admin':['1','2','3']}
    '''
    result = app.config['db'].get_results(table_name, fields) # [{'id':1, 'name': 'wd'}, ...]
    if fields[1] in ['r_id','p_id', 'p_user', 'p_group']:
        result = dict( (str(x[fields[0]]), x[fields[1]].split(',')) for x in result )
    else:
        result = dict( (str(x[fields[0]]), x[fields[1]]) for x in result )

# 获取一个组里面的用户成员，以用户表的r_id,反推出组成员，故如果组内无成员，则这个组就不会返回
def role_members():
    users = getinfo('user',['id','username'])   # {'1':'wd', '2':'pc'}
    roles = getinfo('role',['id','name'])       # {'1':'sa', '2':'dba','3':'dev'}
    r_id = getinfo('user',['id','r_id'])        # {'1':['1','2'], '2':['2','3'] ... }

    g = {}
    for uid , rids in r_id.itmes():
        for rid in rids:
            if uid not in users or rid not in roles:
                continue
            if roles[rid] not in g:
                g[roles[rid]] = []
            g[roles[rid]].append(users[uid])
    return g
    # print g #{'sa': ['wd'], 'dba':['wd','pc'], 'dev':['pc']}

def project_members():
    users = getinfo('user', ['id', 'username'])   #
    roles = getinfo('role', ['id', 'name'])
    r_users = role_members()
    result = app.config['db'].get_results('project', ['id','name','principal','p_user','p_group'])
    pro_pri = {}
    projects = {}
    for p in result:
        projects.setdefault(p['name'],[])
        pro_pri.setdefault(p['name'],[])
        for pri in p['principal'].split(','):
            if pri in users:
                prijects[p['name']].append(users[pri])
                pro_pri[p['name']].append(users[pri])
        for u in p['p_user'].split(','):
            if u in users:
                projects


