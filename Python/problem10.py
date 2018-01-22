#find the sum all primes below 2 million
import math

million = 2000000

def isPrime(num):
    for i in range(2,math.floor(math.sqrt(num))+1):
        if(num % i == 0):
            return False
    return True

primeSum = 0

for i in range(2,million):
    if(isPrime(i)):
        primeSum += i

print("Sum:",primeSum)
