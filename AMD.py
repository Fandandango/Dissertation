import csv
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def fit_all(src, function):
	errors = []
	names = []
	with open(src) as f:
		reader = csv.reader(f)
		next(reader)
		for line in reader:
			names.append(line[0])
			y = [float(i) for i in line[3:]]
			n = len(y)
			xdata = np.linspace(1, n, n)
			ydata = np.array(y, dtype=np.float64)
			param_opt, _ = curve_fit(function, xdata, ydata)
			errors.append(np.sum(np.square(ydata - function(xdata, *param_opt))) / n)
	arg_min = np.argmin(errors)
	arg_max = np.argmax(errors)
	min_err = errors[arg_min]
	max_err = errors[arg_max]
	av_err  = sum(errors) / len(errors)
	min_max_dict = {names[arg_min] : min_err, names[arg_max] : max_err}
	return min_max_dict, av_err

def plot_all_actual_and_fitted(src, function):
	with open(src) as f:
		reader = csv.reader(f)
		next(reader)
		for line in reader:
			y = [float(i) for i in line[3:]]
			n = len(y)
			xdata = np.linspace(1, n, n)
			ydata = np.array(y, dtype=np.float64)
			param_opt, _ = curve_fit(function, xdata, ydata)
			plt.plot(ydata, label='actual')
			plt.plot(function(xdata, *param_opt), label='fitted')
			plt.legend()
			plt.show()
			plt.close()

def plot_actual_and_fitted(src, function, job_name):
	with open(src) as f:
		reader = csv.reader(f)
		next(reader)
		for line in reader:
			if line[0] == job_name:
				y = [float(i) for i in line[3:]]
				n = len(y)
				xdata = np.linspace(1, n, n)
				ydata = np.array(y, dtype=np.float64)
				param_opt, _ = curve_fit(function, xdata, ydata)
				plt.plot(ydata, label='actual')
				plt.plot(function(xdata, *param_opt), label='fitted')
				plt.legend()
				plt.show()
				plt.close()
				break

def plot_est_derivative(src, job_name):
	with open(src) as f:
		reader = csv.reader(f)
		next(reader)
		for line in reader:
			if line[0] == job_name:
				y = [float(i) for i in line[3:]]
				diffs = np.array(y[1:]) - np.array(y[:-1])
				plt.plot(diffs)
				print(diffs)
				plt.show()
				plt.close()
				break

if __name__ == '__main__':
	import test_funcs

	filename = "T2L_Energy_Density_AMDs1000_CLEAN.csv"
	# plot_actual_and_fitted(filename, test_funcs.log_base, "job_03168")
	print(fit_all(filename, test_funcs.n))
	# plot_est_derivative(filename, "job_07107")
