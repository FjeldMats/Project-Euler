from itertools import product
from string import ascii_lowercase
def decode(key):
    data = open("cipher.txt").read().replace('\n', '').split(',')
    text = ""

    while len(key)<len(data):
        key += key

    for i in range(len(data)):
        text += chr(int(data[i])^ord(key[i]))

    return text

def sumOASCII(text):
    return sum(map(ord,( map(str,text))))

msg = []

for key in [''.join(i) for i in product(ascii_lowercase, repeat = 3)]:
    text = decode(key)
    if "The" in text:
        print("sum: " + str(sumOASCII(text))+ " " + key +  ": " + text + "\n")
