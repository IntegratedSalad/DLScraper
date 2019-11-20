import matplotlib
matplotlib.use('Agg')

import os
from web_app import OUTPUT_FOLDER

def save_graph(counted_words, band, results_num=10):
	from matplotlib import pyplot as plt
	names = [counted_words[x][0] for x in range(results_num)]
	values = [counted_words[x][1] for x in range(results_num)]

	plt.style.use('seaborn-dark')
	plt.figure(figsize=(9, 3))
	plt.plot(values[0])
	plt.bar(names, values)
	plt.suptitle(f"Words of {band.title()}")
	# plt.show()
	plt.savefig(os.path.join(OUTPUT_FOLDER, 'plot.png'), bbox_inches='tight')
