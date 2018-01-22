#problem 20

# n! means - n * (n-1) * ... * 3 * 2 * 1
# example 10! = 3628800
# the sum of those digits are: 3+6+2+8+8+0+0 = 27
# find the sum of the digits in 100!

import timeit

start = timeit.default_timer()


def factorial(num):
    fac = 1
    for i in range(1,num):
        fac *= i
        #print(i)
    return fac

number = str(factorial(100))

sumOfDigits = 0
for i in range(0,len(number)):
    sumOfDigits += int(number[i])

print(sumOfDigits)

stop = timeit.default_timer()

print(stop - start) 
