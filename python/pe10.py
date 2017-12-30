from math_functions import sieve_of_eratosthenes
from math_functions import is_prime
import time
# can be sped up with sieve of eratosthenes
start1 = time.time()
total = 0
for x in xrange(2, 2*10**6 + 1):
    if is_prime(x):
        total += x
print total

print time.time() - start1

start2 = time.time()

lst = sieve_of_eratosthenes(2 * 10 ** 6)
total = 0
for i in xrange(len(lst)):
	if lst[i]:
		total += i

print total

print time.time() - start2