def contfrac_to_frac(seq):
    num, den = 1, 0
    for u in reversed(seq):
        num, den = den + num*u, num
    return num, den

def sumOfDigits(n):
    return sum(map(int,list(str(n))))

fraction = [2]

def e_cont_frac(n):

    seq = [2 * (i+1) // 3 if i%3 == 2 else 1 for i in range(n)]
    seq[0] += 1
    return seq

a,b = contfrac_to_frac(e_cont_frac(100))

print (sumOfDigits(a))
