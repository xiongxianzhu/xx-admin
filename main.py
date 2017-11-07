# coding: utf-8

import sys
from flask import Flask
from flask_admin import Admin, BaseView, expose

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

admin = Admin(app, name='后台管理系统')

app.run()