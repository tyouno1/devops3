#!/usr/bin/env python
#coding:utf-8
# 不使用表关联,将role中的p_id，依据power，转换成文字的形式
from pprint import pprint

role = [
    {'id':1, 'name':'php','p_id':'1,3,4'},
    {'id':2, 'name':'ios','p_id':'2,3'},
    {'id':3, 'name':'sa','p_id':'1,2,3'},
]

power = {
    '1':'git',
    '2':'elk',
    '3':'jiankong',
    '4':'cdn'
}

result=[]
for x in role:
    p_name = [ power[p_id] for p_id in x['p_id'].split(',') if p_id in power]
    x['p_id'] = ','.join(p_name)
    result.append(x)

pprint(result)
pprint(role)

'''
In [13]: result
Out[13]: 
[{'id': 1, 'name': 'php', 'p_id': 'git,jiankong,cdn'},
 {'id': 2, 'name': 'ios', 'p_id': 'elk,jiankong'},
 {'id': 3, 'name': 'sa', 'p_id': 'git,elk,jiankong'}]

In [14]: role
Out[14]: 
[{'id': 1, 'name': 'php', 'p_id': 'git,jiankong,cdn'},
 {'id': 2, 'name': 'ios', 'p_id': 'elk,jiankong'},
 {'id': 3, 'name': 'sa', 'p_id': 'git,elk,jiankong'}]
 '''
