import redis

from utils.settings import SQLALCHEMY_DATABASE_URI


class Config:

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SECRET_KEY = 'secret_key'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='127.0.0.1',port='6379')
    SESSION_KEY_PREFIX = 'aj'
