import math
import itertools
def isPrime(n):
    if(n == 2):
        return True

    for i in range(2, int(math.sqrt(n)+2)):
        if(n % i == 0):
            return False
    else:
        return True

def combTuple(list):
    tupels = []
    for pair in itertools.combinations(list , 2):
        tupels.append(pair)
    return tupels

def concat(a, b):
    return int(str(a)+str(b))

def allPrime(list):
    for pair in combTuple(list):
        if(isPrime(concat(pair[0], pair[1])) and isPrime(concat(pair[1], pair[0]))):
            continue
        else:
            return False
    else:
        return True

lowest = float('inf')

primes = []
for i in range(2,10000):
    if(isPrime(i)):
        primes.append(i)

minval = 99999999999
lim = len(primes)-1
for a in range(lim):
    for b in range(a+1, lim):
        for c in range(b+1, lim):
            print(a,b,c)
            for d in range(c+1, lim):
                for e in range(d+1, lim):


                    num1 = primes[a]
                    num2 = primes[b]
                    num3 = primes[c]
                    num4 = primes[d]
                    num5 = primes[e]

                    numbers = [num1, num2, num3, num4, num5]

                    if(allPrime(numbers)):
                        if(sum(numbers)<lowset):
                            lowest = sum(number)
                            print(numbers, lowest)
print("aws:",lowset)
