from flask import Flask 
import os

import font_download

app = Flask(__name__)

OUTPUT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static", "Augusta.ttf")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config["SECRET_KEY"] = '19e5561987aab208337f98c2804d486de931d2f484ec253fa349a18be14e8dcf'

if os.path.isfile(PATH_TO_FILE):
	print("Font is installed.")
else:
	print("Installing font...")
	download_augusta_font()
	

from web_app import routes
