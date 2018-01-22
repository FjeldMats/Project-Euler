#Integer right triangles
import math

index = 0
big = 0
bP = 0
for p in range(2,1001):
    #print("p:",p)
    setOfNums = set()

    for i in range(1,p):
        for j in range(1,p):

            k2 = i**2 + j**2
            k = math.sqrt(k2)


            if(i+j+k == p and k == int(k)):
                lis = [i,j,int(k)]
                lis.sort()
                SET = str(lis[0])+" "+str(lis[1])+" "+str(lis[2])
                #print(SET)
                setOfNums.add(SET)

                if len(setOfNums) > big:
                    big = len(setOfNums)
                    print(p,setOfNums)
                    bP = p

print(bP)
