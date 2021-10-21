#
# Project Euler - Problem 27
# Copyright Aled Parry. All rights reserved.
#
from math import sqrt

"""
This gets the answer but it is horrendously slow, and I've no idea how to improve its speed
Generating the list of prime numbers reduces the need to recalculate continuously but I'm not sure
how else to improve the efficiency. I'll check out other's answers and maybe in the future I'll be
able to return and improve it.
"""

"""
Returns a list of prime numbers using the Sieve of Eratosthenes
"""
def primes(n: int) -> list:
    A = {p: True for p in range(2, n+1)}

    for i in range(2, int(sqrt(n))):
        if A[i]:
            j, k = 0, 0
            while j < n:
                j = pow(i, 2)+k*i
                A[j] = False
                k += 1
    
    return [k for k, v in A.items() if v]

P = primes(100000)

def f(n,a,b):
    return pow(abs(n),2) + a * abs(n) + b

def countPrimes(a, b):
    n = 0
    while True:
        if f(n,a,b) not in P: 
            return n
        else:
            n += 1

amax = bmax = cmax = 0

for a in range(-999,1001):
    for b in range(2,1001):
        c = countPrimes(a, b)

        if c > cmax:
            print(c,a,b)
            cmax = c
            amax = a
            bmax = b

print(amax*bmax)