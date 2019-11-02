from bs4 import BeautifulSoup as bs
import requests

def make_soup_from_band_name(band_name):

	BAND_NAME_FORMATTED = band_name.replace(" ", "").lower()
	URL = f"http://www.darklyrics.com/{BAND_NAME_FORMATTED[0]}/{BAND_NAME_FORMATTED}.html"
	HTML = requests.get(URL).content
	soup = bs(HTML, 'html.parser')

	return soup

def make_soup_from_album_url(album_url):

	URL = f"http://www.darklyrics.com{album_url}"
	HTML = requests.get(URL).content
	soup = bs(HTML, 'html.parser')

	return soup
