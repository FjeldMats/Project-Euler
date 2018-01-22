from num2words import num2words

count = 0
for i in range(1,1001):
    string = num2words(i)
    #cprint(string)

    for j in range(0,len(string)):

        if(string[j].isalpha()):
            count += 1

print(count)
