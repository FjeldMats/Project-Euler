row = 0
add = 0
Sum = 1
while add <= 1001:
    add += 2
    for i in range(4):
        Sum += add

print(Sum)
