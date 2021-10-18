#
# Project Euler - Problem 22
# Copyright Aled Parry. All rights reserved.
#

"""
This one took a little time to get the right answer (due to bugs) that were difficult to identify whether the new answer was correct
or not (as it was so ambiguously large) Either way, it works now. I feel a little lazy using the built in sort but that's not for now
"""

def chrVal(chr):
    # In this character set A == 65
    return ord(chr) - 64

# Easiest/Quickest way to sort - I'd like to implement some sorting algorithms manually though
input = sorted(open('input', 'r').read().replace('"','').split(','))

names,nameScores = [sum([chrVal(c) for c in n]) for n in input], []

i = 0
while i < len(names):
    nameScores.append((i+1) * names[i])
    i += 1

print(sum(nameScores))