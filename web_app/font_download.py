import requests
import os
from zipfile import ZipFile

PATH = os.path.dirname(os.path.realpath(__file__))
dirs = [PATH, "web_app", "static"]

LINK = "https://dl.dafont.com/dl/?f=augusta"

def download_augusta_font():

	"""Downloads 'Augusta' font from dafont.com, and places it in static folder."""

	request = requests.get(LINK, allow_redirects=True)
	with open(os.path.join(PATH, "archive.zip"), 'wb') as file:
		file.write(request.content)

	with ZipFile('archive.zip', 'r') as zip_file:
		zip_file.extractall(path=os.path.join(*dirs))


if __name__ == '__main__':
	download_augusta_font()
