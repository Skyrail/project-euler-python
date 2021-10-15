#
# Project Euler - Problem 4
# Copyright Aled Parry. All rights reserved.
#
"""
Didn't look at the C code this time - but Python will have made it much easier anyway
with range and a quick and easy way of reversing strings. Cracking stuff.
"""

pmax = 0
for i in range(100,1000):
    for j in range(100, 1000):
        p = i*j
        if str(p) == str(p)[::-1]: pmax = max(p,pmax)

print(pmax)