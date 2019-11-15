"""

Resilience

A positive fraction whose numerator is less than its denominator is called a
proper fraction. For any denominator, d, there will be d-1 proper fractions;
for example, with d = 12:
    1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator R(d), to be the
ratio of its proper fraction that are resilient; for example R(12) = 4 / 11
in fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10.

Find the smallest denominator d, having a resilience R(d) < 15499 / 94744.

R(12)

1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.
1/12, 1/6,  1/4,  1/3,  5/12, 1/2,  7/12, 2/3,  3/4,  5/6,   11/12
 1                       2           3                         4

-> 4/11

"""

import time
from sympy.ntheory import factorint
from fractions import Fraction

def factors(n):
    return factorint(n)

def phi(n):
    m = 1
    for key, value in n.items():
        m *= (key**value - key**(value-1))
    return m

def R(d):
    return Fraction(phi(factors(d)), d-1)

d = 892371480
while True:
    if R(d) < Fraction(15499, 94744):
        break;
    d += 1
print(d)
