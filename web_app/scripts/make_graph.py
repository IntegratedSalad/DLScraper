import matplotlib.pyplot as plt
# album_urls = get_albums(soup)
# album_lyrics = parse_albums(album_urls)

#counted_words = return_word_count(album_lyrics)
#counted_words = [('rising', 6), ('awake', 6), ('old', 5), ('running', 4), ('tears', 3), ('drop', 2), ('walls', 1), ('reunite,', 1), ('implode,', 1), ('explode,', 1)]

def show_graph(counted_words, results_num, band):
	names = [counted_words[x][0] for x in range(results_num)]
	values = [counted_words[x][1] for x in range(results_num)]

	plt.figure(figsize=(9, 3))
	plt.plot(values[0])
	plt.bar(names, values)
	plt.suptitle(f"Words of {band.title()}")
	plt.show()


# show_graph(counted_words, 10, "Gojira")
