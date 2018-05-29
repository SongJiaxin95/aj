from flask import session,redirect
from flask_sqlalchemy import SQLAlchemy
from  flask_debugtoolbar import DebugToolbarExtension
import functools


db = SQLAlchemy()
# debugtoolbar = DebugToolbarExtension()


def init_ext(app):

    db.init_app(app=app)
    # debugtoolbar.init_app(app=app)


def get_database_uri(DATABASE):

    user = DATABASE.get('USER')
    password = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    port = DATABASE.get('PORT')
    name = DATABASE.get('NAME')
    db = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver, user, password, host, port, name)

def is_login(view_fun):
    @functools.wraps(view_fun)
    def decorator():
        try:
            # 验证用户是否登录
            if 'user_id' in session:
                return view_fun()
            else:
                return redirect('/user/login/')
        except:
            return  redirect('/user/login/')
    return decorator