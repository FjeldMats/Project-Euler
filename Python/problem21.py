#Amicable numbers

# let d(n) be defined as the sum of proper devisors of n
# (numbers less than n that devides evenly)
# if d(a) = b and d(b) = a, where a != b, then a and b
# are an amicable pair and each of a and b are called
# amicable numbers.

#Example
# the proper devisors of 220 are 1,2,4,5,10,20,22,44,55
# and 110;
# Therefore d(220) = 284. The proper devisor of 284 are:
# 1,2,4,71 and 142; so d(284) = 220

#Evaluate the sum of all amicable numbers under 10000.

from datetime import datetime
start=datetime.now()

def sumOfDevisors(num):
    sumOfDigits = 0
    for i in range(1,num):
        if(num % i == 0):
            sumOfDigits += i

    return sumOfDigits

def isAmicable(a,b):
    if(sumOfDevisors(a) == b and sumOfDevisors(b) == a and a != b):
        return True
    else:
        return False

sumOfAmicableNum = 0

for i in range(0,10000):
    for j in range(0,i):
        if isAmicable(i,j):
            print(i,j)
            sumOfAmicableNum += sumOfDevisors(i) + sumOfDevisors(j)

print(sumOfAmicableNum)
print(stop - start) 
