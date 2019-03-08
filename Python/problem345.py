import re,itertools, collections, sys

class Node:
  def __init__(self, value, index):
    self.value = value 
    self.index = index
    self.next = None
    self.rowRank = None
  def __str__(self):
    return str(self.value) + "("+str(self.index)+ ")"

#read from file
f = open("345_matrix.txt", "r")
size = 15
matrix = [[0 for i in range(size)] for j in range(size)]
for i, line in enumerate(f):
  for j, num in enumerate(re.split(" +", line.strip())):
    matrix[i][j] = int(num)

def calcSum(perm, matrix):
  s = 0
  for i in range(len(matrix[0])):   
    s += matrix[i][perm[i]]
  return s

#initalize list
lst = [[]for i in range(size)]

#insert nodes to lst
for i, row in enumerate(matrix):
  for j, num in enumerate(row):
    lst[i].append(Node(num, j))

#sort each row
for row in lst:
  row.sort(key= lambda x: x.value, reverse = True)

current_idx = [lst[i][0].index for i in range(size)]

#set next pointers 
for i in range(len(lst)):
  for j in range(len(lst[0])-1):
    lst[i][j].next = lst[i][j+1]
    lst[i][j].rowRank = j    
  lst[i][j+1].rowRank = size-1

#print sorted rows 
#for row in lst:
#  for node in row:
#    print(node, " ",  end ='')
#  print()

def missingIndex(current_idx):
  idx = [i for i in range(len(current_idx))]
  for i in current_idx:
    if i in idx:
      idx.remove(i)
  return idx 

def diffToNext(lst, selected, missing):
  diffToNextMissing = []
  for i, row in enumerate(lst):
    cur_node = row[selected[i]]
    candidate_node = cur_node.next
    while candidate_node.index not in missing:
      if(candidate_node.next != None):
          candidate_node = candidate_node.next
      else:
        break
    diffToNextMissing.append((cur_node.value-candidate_node.value, candidate_node.rowRank - cur_node.rowRank))
  return diffToNextMissing

def iterateIndex(diff, current_idx):
  duplicates = [item for item, count in collections.Counter(current_idx).items() if count > 1] 
  if len(duplicates) == 0:
    return (None,None) 
  minDiff = sys.maxsize
  index = 0
  itr = 0
  for i, num in enumerate(diff):
    if num[0] < minDiff and current_idx[i] in duplicates:
      minDiff = num[0]
      index = i
      itr = num[1]
  return index, itr

selected = [0 for i in lst]
index = iterateIndex(diffToNext(lst, selected, missingIndex(current_idx)), current_idx)

while index[0] != None:
  selected[index[0]] += index[1]
  current_idx = [lst[i][selected[i]].index for i in range(size)]
  index = iterateIndex(diffToNext(lst, selected, missingIndex(current_idx)), current_idx)

#print(current_idx) 
s = 0
for i, row in enumerate(matrix):
  s += row[current_idx[i]]
  print(row[current_idx[i]], " ", end='')
print("=",s)
