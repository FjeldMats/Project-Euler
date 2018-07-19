import math

'''
It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1 2
15 = 7 + 2x2 2
21 = 3 + 2x3 2
25 = 7 + 2x3 2
27 = 19 + 2x2 2
33 = 31 + 2x1 2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?
'''

def isTwiceSquare(n):
    squareTest = math.sqrt(n/2)
    return squareTest == int(squareTest)

def isPrime(n):
    if(n == 2):
        return True

    for i in range(2, int(math.sqrt(n)+1)):
        if(n % i == 0):
            return False
    else:
        return True

def listOfPrimes(upperLim):
    primeList = []
    for i in range(2 , upperLim):
        if(isPrime(i)):
            primeList.append(i)
    return primeList

primeList = listOfPrimes(10000)
result = 1
notFound = True

while notFound:
    result += 2

    j = 0
    notFound = False
    while(result >= primeList[j]):
        if(isTwiceSquare(result-primeList[j])):
            notFound = True
            break
        j += 1

print result
