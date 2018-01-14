import numpy as np

# function to generate from
def generating(n):
	total = 0
	for x in xrange(0, 11):
		total += (-1)**x * (n ** x)
	return total

# L = len(values)
# will find a polynomial of order (L - 1) that fits at least the first L values
def poly_fit(values):
	coeff_mat = []
	for x in xrange(1, len(values) + 1):
		coeff_row = []
		for i in xrange(len(values)):
			coeff_row.append(x ** (len(values) - i - 1))
		coeff_mat.append(coeff_row)

	# convert to proper datatype for linalg library
	coeff_mat = np.array(coeff_mat)
	solution_mat = np.array(values)

	# coefficient list for resulting polynomial
	return map(lambda x : int(round(x)), list(np.linalg.solve(coeff_mat, solution_mat)))

# given a list of coefficients for a polynomial and a point, evaluate
def evaluate(coeff_list, x):
	total = 0
	for i in xrange(len(coeff_list)):
		total += coeff_list[i] * x ** (len(coeff_list) - i - 1)
	return total

def fit(values, num_given):
	coeff_list = poly_fit(values[:num_given])
	for x in xrange(len(values)):
		if values[x] != evaluate(coeff_list, x + 1):
			return evaluate(coeff_list, x + 1)

	return 'fit all values in the values list'

precomupted_values = []
for x in xrange(1, 300):
	precomupted_values.append(generating(x))

total = 0
for num_given in xrange(1, 11):
	total += fit(precomupted_values, num_given)
print total