#
# Project Euler - Problem 6
# Copyright Aled Parry. All rights reserved.
#
from functools import reduce

"""
Quick and easy, does the job in a couple of lines - thanks Python!
"""

sumOfSquares = reduce(lambda x,y: x+y, map(lambda x: pow(x,2), range(1,101)))
squareOfSum = pow(sum(range(1,101)),2)

print(squareOfSum - sumOfSquares)