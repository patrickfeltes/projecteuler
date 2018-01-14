from math_functions import lcm

# follows a cycle

def find_max_r(a):
	max_val = 2
	n = 1
	possible = set()
	while True:
		val = (n * 2 * a) % (a ** 2)

		if val in possible:
			break
		else:
			max_val = max(max_val, val)
			possible.add(val)


		n += 2
	return max_val

total = 0
for x in xrange(3, 1001):
	total += find_max_r(x)

print total