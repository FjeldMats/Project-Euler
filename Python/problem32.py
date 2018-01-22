import math

def isSquare(N):
    root = math.sqrt(N)
    if int(root + 0.5) **2 == N:
        return True
    else:
        return False

def fermatFactor(N):
    a = int(math.ceil(math.sqrt(N)))
    b2 = a**2 - N

    grense = math.ceil(math.sqrt(N))
    while isSquare(b2):
        a += 1
        b2 = a**2 - N
    fac1 = int(a - math.sqrt(b2))
    fac2 = int(a + math.sqrt(b2))
    facs = [fac1,fac2]
    return facs

def isPandigital9(N):
    strNum = str(N)

    nums = set()

    for i in range(1, 10): #legg alle tall fra  1 - n i nums
        nums.add(str(i))

    for i in range(0, len(strNum)):
        if strNum[i] in nums:
            nums.remove(strNum[i])
        else:
            nums.add(strNum[i])

    #print(N)
    #print(nums)
    if(len(nums) == 0):
        return True
    else:
        return False


if __name__ == "__main__":

    panSet = set()
    for i in range(1,10000):
        #print(i)
        fs = fermatFactor(i)
        panNum = str(fs[0]) + str(fs[1]) + str(i)
        print(fs[0],fs[1],i)
        if(isPandigital9(panNum)):
            print(fs[0],fs[1],i)
            panSet.add(i)
    print(panSet)
    print(len(panSet))
    print(sum(panSet))
