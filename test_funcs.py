import numpy as np

def my_root(x, root):
	return np.power(x, root)

def log_pow(x, param):
	return np.log(x) * np.power(x, param)

def n(x, param):
	x[x == 0] = 1e-8
	x[np.log(x) == 0] = 1e-8
	return np.log(np.log(param * x))

def my_rt(x, param):
	return np.power(param * x, 1/3)
