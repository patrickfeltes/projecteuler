from math_functions import *
import Queue

primes = get_all_primes_from_file()

powers = [1]

pri = Queue.PriorityQueue()
pri.put((4, 0))

def convert_to_number(powers):
	num = 1
	for i in xrange(len(powers)):
		num *= primes[i] ** powers[i]
		num %= 500500507
	return num

n = 500500
for x in xrange(n - 1):
	min_val = primes[len(powers)]
	min_index = len(powers)

	poss = pri.get()
	if poss[0] < min_val:
		min_val = poss[0]
		min_index = poss[1]
	else:
		pri.put(poss)

	if min_index == len(powers):
		powers.append(1)
	else:
		powers[min_index] += powers[min_index] + 1

	pri.put((primes[min_index] ** (powers[min_index] + 1), min_index))

print "converting"
print convert_to_number(powers)