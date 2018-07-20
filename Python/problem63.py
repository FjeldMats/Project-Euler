count = 0
for a in range(1,100):
    for b in range(1,100):
        num = a**b
        if(len(str(num)) == b):
            count += 1
            print( a,'^',b,'=',num)
print (count)
