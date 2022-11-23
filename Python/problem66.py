import math 
from problem64 import count_period
from problem64 import continued_fraction
"""
Diophantine equation (unoptimal solution)
f (x,y,D) = x^2 - Dy^2 = 1

ex. 
when D = 13
minemal solution in x, where x is an positive integer
is x = 649 and y = 180

rearragning the equation to give an expression for x in terms of y
g(y) = sqrt(D*y^2 + 1)

g(1) = 3.7416573867739
g(2) = 7.2801098892805
g(3) = 10.816653826391
...
g(180) = 649 (first integer solution) 

"""

"""

sqrt(d): for x^2 - Dy^2 = 1
m = is the period of sqrt(d)
n = m - 1

p_0 = a_0, where a_0 is the first convergent of sqrt(d)
p_1 = a_1 * a_0 + 1
p_n = a_n * p_n-1 + p_n-2

q_0 = 1
q_1 = a_1
q_n = a_n * q_n-1 + q_n-2

then the minimal solution is given by

(p_n)^2 - d * (q_m)^2 = (-1)^m

x = p_n
y = q_m
"""

#2865454435422583218
#31138100617500578690

def p_n(n, a):
    if n == 0:
        return a[0]
    elif n == 1:
        return a[1] * a[0] + 1
    else:
        return a[n] * p_n(n-1, a) + p_n(n-2, a)

def q_n(n, a):
    if n == 0:
        return 1
    elif n == 1:
        return a[1]
    else:
        return a[n] * q_n(n-1, a) + q_n(n-2, a)


def fundamental(d): 
    m = count_period(d)
    a = continued_fraction(d)
    n =  m - 1

    x = p_n(n, a)
    y = q_n(n, a)

    return x, y




"""
#print(fundamental(7)) # 3, 2 -> p_n = 1 * 2 + 1 = 3 
for d in range(1000): 
    if int(d**0.5) != d**0.5:
        print(d, fundamental(d))

""" 

#ds that are wrong 
# 2, 5, 10, 13, 17, 26, 29, 35

"""

def eq(D, x, y): 
    return x**2 - D*y**2 == 1

def eqX(D, y): 
    return (D*y**2 + 1)**0.5

def find_minemal_solution2(D): 
    y = 1
    x = eqX(D, 1)
    while not (x == int(x) and eq(D, x, y)):
        y += 1
        x = eqX(D, y)
    return int(x), x, y


print(find_minemal_solution2(61))

# 1766319049, 226153980
# 335159612, 42912791

print(eqX(61, 226153980))
print(eqX(61, 42912791))

print(eq(61 , 1766319049, 226153980))
print(eq(61 , 335159612, 42912791))


"""


"""
max_x = 0
max_d = 0
for d in range(1000): 
     if int(d**0.5) != d**0.5:
        sol = find_minemal_solution2(d)
        if sol[0] > max_x:
            print(d, sol)
            max_x = sol[0]
            max_d = d

print(max_d, max_x) 
"""
"""
def find_minemal_solution(d, n, N): 
    for x in range(n,N): 
        for y in range(n,N): 
            if eq(d, x, y): 
                return x, y
    return None

xs = []
for d in range(100):
    if int(d**0.5) != d**0.5: 
        sol = find_minemal_solution(d, 1, 1000)

        if sol is None: 
            print(f"no solution for {d}")
            Nsum = 1000
            while sol == None:
                Nsum += 1000 
                print("increasing N to", Nsum)
                sol = find_minemal_solution(d, 1, Nsum)

        
        xs.append(sol) 

print(sorted(xs, key=lambda x: x[0], reverse=True))

"""

