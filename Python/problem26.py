#Reciprocal cycle - problem 26
bigNumber = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 #50
bigNumber *= bigNumber
bigNumber *= bigNumber
bigNumber *= bigNumber
bigNumber *= bigNumber
bigNumber *= bigNumber
bigNumber *= bigNumber
bigNumber *= bigNumber
bigNumber *= bigNumber


def findRep(num):
    Snum = str(num)
    Lnum = len(Snum)
    for i in range(2,int(Lnum)):
        #print(Snum[0:i], Snum[i:i+i])
        if(Snum[0:i] == Snum[i:i+i]):
            #print("found")
            print()
            print(Snum[0:i], Snum[i:i+i])
            return str(Snum[0:i])
longest = 1
longestnum = 0
d = 0
for i in range(2,1000):
    num = int(bigNumber//i)
    rep = findRep(num)
    lrep = len(str(rep))
    print("1/"+str(i)+" =  "+ "0."+str(num), rep, lrep)
    if(lrep > longest):
        longest = lrep
        longestnum = rep
        d = i

print(longestnum)
print(d)
