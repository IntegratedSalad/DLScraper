from web_app.scripts import get_soup, find_words, make_graph

def return_stats(band_name):
	soup = get_soup.make_soup_from_band_name(band_name.lower())
	if soup == 'invalid_band':
		return soup
	else:
		album_urls = find_words.get_albums(soup)
		album_lyrics = find_words.parse_albums(album_urls)
		if album_lyrics is not "albums_not_found":
			counted_words = find_words.return_word_count(album_lyrics)
			make_graph.save_graph(counted_words, band_name)
		else:
			return album_lyrics # albums_not_found
	
