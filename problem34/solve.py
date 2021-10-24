#
# Project Euler - Problem 34
# Copyright Aled Parry. All rights reserved.
#
from math import factorial

"""
This is another one that I didn't know the upperbound for so I just continued to increase it until it seemed like 
there were no more. After finding the result I dropped the upperbound here so it just runs quickly.
"""

f = []

for num in range(3,100000):
    facSum = sum([factorial(int(x)) for x in str(num)])
    if facSum == num:
        f.append(facSum)

print(sum(f))