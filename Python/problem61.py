"""
Problem 61: Cyclical figurate numbers

1. Cyclical figurate numbers 2 last digits are the same as the first 2 digits of the next number
2. each number is a different type of figurate number

"""

def triangle(n):
    return n*(n+1)//2

def square(n):
    return n*n

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

def heptagonal(n):
    return n*(5*n-3)//2

def octagonal(n):
    return n*(3*n-2)

def polygonal(n, f):
    return f(n)


simple_polygonal = [triangle, square, pentagonal]
full_polygonal = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]

polygonals = full_polygonal

all_polyonal_numbers = []
for f in polygonals:
    all_polyonal_numbers.append([])

# genereate first 1000 numbers for each polygonal    
for i in range(100000):
    for index, f in enumerate(polygonals):
        num = polygonal(i, f)
        if num > 999 and num < 10000: # only 4 digit numbers
            all_polyonal_numbers[index].append(num)

def is_cyclical(n1, n2):
    return str(n1)[-2:] == str(n2)[:2]

def is_cyclical_link(n, nums):
    for num in nums:
        if is_cyclical(n, num):
            return num
    return None

# find cyclical links for a number
def find_links(num, other_polygonals):
    cyclical_nums = []
    for lst in other_polygonals:
        link = is_cyclical_link(num, lst)
        if link:
            cyclical_nums.append(link)  
    return cyclical_nums

# find 
def find_links_ploygonal(polygonals, index):
    cyclical_links = []
    other_polygonals = polygonals[:index] + polygonals[index+1:]
    starts = polygonals[index]
    
    for num in starts:
        cyclical_nums = find_links(num, other_polygonals)
        if cyclical_nums:
            cyclical_links.append((num, cyclical_nums))
    return cyclical_links
        

all_links = []
for index, polygonal in enumerate(all_polyonal_numbers):
    links = find_links_ploygonal(all_polyonal_numbers,index)
    all_links.append(links)


def walk_link(cur, all_links, chain, initial):
    
    if len(chain) > 2 and cur == chain[0]:
        return [chain]
    if len(chain) > len(polygonals):
        return []
    for i in all_links:
        for j in i:
            if cur == j[0]:
                lst = []
                for k in j[1]: 
                    lst.append(walk_link(k, all_links, chain + [k], initial))
                return lst
    return []

# remove all empty lists
def remove_empty(lst):
    new_lst = []
    for i in lst:
        if i:
            if isinstance(i[0], list):
                new_lst += remove_empty(i)
            else:
                new_lst.append(i)
    return new_lst

def walk_link_helper(start, all_links):
    return remove_empty(walk_link(start, all_links, [start], start))


# check if each number has a different type of polygonal
def check_plygonal_type(lst, polygonals):
    """
    Some numbers can have multiple polygonal types

    1. check that no number has the duplicate polygonal type
    """
    used_polygonals = []

    for i, num in enumerate(lst):
        used_polygonals.append([])
        for j, f in enumerate(polygonals):
            if num in all_polyonal_numbers[j]:
                used_polygonals[i].append(j) 

    # check for duplicates
    for i, lst_i in enumerate(used_polygonals):
        for j, lst_j in enumerate(used_polygonals):
            if set(lst_i) == set(lst_j) and i != j:
                return False 

    # get the differencve 
    used_polygonals = list(map(set, used_polygonals))
    diff = set.union(*used_polygonals) - set.intersection(*used_polygonals)
    return len(diff) == len(all_polyonal_numbers)
            

final_nums = []
for i in all_links[0]:
    link = walk_link_helper(i[0], all_links)
    for j in link:
        lst = list(set(j))
        if check_plygonal_type(lst, polygonals):
            final_nums.append(lst)

final_nums = filter(lambda x: len(x) == len(polygonals), final_nums)

for i in final_nums:
    print(i, sum(i))
