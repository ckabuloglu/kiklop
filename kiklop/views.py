from flask import Flask, render_template

from kiklop import app

@app.route('/')
def index():
    return render_template('login.html')
     