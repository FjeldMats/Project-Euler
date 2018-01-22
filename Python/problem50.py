#Consecutive prime sum

def isPrime(n):
    limit = int(abs(n)**(1/2)+1)
    if(n == 1):
        return False
    for i in range(2,limit):
        if n % i == 0:
            return False
    else:
        return True

primes = []
i = 0
while len(primes) < 1000000 :
    if( isPrime(i) ):
        primes.append(i)
    i += 1

print("done gen. primes to", len(primes))

for i in range(0,len(primes)):

    Sum = 0
    index = 0

    while(not Sum >= primes[i]):
        Sum += primes[index]
        index += 1
        if(Sum == primes[i]):
            print(Sum,index)
            break
