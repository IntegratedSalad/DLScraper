from web_app.scripts.get_soup import make_soup_from_band_name, make_soup_from_album_url
from time import sleep
from web_app.scripts import make_graph

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
	   Returns list with n strings, where n is the number of band's albums."""

	lyrics = []

	for album_url in albums_list:
		if not "google" in album_url:

			album_soup = make_soup_from_album_url(album_url)

			if album_soup is not None:

				lyrics_ = album_soup.find_all("div", "lyrics")
				for lyr in lyrics_:
					to_remove = lyr.find_all(["h3", "br", "div", "a", "i"])
					for element in to_remove:
						element.decompose() # evil method

					lyrics.append(str(lyr))
			else:

				raise TypeError("Album soup appears to be empty.")
		else:		
				
			return "albums_not_found"

	return lyrics

def return_word_count(album_lyrics):
	ignore_list = ["the", "my", "to", "from", "this", "i", "you", "and", "for", "with", "your", "a", "an", "or", \
	"out", "in", "as", "of", "on", "will", "into", "onto", "them", "off", "are", "is", "it", "every", "have", "no", "yes", "by", "it's", \
	"their", "me", "now", "you'll", "i'll", "will", "but", "can", "we", "us", "our", "not", "could", "would", "am", "don't", "be", "has",\
	"never", "ever", "sometimes", "like", "i'm", "-", "at", "own", "all", "so", "that", "what"]

	occurences_dict = dict()

	for lyric in album_lyrics:
		words = lyric.split()

		for word in words:
			if word.lower() not in ignore_list:
				if word.lower() in occurences_dict:
					occurences_dict[word.lower()] += 1
				else:
					occurences_dict[word.lower()] = 1

	sorted_list = sorted(occurences_dict.items(), key=lambda k: k[1])
	return list(reversed(sorted_list))
