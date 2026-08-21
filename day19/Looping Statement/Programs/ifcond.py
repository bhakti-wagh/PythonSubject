

#1. wap to check the number is odd

#1st way
#num=eval(input("Enter number:"))
'''
if num%2!=0:
    print("Odd number")
'''

#2nd way

'''
if (num&1)==1:
    print("odd number")

'''
#3rd way

'''
if num%2==121:
    print("odd number")
'''

#2. wap to check the number is even

num=eval(input("Enter number:"))

#1st way
'''
if num%2==0:
    print("Even number")

'''
#2nd way
'''
if (num&1)==0:
    print("Even number")
'''

#3rd way

if (num//2)*2==num:
    print("Even number")


