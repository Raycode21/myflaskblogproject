from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SECRET_KEY'] = '2d5ca6681f533eeb43d8c4d92e3a9b87'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from myflaskapp import routes