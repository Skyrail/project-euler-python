#
# Project Euler - Problem 24
# Copyright Aled Parry. All rights reserved.
#
from itertools import permutations

"""
Is this cheating? Maybe it's cheating. It's a built in lib though.
Is it the most efficient? Maybe not - the other way is to convert the
permutations into a list and just get it by index - but that's not very
memory efficient. As if that matters. Either way, if I choose to do the task
in another language I may need to write it myself as it won't have a built in lib.
"""

for x in enumerate(permutations(range(10))):
    i,num = x
    if i == (int(1e6) - 1):
        print(''.join([str(num) for num in num]))
        break