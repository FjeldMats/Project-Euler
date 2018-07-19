import math

def sumOfDigits(n):
    return sum(map(int,list(str(n))))

largestNum = 0
for a in range(0,100):
    for b in range(0,100):
        number = a**b
        if(sumOfDigits(number)>largestNum):
            largestNum = sumOfDigits(number)
            print str(largestNum) +' - ' + str(a)+'^'+str(b)+ ' - ' + str(number)

print largestNum
