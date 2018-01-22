import math

def isPrime(n):
    limit = int(abs(n)**(1/2)+1)
    if(n == 1):
        return False
    for i in range(2,limit):
        if n % i == 0:
            return False
    else:
        return True

def isPermutation(n,n2):
    strNumber = str(n)
    listNumber = list(strNumber)

    strNumber2 = str(n2)
    listNumber2 = list(strNumber2)

    count = 0
    for i in listNumber:
        if i in listNumber2:
            listNumber2.remove(i)
            count += 1
    if(count == len(listNumber) and len(listNumber2) == 0):
        return True
    else:
        return False

primes = []

for i in range(999,9999):
    if( isPrime(i) ):
        primes.append(i)

for i in range(0,len(primes)):
    for j in range(1000,5000):
        if(isPrime(primes[i] + j) and isPrime(primes[i] + j + j) and
         isPermutation(primes[i], primes[i] + j) and
         isPermutation(primes[i], primes[i] + j+j) ):
            print(str(primes[i])+", "+str(primes[i] + j)+", "+str(primes[i] + j+j)+" inc by:"+str(j))
