#Digit fifth powers

limit =  9**5 * 5

def digitSum(num,power):
    Snum = str(num)
    numSum = 0
    for i in range(0,len(Snum)):
        numSum += int(Snum[i])**power
        #print(Snum[i])
    if(numSum == num):
        print(num)
        return num
    else:
        return 0

endSum = 0
for i in range(2,limit+1):
    endSum += digitSum(i,5)

print(endSum)
