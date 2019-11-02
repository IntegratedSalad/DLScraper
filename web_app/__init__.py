from werkzeug.utils import secure_filename
from flask import Flask 

app = Flask(__name__)

app.config["SECRET_KEY"] = '19e5561987aab208337f98c2804d486de931d2f484ec253fa349a18be14e8dcf'

from web_app import routes
