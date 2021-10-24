#
# Project Euler - Problem 36
# Copyright Aled Parry. All rights reserved.
#

"""
I don't know if it was premature efficiency to calculate all of the decimal palindroms first or the right way to do it
but either way it's quick enough and didn't take long to solve.
"""

def decimalPalindromes(n):
    palindromes = set()
    for i in range(0,n):
        if str(i) == str(i)[::-1]:
            palindromes.add(i)
    return palindromes

palindromes = []
for i in decimalPalindromes(int(1e6)):
    bin = str(format(i, 'b'))
    if bin == bin[::-1]:
        palindromes.append(i)

print(sum(palindromes))