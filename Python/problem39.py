#Integer right triangles

index = 0
big = 0
bP = 0
for p in range(0,1001):
    setOfNums = set()

    for i in range(1,p):
        for j in range(1,p):
            for k in range(1,p):
                nums = [i,j,k]
                nums.sort()
                if(nums[0]**2 + nums[1]**2 == nums[2]**2 and i+j+k == p):
                    SET = frozenset({i,j,k})
                    setOfNums.add(SET)

        print(len(setOfNums))
        if len(setOfNums) > big:
            big = len(setOfNums)
            bP = i

print(bP)
