from math_functions import is_prime
# can be sped up with sieve of eratosthenes
total = 0
for x in xrange(2, 2*10**6 + 1):
    if is_prime(x):
        total += x
print total