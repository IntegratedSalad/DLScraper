from bs4 import BeautifulSoup as bs
import requests

headers = {"User-Agent": 'Mozilla/5.0 (WINDOWS NT 6.1; Win64; x64; rv:47.0)'}

def make_soup_from_band_name(band_name):

	BAND_NAME_FORMATTED = band_name.replace(" ", "").lower()
	URL = f"http://www.darklyrics.com/{BAND_NAME_FORMATTED[0]}/{BAND_NAME_FORMATTED}.html"
	HTML = requests.get(URL, headers=headers).content

	soup = bs(HTML, 'html.parser')

	if soup.title.contents[0][-14:].lower() == "page not found":
		#return "not_found"
		print(f"{band_name} was not found.")
		return 'invalid_band'

	return soup

def make_soup_from_album_url(album_url):

	URL = f"http://www.darklyrics.com{album_url}"
	HTML = requests.get(URL, headers=headers).content
	soup = bs(HTML, 'html.parser')

	# TODO: EXCEPTIONS

	return soup
