from math_functions import *
n = 1
while True:
    num_divisors = 0
    # since n and n + 1 are coprime, number_of_factors is multiplicative and we need integer inputs
    if n % 2 == 0:
        num_divisors = number_of_factors(n / 2) * number_of_factors(n + 1)
    else:
        num_divisors = number_of_factors(n) * number_of_factors((n + 1) / 2)
    if num_divisors > 500:
        print n * (n + 1) / 2
        break
    n += 1