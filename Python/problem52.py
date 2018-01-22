def permutedMult(n):
    tall = makeLists(n)

    #sjekker alle tallene har lik lengde
    for i in range(0,len(tall)):
        if(len(tall[i] == len(tall[0])):
            continue
        else:
            return False
    else:

        for i in range(0,len(tall)):
            for j in range(0, len(tall)):
                if(tall[0][j] in tall[i]):
                    continue
                else:
                    return False

def makeLists(n):
    multiples = []
    for i in range(1,7):
        strN = str(n*i)
        listN = list(strN)
        multiples.append(listN)
    return multiples


def main():
    print(makeLists(125874))

main()
