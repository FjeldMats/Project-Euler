#sub-String divisibility (43)

def listToNum(listOfNums):
    strNumber = ''
    for i in range(0,len(listOfNums)):
        strNumber += str(listOfNums[i])
    return int(strNumber)

def permutations():
    allPer = []
    nums = [0,1,2,3,4,5,6,7,8,9]
    nums.sort()
    index = 0
    while True:

        #Setp 1 biggest - i
        bigI = -1
        for i in range(0,len(nums)-1):
            if(nums[i] < nums[i+1]):
                bigI = i
        if(bigI == -1):
            #print("final")
            allPer.append(listToNum(nums))
            #print(nums)
            break
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

            allPer.append(listToNum(nums))
            index += 1
    return allPer

if __name__  == "__main__":

    primes = [2,3,5,7,11,13,17]
    lst = permutations()

    for i in range(0,len(lst)):
        for j in range(0,len(str(lst[i]))):

            number = str(lst[i])
            print(number)
            for k in range(0,len(number)):
                num = number[2+k:5+k]
                print(num)
