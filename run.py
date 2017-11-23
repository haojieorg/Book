from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from admin import admin_blueprint

#创建app 实例
app = Flask(__name__)
app.debug = True #打开调试
app.secret_key = 'haojieorg' #增加安全码

#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


@app.route('/')
def index():
    return '欢迎使用Flask'

app.register_blueprint(admin_blueprint,url_prefix='/admin')

if __name__ == '__main__':
    app.run()