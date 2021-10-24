#
# Project Euler - Problem 37
# Copyright Aled Parry. All rights reserved.
#
from math import sqrt

"""
I misunderstood the original task but once I realised what it actually meant, well, here's the result.
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

for p in P:
    for i in range(1,len(p)):
        if p[i:] not in P or p[:len(p)-i] not in P:
            break
    else:
        if int(p) > 10:
            c.append(int(p))
    
print(sum(c))