from bs4 import BeautifulSoup as bs
from get_soup import make_soup_from_band_name, make_soup_from_album_url
from time import sleep

#band = input("Type a band name: ")
soup = make_soup_from_band_name("gorgasm")

def get_albums(soup):

	"""Gets album's urls."""

	album_links = []
	albums_divs = soup.find_all("div", "album")


	for tag in albums_divs:
		a = tag.a
		album_links.append(a['href'][2:]) # every href starts with "..", so we cut it out.

	return album_links

def parse_albums(albums_list):

	"""Gets lyrics as a concatenated string of every song on album. 
	   Returns n strings, where n is a number of band's albums."""

	lyrics = []

	for album_url in albums_list:

		album_soup = make_soup_from_album_url(album_url)

		lyrics_ = album_soup.find_all("div", "lyrics")
		for lyr in lyrics_:
			to_remove = lyr.find_all(["h3", "br", "div", "a"])
			for element in to_remove:
				element.decompose()

			lyrics.append(str(lyr))

	return lyrics

album_urls = get_albums(soup)
album_lyrics = parse_albums(album_urls)

print(len(album_lyrics))
