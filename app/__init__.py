from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
app.config['SECRET_KEY'] = 'a really really really realy long secret key'

from app import routes, models

from flask_cors import CORS
cors = CORS(app)