from flask import render_template, url_for, request, redirect
from web_app import app

@app.route("/", methods=["GET", "POST"])
@app.route("/home.html", methods=["GET", "POST"])
def home():
	return render_template('home.html')
