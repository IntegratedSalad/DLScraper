from bs4 import BeautifulSoup as bs
import requests

def make_soup(band_name):

	BAND_NAME_FORMATTED = BAND.replace(" ", "").lower()
	URL = f"http://www.darklyrics.com/{BAND_NAME_FORMATTED[0]}/{BAND_NAME_FORMATTED}.html"
	HTML = requests.get(URL).content
	soup = bs(HTML, 'html.parser')
	print(soup.prettify())


BAND = input('Type a band name: ')
make_soup(BAND)

