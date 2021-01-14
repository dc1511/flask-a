from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy #sql
from flask_migrate import Migrate #database migration
from flask_login import LoginManager #login services

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models