
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
'''
num1=eval(input("Enter 1st num:"))

num2=eval(input("Enter 2nd num:"))

if num1==num2:
    print(num1*num2)
else:
    print(num1//num2)
'''

#wap to find the largest of two numbers
'''
num1=eval(input("Enter num 1:"))

num2=eval(input("Enter num 2:"))

if num1>num2:
    print(f"{num1} is largest number")
else:
    print(f"{num2} is largest ")
'''

#wap to check whether input num is greater than 10 or not
#If it greater than 10 print messages as greater with number.
#IF it is not a greater than 10 print that number
'''
num=eval(input("Enter number:"))

if num>=10:
    print(f"{num} is greater")
else:
    print(f"{num} is not greater than 10")
'''

#wap to the given num integer if n is greater than 21 , print the
#Absolute difference between n and 21.
#Otherwise print twice the absolute difference
'''
n=eval(input("Enter number:"))

'''

#wap to find smallest of two numbers
'''
num1=eval(input("Enter num 1:"))

num2=eval(input("Enter num 2:"))

if num1<num2:
    print(f"{num1} is smallest number")

else:
    print(f"{num2} is smallest number")

'''


#wap to check whether the given input is divisible by 3 or not if yes
#if yes print the number or else print cube of number
'''
num=eval(input("Enter number:"))

if num%3==0:
    print(num)
else:
    print(num**3)

'''

#wap to check whether the given number is even or odd
#If it is even then make it as an odd number if it
#is an odd number then make it as even number
'''
num=eval(input("Enter number:"))

if num%2==0:
    print(num+1)
else:
    print(num)
'''

#wap to check whether the given input is divisible by 3 and 5 . if yes
#Print the actual number or else print string of that number
'''
num=eval(input("Enter number:"))

if num%3==0 and num%5==0:
    print(num)
else:
    print(str(num))
'''

#wap to check whether the given number lies between 1 and 19.
#if it is true square that number or else false cube that number and display the  number
'''
num=eval(input("Enter number:"))

if num>=1 and num<=19:
    print(num**2)
else:
    print(f"{num} and cube of number is",num**3)
'''

#wap to check whether the student has passed or failed.
#If the student got more than 40 marks print 'pass' along with those marks
#If it is not printed Fail along with marks

marks=eval(input("Enter marks:"))

if marks>=40:
    print(f"{marks} you are pass")
else:
    print(f"{marks} you are Fail")
