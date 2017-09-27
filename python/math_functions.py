import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    if n == 2:
        return True

    for x in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 2
    while count != n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1
