#
# Project Euler - Problem 15
# Copyright Aled Parry. All rights reserved.
#
from math import factorial as f

"""
A little bit of search brought up the binomial coefficient. I'll be honest, I don't know much about it yet,
but I have a feeling that it's going to come in handy in future Euler problems. So one for the memory bank
even if the code is really simple this time around.
"""

def binomial(n, k):
    return f(n + k) / (f((k+n) - n) * f(n))

print(int(binomial(4,2)))