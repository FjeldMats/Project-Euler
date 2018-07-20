import math

def square(n):
    return n**2

def digitSquare(n):
    return sum(map(square,(map(int,list(str(n))))))


def chain(startVal):
    n = startVal
    #iterations = 0
    while n != 1 and n != 89:
        n = digitSquare(n)
        #iterations += 1
        #print(n, iterations)
    return n

n = 0
for i in range(1,10000000):

    if(chain(i) == 89):
        n += 1
        if i%100000 == 0:
            print(i,"/",10000000)
print(n)
