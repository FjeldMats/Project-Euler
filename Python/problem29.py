tall = set()

grense = 100

for i in range(2,grense + 1 ):
    for j in range(2,grense + 1):
        
        tall.add(i**j)

print(tall)
print(len(tall))
