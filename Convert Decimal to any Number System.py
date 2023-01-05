decimal = int(input("Enter decimal value :\n"))
convert = int(input('''1 - fro binary
2 - for octal 
3 - for hexadecimal : \n'''))

if convert == 1:
    print("Converted to Binary \n" , bin(decimal))

elif convert == 2:
    print("Converted to Octal \n" , oct(decimal))

elif convert == 3:
    print("Converted to Hexadecimal \n" , hex(decimal))

else:
    print("Review Your Input")

