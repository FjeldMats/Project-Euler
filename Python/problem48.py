#Self powers
Sum = 0
for i in range(1,1000):
    print(i)
    Sum += i**i

strSum = str(Sum)

print(strSum[-10:])
