# wap to check the given character is alphabet or digit or special characters
#wap to check the given number is +ve or -ve or neutral

char=eval(input("Enter character:"))

if char.isalpha():
    print(f"{char} is alphabet")

elif char.isdigit():
    print(f"{char} is alphabet")

else:
    print(f"{char} is special character")



num=eval(input("Enter number:"))

if num>0:
    print(f"{num} is positive number")

elif num<0:
    print(f"{num} is negative number")

elif num==0:
    print(f"{num} is neutral ")
