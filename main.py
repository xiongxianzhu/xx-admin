# coding: utf-8

import sys
from flask import Flask
from flask_admin import Admin, BaseView, expose
from flask_babelex import Babel
from models import *

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
babel = Babel(app)

admin = Admin(app, name='后台管理系统', template_mode='bootstrap3')
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'        # zh_CN, 默认en
admin.add_view(UserView(User, db.session, name='信息', category='用户'))

app.run()