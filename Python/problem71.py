import math

def reduced_proper_fraction(n, d):
    return True if (n<d) and (math.gcd(n, d) == 1) else False 

def solve_naive(D):
    frac = []
    for n in range(1,D+1):
        for d in range(1,D+1):
            if reduced_proper_fraction(n, d):
                frac.append((f"{n}/{d}", n/d))

    frac = sorted(frac, key=lambda x: x[1])

    for index, i in enumerate(frac):
        if i[0] == "3/7":
            print(frac[index-1][0])

# https://en.wikipedia.org/wiki/Farey_sequence
def farey_sequence_HCF(n):
    seq = []
    (a, b, c, d) = (0, 1, 1, n)
    while (c <= n):
        k = (n + b) // d
        (a, b, c, d) = (c, d, k * c - a, k * d - b)
        if reduced_proper_fraction(a, b):
            seq.append((a, b))
    return seq


def farey_sequence_search(lower, upper, target, D):
    """search for the closest fraction to target in the Farey sequence of order D"""

    frac = []

    # keep calculating the Farey sequence until the upper bound is reached
    a, b = upper[0] + lower[0], upper[1] + lower[1]  
    while b <= D:
        frac.append((a, b))
        
        # set a,b to upper or lower bound
        # depending on if a,b is greater or less than to target
        if a/b >= target[0]/target[1]:
            upper = (a, b)
        elif a/b < target[0]/target[1]:
            lower = (a, b)
        
        a, b = upper[0] + lower[0], upper[1] + lower[1]
    
    return frac[-1]

if __name__ == "__main__":
    #solve_naive(8) # naive solution (brute force)
    print(farey_sequence_search((0,1), (1,1), (3,7), 1_000_000)) # farey sequence solution
    #print(reduced_proper_fraction(428570, 999997))
