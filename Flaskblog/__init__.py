from flask import Flask
# Object Relational mapping
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/
from flask_sqlalchemy import SQLAlchemy
# Handle hashing for application
# https://flask-bcrypt.readthedocs.io/en/latest/
from flask_bcrypt import Bcrypt
# Handle user login session
# https://flask-login.readthedocs.io/en/latest/
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '8bee0a560054550f03c9d0eeed455e78'

# BD Location.
# Development Database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# ORM, SQLite in development, Postgress in production.
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# login is rount name in routes.py
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Flaskblog import routes