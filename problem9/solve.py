#
# Project Euler - Problem 9
# Copyright Aled Parry. All rights reserved.
#
"""
This was my initial attempt at the task. It's slow, and not very elegant.
It is a very naive brute force, but does get the answer, eventually
"""
def bruteForceTriple(r):
    for a in range(r):
        for b in range(r):
            for c in range(r):
                if a+b+c != r: continue
                if pow(a,2) + pow(b,2) != pow(c,2): continue
                if a*b*c != 0: return a*b*c

# print(bruteForceTriple(1000))

"""
This was my second attempt after reading a little on generating pythagorean triples
I can't profess to understand why it works but it's a whole lot quicker than brute
forcing it as above. Thank you Euclid!
"""
def a(m,n):
    return pow(m,2) - pow(n,2)

def b(m,n):
    return 2*m*n

def c(m,n):
    return pow(m,2) + pow(n,2)

def euclidsTriple(r):
    for m in range(1,r):
        for n in range(1,m):
            _a,_b,_c = a(m,n),b(m,n),c(m,n)

            if _a+_b+_c == r: 
                return _a,_b,_c

_a,_b,_c = euclidsTriple(1000)

print(_a*_b*_c)