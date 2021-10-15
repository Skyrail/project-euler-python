#
# Project Euler - Problem 11
# Copyright Aled Parry. All rights reserved.
#
from operator import mul
from functools import reduce

"""
I'll admit, it's not the most elegant solution - but it's fairly quick (compared to others I've brute forced)
It could probably be made more efficient by not calculating the products of those arrays shorter than 4
(for example, at the edges of the matricies) but the time addition is so negligible compared to how simple
the code is I thought it worthwhile to just catch IndexErrors and crack on.
"""

input = open('input', 'r').read().split('\n')

input = [l.split() for l in input]

m = 0

for r in range(len(input)):
    for c in range(len(input[r])):
        try: 
            horz = set(int(h) for h in input[r][c:c+4])
            vert = set(int(row[c]) for row in input[r:r+4])
            diag = set(int(input[r+i][c+i]) for i in range(4))
            adiag = set(int(input[r+i][c-i]) for i in range(4))

            for x in [horz, vert, diag, adiag]:
                m = max(m, reduce(mul, x, 1))

        except IndexError:
            pass
    
print(m)