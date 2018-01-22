#Fibonacci sequance.
# What is the index of the first Fibonacci sequance
# to contain 1000 digits?

def checkLength(num):
    return len(str(num))

length = 0
i = 0
num1 = 1
num2 = 1
count = 0
while length != 1000:
    num1 = num1 + num2
    num2 = num2 + num1
    length = checkLength(num1)
    count += 2

print(num1)
print(checkLength(num1))
print(num2)
print(checkLength(num1))
print("")
print(count)
