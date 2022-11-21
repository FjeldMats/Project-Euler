"""
Cubic permutations (efficient)
"""

cubic_count = dict()

def print_cubes(nums):
    for num in nums:
        cube = int(round(num ** (1. / 3)))
        print(f"{cube}^3 = {num}", end = ',  ')
    print()

for i in range(0,10000):
    cube = i**3
    key = ''.join(sorted(str(cube)))
    if key in cubic_count:
        cubic_count[key].append(cube)
        if len(cubic_count[key]) == 5:
            print_cubes(cubic_count[key])
            break
    else:
        cubic_count[key] = [cube]

