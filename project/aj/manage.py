from flask_script import Manager
from flask import render_template

from utils.app import create_app
from utils.config import Config

app = create_app(Config)
manage = Manager(app=app)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    manage.run()
