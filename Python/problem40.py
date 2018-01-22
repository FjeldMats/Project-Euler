fraction = ''
i = 0
while len(fraction) < 1000000:
    fraction += str(i+1)
    i += 1

print(len(fraction))
product = 1
index = [1,10,100,1000,10000,100000,1000000]

for i in range(0,len(index)):

    print(int(fraction[index[i]-1]),index[i])
    product *= int(fraction[index[i] - 1])

print(product)
