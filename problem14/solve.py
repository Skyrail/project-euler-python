#
# Project Euler - Problem 14
# Copyright Aled Parry. All rights reserved.
#
"""
I'd done this one before, using C, in the 'dim and distant past' as Project Euler 
likes to put it. This is basically that re-created. I vaguely remember it being slow
in C - it's definitely slow in Python. Maybe I'll come back to it again and try and speed
it up at some point - like a lot of these, Python isn't really made for this sort of speed
but equally my algorithms aren't the best.
"""

chainMax, numMax = 0, 0

for num in range(1000000):
    n, chain = num, 0

    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        chain += 1

    if chain > chainMax:
        chainMax = chain
        numMax = num

print(numMax)