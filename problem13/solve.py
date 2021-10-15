#
# Project Euler - Problem 13
# Copyright Aled Parry. All rights reserved.
#
from math import floor

"""
I'm actually really happy with how this one turned out. It's a compact bit of code
and it's quick. I thought about how to finish this one while eating tea - was nice
to get in front of the computer and actually put it into practice.
"""

input,rem = open('input', 'r').read().split('\n'), 0

for i in range(49,10,-1):
    rem = floor(sum([int(num[i]) for num in input], rem)/10)

print(str(sum([int(x[:10]) for x in input], rem))[:10])