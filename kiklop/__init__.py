from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_bcrypt import Bcrypt
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_sqlalchemy import SQLAlchemy

from .views.login import login
from .views.home import home
from .views.client import client

# Initiate the Flask app with config
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Blueprints
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(client)

# Extensions
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)

# Navbar
nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'Kiklop ',
        View('Home', 'home.homepage'),
        View('Client', 'client.get_client_list'),
    )

nav.init_app(app)

# For circular dependencies
import kiklop.views