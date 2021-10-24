#
# Project Euler - Problem 35
# Copyright Aled Parry. All rights reserved.
#
from math import sqrt

"""
This one was really slow. Until I switched to a set - because set lookups are O(1) vs list lookups which are O(n)
Worth knowing for the future, I originally switched to a dict to try and improve efficiency by marking true those
that had already been checked but the speed increase was noticable from just switching to checking against the keys
- because key lookups in dicts are also O(1). Instead of pushing further I just switched to sets and here we have it
"""

def primes(n):
    A = {p: True for p in range(2, n+1)}

    for i in range(2, int(sqrt(n))):
        if A[i]:
            j, k = 0, 0
            while j < n:
                j = pow(i, 2)+k*i
                A[j] = False
                k += 1

    return [k for k, v in A.items() if v]

P,c = set(str(x) for x in primes(1000000)),[]

for k in P:
    cp = []
    for x in range(len(k)):
        k = k[1:] + k[0]
        if k not in P:
            break
        elif k in P:
            cp.append(k)
    else:
        c.append(cp)
    
print(len(c))