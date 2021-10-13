#
# Project Euler - Problem 8
# Copyright Aled Parry. Al rights reserved.
#
from functools import reduce

maximum, chunkSize = 0, 13
input = open('input', 'r').read().replace('\n', '')

for i in range(len(input) - chunkSize + 1):
    maximum = max(maximum, reduce((lambda x, y: int(x) * int(y)),
                                  list(input[i:i+chunkSize])))

print(maximum)