#pandigital prime (41)

def isPrime(n):
    limit = int(abs(n)**(1/2)+1)
    if(n == 1):
        return False
    for i in range(2,limit):
        if n % i == 0:
            return False
    else:
        return True

def listToNum(listOfNums):
    strNumber = ''
    for i in range(0,len(listOfNums)):
        strNumber += str(listOfNums[i])
    return int(strNumber)

def permutations(num):
    allPer = []
    nums = list(str(num))
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
    lst = permutations(1234567)

    for i in range(0,len(lst)):
        if( isPrime(lst[i]) == True):
            print(lst[i])
