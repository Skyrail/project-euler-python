#
# Project Euler - Problem 16
# Copyright Aled Parry. All rights reserved.
#
from math import floor

"""
This is so far from my best work, I'll admit that much. It works. It gets the answer, and quickly.
But ugh, my brains not into tidying it up right now after taking the time to make it work. Lots
of finiky conditionals just to get everything right. Things that could be done to refactor:
1) Extract out place value functionality
2) Code, if written properly could probably be made recursively, maybe not, it might need too much context
3) So much clarity could be made out of the lexical decisions
"""

numMap = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

numTensMap = {
    0: '',
    10: '',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}


def numToWords(num):
    if num in numMap:
        return numMap[num]
    if num in numTensMap:
        return numTensMap[num]

    units = num % 10
    tens = floor((num % 100)/10)*10 if (num % 100) >= 20 else (num % 100)
    hundreds = floor((num % 1000)/100)
    thousands = floor((num % 10000)/1000)

    unitsStr = numMap[units] if units > 0 and tens >= 20 else ''
    tensStr = (numTensMap[tens] if tens >= 20 else numMap[tens]) if tens > 0 else ''
    hundredsStr = f'{numMap[hundreds]} hundred' if hundreds > 0 else ''
    thousandsStr = f'{numMap[thousands]} thousand' if thousands > 0 else ''

    hundredsAnd = 'and' if (units > 0 or tens > 0) and hundreds > 0 else ''
    thousandsAnd = 'and' if (units > 0 or tens > 0 or hundreds > 0) and thousands > 0 else ''

    return f'{thousandsStr} {thousandsAnd} {hundredsStr} {hundredsAnd} {tensStr} {unitsStr}'  

sum = 0
for i in range(1, 1001):
    sum += len(numToWords(i).replace(' ', ''))

print(sum)
