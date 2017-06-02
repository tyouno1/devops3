#!/usr/bin/env python
#coding:utf-8

from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/', methods=['GET','POST','PUT','DELETE'])
def index():
    if request.method == 'GET':
        name = request.args.get("name") #curl "http://192.168.137.101:5001/?name=wd"
        return "GET User is %s" % name
    elif request.method == 'POST':
        #name = request.form.get("name") #curl "http://192.168.137.101:5001/" -d "name=wd" -X POST
        data = request.get_json()
        data = json.loads(data)
        name = data['name']
        return "POST User is %s" % name
    elif request.method=='PUT':
        name = request.form.get("name") #curl "http://192.168.137.101:5001/" -d "name=wd" -X PUT
        #data = request.get_json()
        #name = data['name']
        return "PUT User is %s" % name
    elif request.method == 'DELETE':
        name = request.form.get("name") #curl "http://192.168.137.101:5001/" -d "name=wd" -X DELETE
        #data = request.get_json()
        #name = data['name']
        return "DELETE User is %s" % name

@app.route('/<string:username>',methods=['GET','POST','PUT','DELETE'])
def test(username):
    if request.method == 'GET':
        age = request.args.get('age') #curl "http://192.168.137.101:5001/wd?age=18"
    elif request.method == 'POST':
        age = request.form.get('age') #curl "http://192.168.137.101:5001/wd" -d "age=18" -X POST
    elif request.method == 'PUT':
        age = request.form.get('age') #curl "http://192.168.137.101:5001/wd" -d "age=18" -X PUT
    return "%s User is %s , and age is %s" % (request.method,username, age)
    
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5001)
