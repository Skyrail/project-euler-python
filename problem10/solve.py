#
# Project Euler - Problem 10
# Copyright Aled Parry. All rights reserved.
#
from math import sqrt

"""
This implements the sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
It's not the fastest but it's a whole lot faster then trying to brute force it (I did start doing
that this time but it's far too slow.)

Other algorithms are a little over my head at the moment.
"""
n = 2000000

A = {p: True for p in range(2, n+1)}

for i in range(2, int(sqrt(n))):
    if A[i]:
        j, k = 0, 0
        while True:
            j = pow(i, 2)+k*i
            A[j] = False
            k += 1
            if j > n:
                break

print(sum(set(k for k, v in A.items() if v)))
