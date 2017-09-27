"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math_functions import lcm

num = 1
for x in xrange(1, 21):
    num = lcm(num, x)
print num
