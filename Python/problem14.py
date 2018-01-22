# Longest Collatz sequence

# find the Longest collatz sequence which starts under - 1 000 000
#  *The chain is allowed to go above one million


# n --> n/2 (if n is even)
# n --> 3n + 1 (if n is odd)

from datetime import datetime
start=datetime.now()

million = 1000000
longest = 1
longestNum = 0
for i in range(1,million):
    n = i
    count = 0
    while n != 1:
        if(n % 2 == 0):
            n /= 2
            #print(n)
        else:
            n = 3*n +1
            #print(n)
        count += 1
    if(count>longest):
        longest = count
        longestNum = i
    #print(i,"has",count,"sequenceses")

print("-----")
print("The longest sequence starts at",longestNum,"and has",longest,"sequenceses")

print(datetime.now()-start)
