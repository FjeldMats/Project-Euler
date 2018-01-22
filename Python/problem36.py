def isPalindromic(num):
    strNum = str(num)
    length = len(strNum)
    if( len(strNum) % 2 == 0 ):
        Hlength = int(length/2)

        firstHalf = strNum[0:Hlength]
        secHalf = strNum[Hlength:length]

        if(firstHalf == secHalf[::-1]):
            return True

        else:
            return False


    else:
        Hlength = int((length+1)/2)

        firstHalf = strNum[0:Hlength]
        secHalf = strNum[Hlength-1:length]

        if(firstHalf == secHalf[::-1]):
            return True

        else:
            return False

if __name__ == "__main__":
    SUM = 0
    for num in range(1,1000001):
        binNum = bin(num)[2:]

        palDes = isPalindromic(num)
        palBin = isPalindromic(binNum)

        if(palDes == True and palBin == True):
            print(num,binNum, palDes, palBin)
            SUM += num

    print(SUM)
