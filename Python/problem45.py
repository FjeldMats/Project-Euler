triangle = []
pentagon = []
hexagonal = []

upperlimit = 100000

#triangle nums
for i in range(1,upperlimit):
    tri = (i*(i + 1))/2
    triangle.append(int(tri))

#pentagon nums
for i in range(1,upperlimit):
    pent = (i*(3*i - 1)) / 2
    pentagon.append(int(pent))

#hexagonal nums
for i in range(1,upperlimit):
    hexa = (i*(2*i - 1))
    hexagonal.append(int(hexa))

for i in triangle:
    if i in triangle and i in pentagon and i in hexagonal:
        print(i)
