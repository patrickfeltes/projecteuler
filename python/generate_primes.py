from math_functions import sieve_of_eratosthenes

lst = sieve_of_eratosthenes(10**7)
primes = []
for x in xrange(len(lst)):
	if lst[x]:
		primes.append(x)

f = open('../textfiles/primes.txt', 'w')

f.write(str(primes)[1:-1])

f.close()