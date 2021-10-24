#
# Project Euler - Problem 32
# Copyright Aled Parry. All rights reserved.
#
from itertools import permutations

"""
This one was a fun one to figure out - starting off with 1234 and moving upwards
just to make sure I'd got the logic okay
"""

products = set()

for num in permutations('123456789'):
    for i in range(1,len(num)-1):
        for j in range(i):
            m = num[:i+1]
            r = int(''.join(num[i+1:]))
            a = int(''.join(m[:j+1]))
            b = int(''.join(m[j+1:]))

            if a*b == r:
                products.add(r)
                print(f'{a} x {b} = {r}')

print(f'Sum is {sum(products)}')
