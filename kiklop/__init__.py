from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from .views.login import login

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

app.register_blueprint(login)

bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

# For circular dependencies
import kiklop.views