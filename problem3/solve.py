#
# Project Euler - Problem 3
# Copyright Aled Parry. All rights reserved.
#
"""
Almost copied straight from my C solution. Except this time I've got it 
to print out the result for me rather than all the results. It's short and sweet I think
albeit maybe not very clear.
"""
i, j, prime = 600851475143, 2, 0

while j < i and i % j != 0:
    j += 1
    if i % j == 0:
        prime, i, j = max(j, prime), i/j, 2

print(prime)