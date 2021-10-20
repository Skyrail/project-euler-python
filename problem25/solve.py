#
# Project Euler - Problem 25
# Copyright Aled Parry. All rights reserved.
#
from math import log10

"""
I'll admit I sort of got some help with this one. I knew that brute forcing
Fib numbers up to that scale would take far too long so I searched about for 
faster methods and this one felt the most 'right' and had a time complexity of O(logN)
(I'm not sure if my particular implementation of it is but it's fast enough)
"""

nums = [0 for x in range(10000)]

def F(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        nums[n] = 1
        return nums[n]
    elif nums[n]:
        return nums[n]
    elif n % 2 == 0:
        k = int(n / 2)
        nums[n] = (2 * F(k - 1) + F(k)) * F(k)
        return nums[n]
    else:
        k = int((n + 1)/2)
        nums[n] = pow(F(k), 2) + pow(F(k-1), 2)
        return nums[n]

ans = n = 1
while int(log10(ans)) + 1 < 1000:
    n += 1
    ans = F(n)
     
print(n)