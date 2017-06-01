from flask import Flask
import os

app = Flask(__name__)
app.config.from_pyfile('config2.py')

@app.route('/')
def hello_world():
    print app.config.get('HOST'), app.config.get('PORT')
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
