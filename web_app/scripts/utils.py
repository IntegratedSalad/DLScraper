
def timer(orig_func):
	import time

	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print('{0} ran in: {1} sec'.format(orig_func.__name__, t2))
		return result

	return wrapper
	