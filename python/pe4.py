"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(prod):
    return str(prod) == str(prod)[::-1]

max_palindrome_prod = 0
for num1 in xrange(100, 1000):
    for num2 in xrange(100, 1000):
        prod = num1 * num2
        if is_palindrome(prod) and prod > max_palindrome_prod:
            max_palindrome_prod = prod
print max_palindrome_prod
