def FiboIterate(n):
    PrevNum = 0
    CurrentNum = 1
    for i in range (1,n):
        prePrevNum = PrevNum
        PrevNum = CurrentNum
        CurrentNum = prePrevNum+PrevNum
    return CurrentNum

num = int(input("Enter number :\n"))
print(f'Value of Fibo is {num} is {FiboIterate(num)}')