import re,itertools
f = open("345_matrix.txt", "r")
size = 15

matrix = [[0 for i in range(size)] for j in range(size)]

i = 0
for line in f:
  j = 0
  for num in re.split(" +", line.strip()):
    #print(i,j)
    matrix[i][j] = int(num)
    j += 1
  i += 1


def calcSum(perm, matrix):
  s = 0
  #print(perm)
  for i in range(len(matrix[0])):
    #print(matrix[i][perm[i]])
    s += matrix[i][perm[i]]
  return s

highestSum = 0
curSum = 0
permutations = list(itertools.permutations([i for i in range(size)]))

print(len(permutations))

for perm in permutations:
  curSum = calcSum(perm, matrix)
  if curSum > highestSum:
    highestSum = curSum

print(highestSum)




