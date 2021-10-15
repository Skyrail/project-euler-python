#
# Project Euler - Problem 1
# Copyright Aled Parry. All rights reserved.
#

"""
Going back and re-completing the problems I'd previously done in C, this time in Python
- although I'd like to go back and do C in the future. both for speed and for learning.
For now though I'm getting to know Python better - and just look at this, it makes it 
so much easier!
"""
print(sum(set(range(0, 1000, 3)) | set(range(0, 1000, 5))))
