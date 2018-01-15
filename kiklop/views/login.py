from flask import Blueprint, render_template
# from kiklop import app

login = Blueprint('login', __name__)

@login.route('/')
def index():
    print 'LOGIN PAGE'
    return render_template('login/index.html')

@login.route('/forgot')
def forgot():
    print 'FORGOT PASSWORD'
    return render_template('login/forgot.html')
     