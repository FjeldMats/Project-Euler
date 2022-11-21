"""
Cubic permutations (very unefficient)
"""
import itertools

def check_cube(num): 
    # check if cubic root of num to the power of 3 is the number itself
    return int(round(num ** (1. / 3))) ** 3 == num

def get_all_permutations(num):
    # get all permutations of num
    return set(int(''.join(p)) for p in itertools.permutations(str(num)) if len(str(int(''.join(p)))) == len(str(num)))

def cubes(num):
    # cubes that are permutations of num
    return [n for n in get_all_permutations(num) if check_cube(n)]

def print_cubes(nums):
    for num in nums:
        cube = int(round(num ** (1. / 3)))
        print(f"{cube}^3 = {num}", end = ',  ')
    print()


for i in range(0,10000):
    c = cubes(i**3)
    if len(c) >= 5:
        print_cubes(c)
        break
