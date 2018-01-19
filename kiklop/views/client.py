from flask import Blueprint, render_template, redirect, request, url_for

client = Blueprint('client', __name__)

@client.route('/client', methods=["GET", "POST"])
def get_client_list():
    return render_template('client/client_list.html')

@client.route('/add_client', methods=["GET", "POST"])
def add_client():
    return render_template('client/add_client.html')