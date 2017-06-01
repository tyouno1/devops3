#coding:utf-8
from __future__ import unicode_literals

from flask import Flask, render_template, session, redirect, request
from . import app
import requests, json
import utils

headers={'content-type': 'application/json'}

# dashbord
@app.route('/')
def index():
    if session.get('author','nologin') == 'nologin':
        return redirect('/login')
    username = session.get('username')
    return render_template('index.html',user=username)


@app.route('/user/<htmlname>')
def user(htmlname):
    if session.get('author':'nologin') == 'nologin':
        return redirect('/login')
    utils.write_log('web').info('info')
    return render_template(htmlname + '.html' , user=session.get('username'))

@app.route('/project/<htmlname>')
def project(htmlname):
    if session.get('author':'nologin') == 'nologin':
        return redirect('/login')
    return render_template(htmlname + '.html' , user=session.get('username'))

@app.errhandler(404)
def not_found(e):
    return render_template('404.html')

@app.errhandler(500)
def internal_server_error(e):
    return render_template('500.html')
