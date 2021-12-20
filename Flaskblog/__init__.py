from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SECRET_KEY'] = '8bee0a560054550f03c9d0eeed455e78'

# BD Location.
# Development Database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# ORM, SQLite in development, Postgress in production.
db = SQLAlchemy(app)

from Flaskblog import routes