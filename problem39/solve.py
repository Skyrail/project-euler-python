#
# Project Euler - Problem 39
# Copyright Aled Parry. All rights reserved.
#
import collections
from math import sqrt

"""
This one's a messy result. I was distracted while solving it (Critical Role Season 3!) - to begin
with I over-complicated it, trying to generate triples beforehand before realising I could just loop
over it like I have here. It could be much neater but again, distracted!
"""

triples = collections.defaultdict(list)

for i in range(1,500):
    for j in range(1,500):
        k = sqrt(pow(i,2) + pow(j,2))
        if k.is_integer() and int(i+j+k) <= 1000:
            triples[int(i+j+k)].append((i,j,int(k)))

maximised = []
for s,t in triples.items():
    if len(t) > len(maximised):
        maximised = t
        print(s, len(t), t)