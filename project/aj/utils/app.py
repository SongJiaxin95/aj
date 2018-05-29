from flask import Flask

from App.house_views import house
from App.order_views import order
from utils.settings import TEMPLATES_DIR,STATIC_DIR
from utils.functions import init_ext
from App.user_views import user

def create_app(config):
    app = Flask(__name__,template_folder=TEMPLATES_DIR,static_folder=STATIC_DIR)

    # app.debug = True

    app.register_blueprint(blueprint=user,url_prefix='/user')
    app.register_blueprint(blueprint=house,url_prefix='/house')
    app.register_blueprint(blueprint=order,url_prefix='/order')

    # app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object(config)

    init_ext(app)

    return app