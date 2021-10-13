#
# Project Euler - Problem 9
# Copyright Aled Parry. All rights reserved.
#

"""
This was my initial attempt at the task. It's slow, and not very elegant.
It is a very naive brute force, but does get the answer, eventually
"""
def bruteForceTriple(r):
    for a in range(r):
        for b in range(r):
            for c in range(r):
                if a+b+c != r: continue
                if pow(a,2) + pow(b,2) != pow(c,2): continue
                if a*b*c != 0: return a*b*c

print(bruteForceTriple(1000))