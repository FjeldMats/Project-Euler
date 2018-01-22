#Coin sums
#       0  1  2  3   4   5   6   7
#       a  b  c  d   e   f   g
coin = [1, 2, 5, 10, 20, 50, 100, 200]
#      200 100 40 20 10  4    2    1

count = 0
coinSet = set()

for a in range(0,200+1):
    print(float(a/200)*100,"%")
    for b in range(0,100+1):
        for c in range(0,40+1):
            for d in range(0,20+1):
                for e in range(0,10+1):
                    for f in range(0,4+1):
                        for g in range(0,2+1):

                            coinSum = a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100
                            if(coinSum == 200):
                                count += 1
                                #print(a,b,c,d,e)
                                coinStr = str(a) +str(b) +str(c) +str(d) +str(e) +str(f)+str(g)
                                coinSet.add(coinStr)
                                #coinSet.add(coinInt)
                                #cprint(coinStr)

print(count)
print(coinSet)
print(len(coinSet))
 # + 1 since the last coin isnt in the loop, becouse its only one possiblitiy
 # of getting 1 with the coin ( 1 x 200p)
