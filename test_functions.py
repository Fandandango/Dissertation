import numpy as np
from scipy.optimize import curve_fit
import os

def my_root(x, root):
	return np.power(x, root)

def log_pow(x, param):
	return np.log(x) * np.power(x, param)

def n(x, param):
	a = x * param
	return np.sign(a) * (np.abs(a)) ** (0.35)

def my_rt(x, p1, p2, p3, p4):
	p4 = 1e-8 if p4 <= 0 else p4
	a = p2 + x * p3
	return p1 + np.sign(a) * (np.abs(a)) ** p4

def fancy_func(src):
	import csv
	amds = []
	with open(src) as f:
		reader = csv.reader(f)
		next(reader)
		for line in reader:
			amds.append([float(i) for i in line[3:]])
	amds = np.array(amds, dtype=np.float64)
	n = amds.shape[1]
	xs = np.linspace(1, n, n)
	xdata = np.array([xs for _ in range(amds.shape[0])])

	def optimize_consts(x_, a1):
		def f(x, p1, p2):
			a = p1 * x
			return p2 + np.sign(a) * (np.abs(a)) ** a1
		results = []
		for x, amd in zip(x_, amds):
			param_opt, _ = curve_fit(f, x, amd)
			results.append(f(x, *param_opt))
		print(a1)
		return np.array(results, dtype=np.float64)

	param_opt, _ = curve_fit(optimize_consts, xdata, amds, p0=[0.35])
	return param_opt

if __name__ == '__main__':
	filename = "T2L_Energy_Density_AMDs1000_CLEAN.csv"
	src = os.path.join("Data", filename)
	print(fancy_func(src))
