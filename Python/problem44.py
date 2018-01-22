#Pentagon numbers (44)
import math

pentagon = set()

for i in range(1,10000):
    pent = (i*(3*i -1)) / 2
    pentagon.add(int(pent))

D = 10000000
for x in pentagon:
    for y in pentagon:
        Sum = x+y
        Diff = abs(y-x)
        if ((Sum in pentagon) and (Diff in pentagon)):
            if(D > Diff):
                D = Diff
print(D)
