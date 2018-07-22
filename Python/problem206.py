def uniqeSquare(n):
    lenN = len(str(n))
    lst = list(map(int,list(str(n))))
    _ = None
    nums = [1,_,2,_,3,_,4,_,5,_,6,_,7,_,8,_,9,_,0]
    for i in range(0,len(nums)):
        if(lst[i] != nums[i] and not nums[i] == None):
            return False
    return True

for i in range(1000000000,10000000000):
    if(uniqeSquare(i**2)):
        print(i)
        break
