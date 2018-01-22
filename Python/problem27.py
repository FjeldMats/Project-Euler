#Quadratic primes
import math

def isPrime(n):
    limit = int(math.fabs(n)**(1/2))
    for i in range(2,limit + 10):
        if n % i == 0:
            return False
    else:
        return True

def makeQuad(a,b,n):
    return n**2 + a*n + b

bigA = 0
bigB = 0
bigN = 0



for i in range(-1000,1000):
    for j in range(-1000,1000):
        n = 0
        nrPrimes = 0
        while isPrime(makeQuad(i,j,n)):
            #print(makeQuad(i,j,n), isPrime(makeQuad(i,j,n)) )
            n += 1
            nrPrimes += 1
        if(nrPrimes>bigN):
            bigN = nrPrimes
            bigA = i
            bigB = j
            print("a: ",i,"b: ",j,"- nrPrimes: ",nrPrimes)


print("a: ",bigA," b:",bigB," number of consevutive primes: ",bigN)
print("awsr :", bigA*bigB)
