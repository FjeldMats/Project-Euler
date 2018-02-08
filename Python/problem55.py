# (i) number below 10 000 and has to be a palindrom in less than 50 iterations
# (ii) 10677 is the only palindrome to require over 50 iterations

def isPalindromic(n):
    strN = str(n)
    lstN = list(strN)
    if(len(lstN) % 2 == 0):
        half = len(lstN) / 2

        first = lstN[0:half]
        last = lstN[half:len(lstN)]
        print(first,last.reverse())
    else:
        half = int(len(lstN) / 2)

        first = lstN[0:half]
        last = lstN[half+1:len(lstN)]
        print(first,last)



def main():
    isPalindromic(123321)

main()
