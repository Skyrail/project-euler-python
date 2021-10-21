#
# Project Euler - Problem 29
# Copyright Aled Parry. All rights reserved.
#

"""
Thank goodness for Python sets keeping things unique. Not much to say about this
one really - other than I'm thankful for the simple ones!
"""

results = set()
for a in range(2,101):
    for b in range(2,101):
        results.add(pow(a,b))

print(len(results))
