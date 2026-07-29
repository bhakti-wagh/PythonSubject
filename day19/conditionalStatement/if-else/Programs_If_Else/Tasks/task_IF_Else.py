
#wap to check whether a number is positve or negative
# if positive print message or else print negaitve number
'''
num=eval(input("Enterd number:"))

if num>=0:
    print("positive number")

else:
    print("negative number")
'''

#wap to check whethe a no is even or odd. if even
#Print message an even or else print msg odd
'''
num=eval(input("Enter number:"))

if num%2==0:
    print(f"{num} is Even number")

else:
    print(f"{num} is Odd number")
'''

#wap to check whether a given number is greater than 10 or not
#if it is greater than 10 print mesg as greater or else print
#than number with not greater than
'''
num=eval(input("Entered number:"))

if num>=10:
    print("Greater")
else:
    print(f"{num} is not greater than")
'''

#wap to check a given two input numbers are divisible by 3 and 5.
#if it is divisble print("Good Morning"), if it is not divisible print("Good Evening")

'''
num=eval(input("Enter number:"))

if num%3==0 and num%5==0:
    print("Good Morning")

else:
    print("Good Evening")
'''

#Wap to accept two integers and check whether those two values are equal or not
#if equal , multiply to value or else to display quotation value

num1=eval(input("Enter 1st num:"))

num2=eval(input("Enter 2nd num:"))

if num1==num2:
    print(num1*num2)
else:
    print(num1//num2)
