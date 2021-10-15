#
# Project Euler - Problem 5
# Copyright Aled Parry. All rights reserved.
#

"""
It's faster than my original C implementation (shock horror) - because in that version I looped through
all of the numbers, checking against all of the posible divisors. This, however, checks a subset of each.
By starting at 20, and knowing that it must be divisible by 20, we can increase in jumps of 20
Secondly, the subset of divisors we check has been determined that if the number can be divided by the
larger numbers then any of their factors will also go into it.
"""

def is_divisible(n):
    for i in [11,12,13,14,15,16,17,18,19,20]:
        if n % i != 0 : return False
    return True

n = 20
while not is_divisible(n):
    n += 20

print(n)