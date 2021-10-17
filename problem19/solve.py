#
# Project Euler - Problem 19
# Copyright Aled Parry. All rights reserved.
#
from datetime import date
from math import floor

"""
Now this one I could have brute forced using the given information but I decided
to do a littler search and came across Zeller's Congruence - that magic, albeit weird
little formula! It took me a while to get it working just right (taking into account)
the 13/14 Jan/Feb rule but eventually I got there.

To be honest, the easiest way to do this, given I'm already using the datetime module,
would be to use the weekday() function that does all the heavy lifting - but that's no fun
"""


def dayFromDate(date: date):
    d = date.day
    m = date.month
    y = date.year

    if m in [1, 2]:
        m += 12
        y -= 1

    K = y % 100
    J = floor(y / 100)

    # Zeller's Congruence - c'est magique!
    h = (d + floor((13 * (m + 1))/5) + K +
         floor(K/4) + floor(J/4) - (2 * J)) % 7

    return h


count = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        d = dayFromDate(date(day=1, month=m, year=y))

        if int(d) == 1:
            count += 1

print(count)
