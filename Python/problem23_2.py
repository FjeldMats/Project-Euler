from math import sqrt

def d(n):
    Sum = 1
    t = sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0:
            Sum += i + n / i

    if t == int(t): #ikke tell kvadratroten to ganger
        Sum -= t
    return Sum

limit = 20162
Sum = 0
abn = set() #legger alle abundent numbers i et set
for n in range(1, limit):
    if d(n) > n:
        abn.add(n)
    if not any( (n-a in abn) for a in abn ):
        Sum += n
print(Sum)
