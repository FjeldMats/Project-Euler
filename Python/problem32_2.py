nums = [1,2,3,4,5,6,7,8,9]

final = False
index = 0

while True:

    #Setp 1 biggest - i
    bigI = -1
    for i in range(0,len(nums)-1):
        if(nums[i] < nums[i+1]):
            bigI = i
    if(bigI == -1):
        #print("final")
        break
        print(nums)
    else:

        #Step 2 biggest - j
        bigJ = 0
        for j in range(0,len(nums)):
            if(nums[bigI] < nums[j]):
                bigJ = j

        #print(bigI,bigJ)

        #Step 3 - Swap nums[i] and nums[j]
        tempI = nums[bigI]
        tempJ = nums[bigJ]

        nums[bigJ] = tempI
        nums[bigI] = tempJ

        #Step 4 - reverse from nums[i+1] ... to nums[-1] (last digit)
        reverseNums = nums[bigI+1:len(nums)]
        if(len(reverseNums) != 1):
            del nums[bigI+1:len(nums)]
            reverseNums.reverse()
            nums = nums + reverseNums

        #print(reverseNums)
        #print(nums)

        #list into string
        strNum = ''
        for i in range(0, len(nums)):
            strNum += str(nums[i])
        #print(strNum)
        #print(strNum)
        a = strNum[0:2]
        b = strNum[1:4]

        a1 = strNum[0:3]
        b2 = strNum[3:4]
        c = strNum[4:9]

        #print(a,b,c)
        #print(int(a) * int(b) == int(c))

        if(int(a) * int(b) == int(c) or int(a1) * int(b2) == int(c)):
            print(c)
