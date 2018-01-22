with open ("names.txt", "r") as txtFile:
    data=txtFile.readlines()

data1 = str(data[0])

def letterScore(letter):
    alfaL = "abcdefghijklmnopqrstuvwxyz"
    alfa = list(alfaL)
    for i in range(0, len(alfaL)):
        if(str() +letter+ str() ==  alfaL[i].upper()):
            #print(str() +letter+ str(), alfaL[i].upper())
            return i+1
    else:
        return 0

names = data1.split(",")
names.sort()

namesSum = 0

for i in range(0,len(names)):
    name = list(names[i])
    delSum = 0
    for j in range(0,len(name)):
        delSum += letterScore(name[j])
    namesSum += delSum *(i+1)

print(namesSum)
