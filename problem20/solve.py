#
# Project Euler - Problem 20
# Copyright Aled Parry. All rights reserved.
#
from functools import reduce

""""
This is both super succicnt and also terrible. Don't do this in production code.
By all means use all the neat little features of Python but don't make your code
difficult to decipher for the sake of line count. It gets the answer though so yey.
"""

print(sum([int(a) for a in str(reduce(lambda x,y: x * y, [x for x in range(1,101)]))]))