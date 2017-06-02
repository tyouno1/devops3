#!/usr/bin/env python
#coding:utf-8
from pprint import pprint
''' 
实现查询表中任意两列，并将结果拼接为字典
fields为list两个字段，格式为['field1','field2'],例如：['id','name'], ['name','r_id']
结果1：两列都是字符，如：用户id2name {'1':'tom', '2': 'jerry'}
'''
fields = ['id','name']
data = [{'id':1, 'name': 'wd'}, {'id':2, 'name':'zq'}, {'id':3, 'name':'test'}, {'id':4, 'name':'momo'} ]
result = dict( (str(x[fields[0]]), x[fields[1]].split(',')) for x in data )
pprint(result)

'''
结果2：第二列是一个列表，如：用户name2r_id: {'wd':['1','2'], 'admin':['1','2','3']}
'''
fields = ['name','r_id']
data = [{'name': 'wd', 'r_id': '1,2,3' }, {'name':'zq', 'r_id':'2,3,4'}, {'name':'test', 'r_id':'3,4,5'}, {'name':'momo', 'r_id':'4,5,6'} ]
result = dict( (str(x[fields[0]]), x[fields[1]].split(',')) for x in data )
pprint(result)
