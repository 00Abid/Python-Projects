a = int(input("Enter number :\n"))
b = int(input("Enter number :\n"))

maxNum = max(a,b)

while True:
    if (maxNum%a==0 and maxNum%b==0):
        break
    maxNum +=1

print(f'The LCM of {a} and {b} is {maxNum}')