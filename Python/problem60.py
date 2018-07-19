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


primes = []
for i in range(100):
    if(isPrime(i)):
        primes.append(i)

lim = len(primes)-1

lowest = 0

for a in range(lim):
    print 'a',a
    for b in range(a, lim):
        for c in range(b, lim):
            for d in range(c, lim):

                num1 = primes[a]
                num2 = primes[b]
                num3 = primes[c]
                num4 = primes[d]

                allPrime = True
                stuff = [num1, num2, num3, num4]
                for L in range(1, len(stuff)+1):
                    for subset in itertools.combinations(stuff, L):
                        if(not isPrime(int(''.join(map(str, stuff))))):
                            allPrime = False

                if(allPrime):
                    if(num1+num2+num3+num4 < lowest):
                        lowest = num1+num2+num3+num4
                        print lowest

print lowest
