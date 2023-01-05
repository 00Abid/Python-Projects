def Func(x):
    if x==1:
        return 1
    else:
        return (x*Func(x-1))


x = int(input("Enter Factorial Number:\n"))
print(f'Factorial of  {x} is {Func(x)}')