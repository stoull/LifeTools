import time

def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f"{fn.__name__} has spent {t2 - t1}s")
		return result
	return wrapper


