import os

from utils.functions import get_database_uri

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')

DATABASE = {
    # 用户名
    'USER':'root',
    # 密码
    'PASSWORD':'root',
    # 地址
    'HOST':'localhost',
    # 端口
    'PORT':'3306',
    # 数据库
    'DB':'mysql',
    # 驱动
    'DRIVER':'pymysql',
    # 数据库名称
    'NAME':'aj'
}

SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

UPLOAD_DIRS = os.path.join(os.path.join(BASE_DIR,'static'),'upload')
