sum = 0
while True :
    user_input = input("Enter item amount or Press q to quit :\n")
    if user_input != "q":
        sum = sum+int(user_input)
        print(f'order total so farr {sum}')

    else:
        print(f'Your bill total is {sum} .  Thanks for Shopping with us !')
        break