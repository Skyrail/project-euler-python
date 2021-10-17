#
# Project Euler - Problem 18
# Copyright Aled Parry. All rights reserved.
#
"""
I'll be honest, this took me a long while to figure out, I understand recursion and I
have heard of dynamic programming but never applied it (the latter) in my day to day
programming - so this was a fun one to figure out. I know the code itself isn't the neatest
but it actually got the result - which I'm happy about!
"""

input = open('input', 'r').read().split('\n')
input = [[int(y) for y in x.split(' ')] for x in input]

def func(data, prevRow = []):
    row, maxRow = data.pop(), []

    if not data:
        return sum([row.pop(), prevRow.pop()])

    if prevRow:
        for i in range(len(row)):
            row[i] = row[i] + prevRow[i]

    for i in range(len(row) - 1):
        maxRow.append(max(row[i], row[i+1]))

    return func(data, maxRow)

print(func(input))
