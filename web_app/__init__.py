from flask import Flask 
import os

app = Flask(__name__)

OUTPUT_FOLDER = os.path.join(app.instance_path, 'htmlfo')

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
app.config["SECRET_KEY"] = '19e5561987aab208337f98c2804d486de931d2f484ec253fa349a18be14e8dcf'

from web_app import routes
