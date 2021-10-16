#
# Project Euler - Problem 16
# Copyright Aled Parry. All rights reserved.
#
"""
I'll be honest, this one seems deceptively simple. I don't know if it's easier because 
of python's list comprehensions or if it is just a simple problem
"""

num = pow(2,1000)

print(sum([int(i) for i in str(num)]))