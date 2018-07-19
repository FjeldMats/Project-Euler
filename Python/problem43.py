import random
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of
the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
def randomPandigital():
    listOfNumbers = []
    for i in range(0,10):
        listOfNumbers.append(i)
    random.shuffle(listOfNumbers)
    return ''.join(map(str, listOfNumbers))


def subStringDiv(pandigitalNum):
    #print pandigitalNum
    listOfNumbers = list(map(int, pandigitalNum))

    returnBool = True

    divs = [2, 3, 5, 7, 11 ,13, 17]

    count = 2
    for i in range(0, len(divs)):

        divNum = []
        for j in range(0,3):
            #print count

            divNum.append(listOfNumbers[count-1])
            count = count + 1
        count = count - 2

        #print str(divNum ) + " % " + str(divs[i])


        if(int(''.join(map(str, divNum))) % divs[i] != 0):
            returnBool = False
            #print "FALSE"

        #print " "

    #print returnBool
    return returnBool

#print subStringDiv(randomPandigital())

#print subStringDiv("1406357289")


foundAllNums = False
SET = set()
awnserList = set()
while not foundAllNums:
    if(len(SET) == 3628800):
        foundAllNums = True
    if((len(SET) % 10 == 0) and len(SET) > 3600000):
        print str(len(SET)) +  "/3628800"
    num = randomPandigital()
    SET.add(num)
    if(subStringDiv(num)):
        print str(num) + ' ('+str(len(SET))+')'
        awnserList.add(num)


print "DONE \n"
print sum(list(map(int, awnserList)))
