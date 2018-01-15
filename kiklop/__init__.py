from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'cancan65'

toolbar = DebugToolbarExtension(app)
Bootstrap(app)

import kiklop.views