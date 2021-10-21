#
# Project Euler - Problem 28
# Copyright Aled Parry. All rights reserved.
#
"""
Initially I was visualising it in my mind as some sort of giant multidimensional
list - then I realised there was a pattern. Once you find the pattern it's easy.
"""

sum,num = 1,1
for c in range(1,501):
    for i in range(1,5):
        num += c*2
        sum += num

print(sum)