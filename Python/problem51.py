"""

*3 -> 13 23 43 53 73 83 are all primme

56**3 ->56003, 56113, 56333, 56443, 56663, 56773, and 56993 are prime


1. create a mask for diffrent replacements - 0s and 1s
2. list of all possble permutations for the non replacements
3. put numbers between 0 and 9 for replacements
4. check if the number is prime

"""
import itertools, math

def per(n):
    lst = []
    for i in range(1<<n):
        s=bin(i)[2:]
        s='0'*(n-len(s))+s
        lst.append(s)
    return lst

def isPrime(num):
    for i in range(2,math.floor(math.sqrt(num))+1):
        if(num % i == 0):
            return False
    return True

for digitLength in range(6,7):

    # create masks
    masks = per(digitLength)

    for mask in masks:
        # 1 = replacement number -> dont fill in
        # 0 = put in permutations

        n = mask.count('0') # how long is the permutation?
        if n > 1 and n != digitLength:
            # has to be larger than 1
            permutations = list(itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=n))

            for perm in permutations:
                number = ''
                index = 0
                for digit in mask:
                    if digit == '1':
                        number += '*'
                    if digit == '0':
                        number += str(perm[index])
                        index += 1
                #print(number)

                family = []
                for i in range(1,10):
                    replacement = int(number.replace('*', str(i)))
                    if isPrime(replacement):
                        family.append(replacement)
                        #print(f"{number} -> {replacement}")

                if len(family) == 8:
                    print(f"{number} ({len(family)}) -> {sorted(family)} ")
                    print(sorted(family)[0])
