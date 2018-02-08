def fac(n):
    if(n == 0):
        return 1
    return n * fac(n-1)

def nCr(n,r):
    if(r>n):
        return 0;
    return fac(n) / (fac(r) * fac(n-r))


million = 1000000
count = 0

for i in range(1,101):
    for j in range(1,i):
        if(nCr(i,j)>million):
            #print(nCr(i,j))
            count += 1
