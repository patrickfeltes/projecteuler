"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
number = 600851475143

def get_prime_factors(n):
    factors = []
    for div in xrange(2, int(math.sqrt(n)) + 1):
        while n % div == 0:
            factors.append(div)
            n /= div
    if n != 1:
        factors.append(n)

    return factors

print get_prime_factors(number)[-1]
