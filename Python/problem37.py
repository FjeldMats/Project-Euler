# Truncatable primes

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

def isTruncatable(n):
    strN = str(n)
    for i in range(0,len(strN)):

        num1 = int(strN[0:i+1])
        num2 = int(strN[i:])

        if( isPrime(num1) and  isPrime(num2)):
            pass
        else:
            return False
    else:
        return True

if __name__ == "__main__":

    SUM = 0
    count = 0
    for i in range(10,1000000):
        if(isTruncatable(i)):
            print(i)
            SUM += i
            count += 1
            
    print(SUM,count)
