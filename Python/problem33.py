#Digit cancelling fractions 33

def cancelling(n,t):
    n2 = str(n)
    n2 = list(n2)
    t2 = str(t)
    t2 = list(t2)

    for i in range(0,2):
        for j in range(0,2):
            if(n2[i] == t2[j] and n != 0 and  n2[i] != str(0) and t2[j]  != str(0)):

                n2.remove(n2[i])
                t2.remove(t2[j])
                print(t2[0],n2[0])
                if(n != 0 and float(t2[0]) / float(n2[0]) == float(t)/float(n)):
                    return t2[0], n2[0]
                else:
                    return 0
    return 0

for n in range(11,100):
    for t  in range(11,100):
        if(n>t):
            print(cancelling(t,n))
            #print(str(n)+ ' / ' + str(t))
