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


#based on the number i want to print day name
'''
day=eval(input("Enter number:"))

if day==1:
    print("Monday")

elif day==2:
    print("Tuesday")

elif day==3:
    print("Wensday")

elif day==4:
    print("Thrusday")

elif day==5:
    print("Friday")

elif day==6:
    print("Saturday")

elif day==7:
    print("Sunday")

else:
    print("Invalid day")
'''


#based on the symbol i want to perform operation[
'''
sym=eval(input("Enter symbol:"))

a=eval(input("Enter number:"))
b=eval(input("Enter number2 :"))


if sym=='+':
    print("sum is :",a+b)

elif sym=='-':
    print("substraction is:",a-b)

elif sym=='*':
    print("multiplication is:",a*b)

elif sym=='/':
    print("division is:",a/b)

elif sym=='//':
    print(" floor -division is:",a//b)

elif sym=='%':
    print("remainder is:",a%b)

else:
    print("different data")
'''


#among three vairable largest number
'''
x=eval(input("Enter number:"))
y=eval(input("Enter sec number:"))
z=eval(input("Enter thr number:"))

if x>y and x>z:
    print(f"{x} is largest")

elif y>x and y>z:
    print(f"{y} is largest")

else:
    print(f"{z} is largest")
'''

#among  three vairable smallest number

x=eval(input("Enter number:"))
y=eval(input("Enter sec number:"))
z=eval(input("Enter thr number:"))

if x<y and x<z:
    print(f"{x} is smallest")

elif y<x and y<z:
    print(f"{y} is smallest")

else:
    print(f"{z} is smallest")
