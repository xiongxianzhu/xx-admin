# coding: utf-8

from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask import url_for

class UserView(ModelView):

    # 这三个变量定义管理员是否可以增删改，默认为True
    can_delete = False
    can_edit = False
    can_create = False

    # 这里是为了自定义显示的column名字
    column_labels = dict(
        username='用户名',
    )

    # 如果不想显示某些字段，可以重载这个变量
    column_exclude_list = (
        'password_hash',
    )