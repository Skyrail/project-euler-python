#
# Project Euler - Problem 30
# Copyright Aled Parry. All rights reserved.
#
"""
This one was easy in theory, the difficult bit was knowing the upper bound.
I just tested increasingly higher upper bounds until the sum didn't change. Not smart.
I've seen in other places there's a smart way of thinking about it.
"""

total = 0
for num in range(2,1000000):
    t = sum([pow(int(x),5) for x in str(num)])
    if t == num:
        total += num

print(total)