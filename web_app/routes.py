from flask import render_template, url_for, request, redirect
from web_app import app
from web_app import get_stats

@app.route("/", methods=["GET", "POST"])
@app.route("/home.html", methods=["GET", "POST"])
def home():

	invalid_band = False

	if request.method == "POST":
		band_name = request.form['band']
		if get_stats.return_stats(band_name) == "albums_not_found":
			print("Albums not found")
		elif get_stats.return_stats(band_name) == "invalid_band":
			invalid_band = True
		else:
			return redirect("result.html")

	return render_template('home.html', invalid=invalid_band)

@app.route("/result.html", methods=["GET", "POST"])
def results():
	return render_template("result.html")
	