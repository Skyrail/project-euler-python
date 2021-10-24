#
# Project Euler - Problem 33
# Copyright Aled Parry. All rights reserved.
#
from math import prod
from fractions import Fraction

"""
I initially attempted to do this using a bunch of checks and if statements trying to weed out the values I wanted
but it turned out to be rather frustrating. So I slept on it and then found this paper (https://www.edb.gov.hk/attachment/tc/curriculum-development/kla/ma/res/sa/2018_19MPC(1st%20runner-up).pdf)
which gave a little equality that let me quickly figure it out. It makes a lot of sense now I see it!
"""


f = []

for x in range(1, 10):
    for z in range(1, 10):
        for y in range(1, 10):
            a = ((10 * x) + y) / ((10 * y) + z)
            b = x / z

            if 0 < a < 1 and a == b:
                f.append(Fraction(x,z))

print(f'{prod(f)}')