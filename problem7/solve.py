#
# Project Euler - Problem 7
# Copyright Aled Parry. All rights reserved.
#
from math import sqrt
"""
I'll be honest, I can't find the source of my original C version of this. I can only find the folder
which makes me think I may have cheated the first time around - with aid from Wolfram Alpha(!) With that
said, here's my Python implementation, it's a little sluggish but a whole lot quicker than checking every
number as it limits the checks to all the previous prime numbers.
"""
# Don't include 1 in the primes list because it'll divide into every number
# Start the count at 1 because the prime list already has 2 in it
# num starts at 1 because we want to start counting from 3 (1+2) in the loop
count, num, primes = 1, 1, [2] 
while count < 10001:
    num += 2  # Even numbers can't be prime (other than two, of course)
    for i in primes:
        if num % i == 0: break # Not prime
    else: # Prime number
        primes.append(num)
        count += 1
            
print(primes.pop())