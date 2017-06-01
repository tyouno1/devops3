from flask import Flask
from config import *
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # 以目录中存在的文件来判断是生产环境还是测试环境
    if os.path.exists('./online'):
        #app.config.from_object(ProductionConfig)
        app.config.from_object(config['pro'])
    elif os.path.exists('./test'):
        #app.config.from_object(DevelopmentConfig)
        app.config.from_object(config['dev'])
    else:
        app.config.from_object(config['default'])
    print app.config.get('SQLALCHEMY_DATABASE_URI')
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
