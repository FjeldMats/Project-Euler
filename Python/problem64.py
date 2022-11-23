import math 

def count_period(n):

    # check if n is a perfect square - > no period
    if math.sqrt(n) == int(math.sqrt(n)):
        return 0

    p = 0

    num = 0.0
    den = 1.0
    a0 = int(math.sqrt(n))
    a = int(math.sqrt(n))
    
    # given in https://web.math.princeton.edu/mathlab/jr02fall/Periodicity/alexajp.pdf
    # cited by wikiepedia https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
    # the period will repeat when a = 2 * a0
    while a != 2*a0:
        num = den*a - num
        den = (n - num**2)/den
        a = int((a0 + num)/den)
        p += 1
    return p


def continued_fraction(n):

    # check if n is a perfect square - > no period
    if math.sqrt(n) == int(math.sqrt(n)):
        return 0

    dens = []
    p = 0

    num = 0.0
    den = 1.0
    a0 = int(math.sqrt(n))
    dens.append(a0)
    a = int(math.sqrt(n))
    
    while a != 2*a0:
        num = den*a - num
        den = (n - num**2)/den
        a = int((a0 + num)/den)
        dens.append(a)
        p += 1
    return dens

if __name__ == "__main__":
    N = 10_000
    count = 0
    for i in range(2,N+1):
        if count_period(i) % 2 != 0:
            count += 1

    print(f"there are {count} continued fractions for N <= {N} with odd period")
