import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
import test_funcs

def plot_actual_and_fitted(y, function):
	n = len(y)
	x = np.linspace(1, n, n)
	ydata = np.array(y, dtype=np.float64)
	param_opt, param_cov = curve_fit(function, x, ydata)
	print(param_cov)
	print(np.sum(np.square(ydata - function(x, *param_opt))) / n)
	plt.plot(ydata, label='actual')
	plt.plot(function(x, *param_opt), label='fitted')
	plt.legend()
	plt.show()


def all_errors_plot(filename):
	names  = []
	params = []
	errors = []
	with open(filename) as source:
		reader = csv.reader(source)
		next(reader)
		for line in reader:
			names.append(line[0])
			params.append(float(line[1]))
			errors.append(float(line[2]))
	params = np.array(params)
	errors = np.array(errors)
	print("Average error:", np.average(errors))
	least = np.argmin(errors)
	most  = np.argmax(errors)
	print("Least error:", errors[least], "at", names[least])
	print("Most error:", errors[most], "at", names[most])
	print("Average param:", np.average(params))
	sns.distplot(errors)
	plt.show()
	sns.distplot(params)
	plt.show()
	a = np.argsort(errors)[-10:]
	print("worst jobs:")
	for ind in a:
		print(names[ind])



if __name__ == '__main__':
	# all_errors_plot("log_pow.csv")

	filename = "T2L_Energy_Density_AMDs1000_CLEAN.csv"
	job_name = "job_04441"
	with open(filename) as src:
		reader = csv.reader(src)
		for line in reader:
			if line[0] == job_name:
				y = [float(i) for i in line[3:]]
				break
	plot_actual_and_fitted(y, test_funcs.log_pow_)

