#
# Project Euler - Problem 12
# Copyright Aled Parry. All rights reserved.
#
from math import sqrt

"""
This one took me a while to read up on but once I found the triangle numbers function and understood what divisors 
was doing I could calculate the answer in no time. Sort of. The execution time is pretty slugish because it checks
each triangle number individually. There may be a smarter way which I need to find.
"""

def triangleNumber(n):
    return (n*(n+1))/2

def divisors(n):
    i,count = 1,0
    while i <= sqrt(n):
        if n % i == 0:
            if n/i != i:
                count += 1
            count += 1

        i += 1
    return count

i,n = 1, triangleNumber(1)

while divisors(n) < 500:
    n = triangleNumber(i)
    i += 1

print(n, divisors(n))