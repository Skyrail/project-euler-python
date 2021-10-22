#
# Project Euler - Problem 31
# Copyright Aled Parry. All rights reserved.
#
"""
I couldn't wrap my head around how to brute force this one nicely so I did some research.
Dynamic programming, again. I'm seeing a trend - it's something I'm going to have to get used
to spotting. This one I had to see someone else's method and explanation to then understand
how it works.
"""
values, target = [1,2,5,10,20,50,100,200], 201
ways = [1] + [0 for x in range(target)]

for c in values:
    j = c
    for j in range(j, target):
        ways[j] += ways[j - c]

print(max(ways))