#
# Project Euler - Problem 40
# Copyright Aled Parry. All rights reserved.
#
from math import prod

"""
I don't know if this is the neatest way of solving this but it's here and it's quick.
All of the problems I've solved so far have the difficulty rating of 5% - some of them make me
think I could handle 10% - others make me dread the next level up. This one, more like 1% - but
as I've said before, it's nice to have the simple ones to make up for the ones that leave me stuck.
"""

num,numStr,n = 1,'1',[1,10,100,1000,10000,100000,1000000]
while len(numStr) <= int(1e6):
    num += 1
    numStr += str(num)

print(prod([int(numStr[x-1]) for x in n]))