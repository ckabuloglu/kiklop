from flask import Blueprint, render_template, redirect, request, url_for

home = Blueprint('home', __name__)

@home.route('/home', methods=["GET", "POST"])
def homepage():
    return render_template('home/home.html')