#
# Project Euler - Problem 21
# Copyright Aled Parry. All rights reserved.
#
from math import sqrt

"""
Another not so quick one that would probably benefit from some efficiency improvements
but I'm going to sleep now so it can wait. In the mean time it's solved the problem so
will have to do. Goodnight!
"""

def divisors(n):
    i,divs = 1,[]
    while i <= n/2:
        if n % i == 0:
            divs.append(i)
        i += 1
    return divs

def d(n):
    return sum(divisors(n))

nums = set()
for i in range(2,10001):
    di = d(i)

    if i == d(di) and i != di:
        nums.update([i, di])

print(sum(nums))