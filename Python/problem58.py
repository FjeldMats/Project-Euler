import math

def isPrime(n):
    if(n == 2):
        return True

    for i in range(2, int(math.sqrt(n)+2)):
        if(n % i == 0):
            return False
    else:
        return True

corner = 1
lineCount = 2
cornerNums = []
totalNumbers = 1
totalPrimes = 0
condition = True


while condition:
    for i in range(4):
        totalNumbers += 1
        corner += lineCount
        #print corner
        if(isPrime(corner)):
            totalPrimes += 1
            #print corner
        if(not totalPrimes == 0):
            print float(float(totalPrimes)/float(totalNumbers))*100
            if((float(totalPrimes)/float(totalNumbers))*100 < float(10)):
                condition = False
                break
    lineCount += 2

print lineCount-1
