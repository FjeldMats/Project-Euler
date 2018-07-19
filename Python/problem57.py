def contfrac_to_frac(seq):
    num, den = 1, 0
    for u in reversed(seq):
        num, den = den + num*u, num
    return num, den

fraction = [1]

for i in range(999):
    fraction.append(2)

count = 0
for i in range(1000):
    a,b = contfrac_to_frac(fraction[0:i+1])
    a = len(str(int(a)))
    b = len(str(int(b)))
    if(a>b):
        count += 1
        #print a,"/",b, "i = ",i

print count
