from flask import Blueprint, render_template, redirect, request, url_for
from ..forms.login_forms import ForgotForm, LoginForm

login = Blueprint('login', __name__)

@login.route('/', methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        print "POST"
        email = form.email
        password = form.password
        return redirect(url_for('login.index'))
    print "rendering main page"
    return render_template('login/index.html', form=form)

@login.route('/forgot', methods=["GET", "POST"])
def forgot():
    form = ForgotForm()
    if form.validate_on_submit():
        email = form.email
    print 'rendering forgot page'
    return render_template('login/forgot.html', form=form)
