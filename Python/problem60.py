"""
Problem 60:

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import math
import time

def memoize(f):
    memory = {}
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]
    return inner

@memoize
def isPrime(num):
    if num < 2:
        return False
    for i in range(2,math.floor(math.sqrt(num))+1):
        if(num % i == 0):
            return False
    return True

def genPrime(n):
    "generate all primes below n"

    number_of_primes = 0
    num = 0
    while number_of_primes < n:
        if isPrime(num):
            number_of_primes += 1
            yield num
        num += 1

def combine(n1, n2):
    return int(float("%s%s"%(str(n1),str(n2))))


start = time.time()
primes = list(genPrime(1200))

pairs = {}

for prime1 in primes:
    pairs[prime1] = []
    for prime2 in primes:
        if isPrime(combine(prime1,prime2)) and isPrime(combine(prime2,prime1)):
            pairs[prime1].append(prime2)


start_prime = 0
numbers = [primes[start_prime]]

def find_next_prime(pairs, numbers):
    for prime in primes:
        if all(x in pairs[prime] for x in numbers):
            return prime


while len(numbers) < 5:
    if start_prime == len(primes)-1:
        print("no answer")
        break

    next = find_next_prime(pairs, numbers)
    if next == None:
        start_prime += 1
        numbers = [primes[start_prime]]
    else:
        numbers.append(next)


print(numbers, sum(numbers))
end = time.time()
print(end - start)
