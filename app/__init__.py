from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models