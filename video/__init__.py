from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__, static_path="/static/")
app.config.from_object("video.config")
db = SQLAlchemy(app)

from . import views, models
