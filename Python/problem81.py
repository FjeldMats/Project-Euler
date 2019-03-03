import sys
import heapq

class Node:

	def __init__(self, value, i, j):
		self.visited = False
		self.value = value
		self.distance = sys.maxsize
		self.x = i
		self.y = j
		self.neighbors = []
		self.prev = None

	def visited(self):
		self.visited = True

	def setNeighbor(self, matrix):
		#left
		#if not self.x == 0:
		#	self.neighbors.append(matrix[self.x-1][self.y])

		#right
		if not self.x == len(matrix[0])-1:
			self.neighbors.append(matrix[self.x+1][self.y])
		#up
		#if not self.y == 0:
		#	self.neighbors.append(matrix[self.x][self.y-1])

		#down
		if not self.y == len(matrix[0])-1:
			self.neighbors.append(matrix[self.x][self.y+1])	
		
	def __str__(self):
		return  "(" + str(self.x)+ ", " + str(self.y)+")"

	def __cmp__(self, otherNode):
		return self.cmp(self.distance, otherNode.distance)

	def __lt__(self, otherNode):
		return self.distance < otherNode.distance 		


#read from file
f = open("p081_matrix.txt","r")
size = 80
matrix = [[None for x in range(size)] for y in range(size)]
i = 0
for line in f:
	j = 0
	for num in line.strip().split(','):
		matrix[i][j] = Node(int(num),i,j)
		j += 1
	i += 1


#set neighbors
for i in range(size):
	for j in range(size):
		matrix[i][j].setNeighbor(matrix)

#Djikstra
start = matrix[0][0]
target = matrix[79][79]
start.distance = start.value
queue = []

heapq.heappush(queue, start)


while len(queue) != 0:
	curNode = heapq.heappop(queue)
	for neighbor in curNode.neighbors:
		if not neighbor.visited:
			dist = curNode.distance + neighbor.value
			
			if dist < neighbor.distance:
				neighbor.distance = dist
				neighbor.prev = curNode
				heapq.heappush(queue,neighbor)	
node = target
while node is not None:
	print(node, '-> ' , end = '')
	node = node.prev

print("awns: "+ str(target.distance))

