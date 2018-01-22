#Lexiographic permutations

#hva er den millionte Lexiographic permutations av:
#[0,1,2,3,4,5,6,7,8,9]

nums = [0,1,2,3,4,5,6,7,8,9]


print(nums)

final = False
Dindex = 1000000-1 # trekker fra en fordi det millionte tallet har inx = 999999
index = 0

while index != Dindex:

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
        index += 1
        if(index == Dindex):
            print(nums)
