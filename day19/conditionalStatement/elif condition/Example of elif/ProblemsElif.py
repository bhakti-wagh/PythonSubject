# wap to check the given character is alphabet or digit or special characters

'''
char=eval(input("Enter character:"))

if char.isalpha():
    print(f"{char} is alphabet")

elif char.isdigit():
    print(f"{char} is digit")

else:
    print(f"{char} is special character")
'''

#wap to check the given number is +ve or -ve or neutral
'''
num=eval(input("Enter number:"))

if num>0:
    print(f"{num} is positive number")

elif num<0:
    print(f"{num} is negative number")

elif num==0:
    print(f"{num} is neutral ")
'''


#wap to check the given character is uppercase or lowercase or digit 
'''
char=eval(input("Enter character:"))

if char.isupper():
    print(f"{char} is uppercase")

elif char.isdigit():
    print(f"{char} is digit")

elif char.islower():
    print(f"{char} is lowercase")

'''
##wap to check the given character is uppercase or lowercase or digit without inbuilt function
'''
x=eval(input("Enter the character:"))

if ord("A")<=ord(x)<=ord("Z"):
    print("uppercase")

elif ord('a')<=ord(x)<=ord("z"):
    print("lowercase")

elif ord('0')<=ord(x)<=ord('9'):
    print("digit")

'''
