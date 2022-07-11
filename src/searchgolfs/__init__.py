from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

DEV_MODE = os.environ.get("GOLF_DEV_MODE")

if DEV_MODE == 'True':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///searchgolf'
    app.config['SECRET_KEY'] = os.environ.get("GOLF_SECRET_KEY")

elif DEV_MODE == 'False':
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'GOLF_SQLALCHEMY_DATABASE_URI'
    app.config['SECRET_KEY'] = os.environ.get("GOLF_SECRET_KEY")

db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcyrpt = Bcrypt(app)
login_manager = LoginManager(app)

from searchgolfs import routes
