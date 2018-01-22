#Digit factorials

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

def curiousN(n):
    listN = list(str(n))

    curiousSum = 0
    for i in range(0, len(listN)):
        curiousSum += factorial(int(listN[i]))
    if(curiousSum == n):
        print(curiousSum,n)
        return True

endSum = 0
for i in range(3,100000):
    if(curiousN(i) == True):
        endSum += i

print("the sum of all numbers which are equal to the sum of the factorial of their digits", endSum)
