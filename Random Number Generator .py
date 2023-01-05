import random
r = random.randint(1,5)

while True:
    a = int(input("Enter Number : \n"))

    if a>r:
        print("The NUmber is too great")
    elif a<r:
        print("The Number is too small")
    else:
        print("Congrats You Wonn , Hurray !")
        break
