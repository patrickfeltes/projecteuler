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

def nth_triangular(n):
    return n * (n + 1) / 2

# gives a list of tuples of the for (p, n) where p^n is in the prime factorization
def prime_factorization(n):
    lst = []
    possible_factor = 2
    while possible_factor <= int(math.sqrt(n)):
        count = 0
        while n % possible_factor == 0:
            count += 1
            n /= possible_factor

        if count != 0:
            lst.append((possible_factor, count))

        possible_factor += 1
    
    if n != 1:
        lst.append((n, 1))
    return lst

# given a number n = p_1^a_1*p_2^a_2*...*p_n^a_n, then number of factors
# of that number is (a_1+1)*...*(a_n+1)
def number_of_factors(n):
    return prod(map(lambda x: x[1] + 1, prime_factorization(n)))

def prod(lst):
    prod = 1
    for item in lst:
        prod *= item
    return prod

def digit_sum(n):
    total = 0
    while n != 0:
        total += n % 10
        n /= 10
    return total

# return a list of length (n + 1) with booleans of true when a number at index i is prime
def sieve_of_eratosthenes(n):
    prime_lst = [True] * (n + 1)
    prime_lst[0] = False
    prime_lst[1] = False
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if prime_lst[i]:
            mult = 0
            square = i ** 2
            while square + mult * i <= n:
                prime_lst[square + mult * i] = False
                mult += 1
    return prime_lst

def first_n_primes(n):
    primes = []
    i = 2
    while True:
        if is_prime(i):
            primes.append(i)
        if len(primes) == n:
            break
        else:
            i += 1
    return primes

def get_n_primes_from_file(n):
    f = open('../textfiles/primes.txt')
    primes = map(int, (f.read().split(',')))[:n]
    f.close()
    return primes

def get_all_primes_from_file():
    f = open('../textfiles/primes.txt')
    primes = map(int, (f.read().split(',')))
    f.close()
    return primes