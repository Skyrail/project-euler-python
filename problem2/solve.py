#
# Project Euler - Problem 2
# Copyright Aled Parry. All rights reserved.
#
"""
Again, going over previous problems - this one's short and quick but I'm not 
thrilled with the way it's done, I feel like...maybe it could be done more
concicsely? Hmm.
"""

i,pi,s = 1,1,0
while i < 4e6:
    s += i if i % 2 == 0 else 0
    i,pi = i+pi, i

print(s)