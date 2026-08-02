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
'''
x=eval(input("Enter number:"))
y=eval(input("Enter sec number:"))
z=eval(input("Enter thr number:"))

if x<y and x<z:
    print(f"{x} is smallest")

elif y<x and y<z:
    print(f"{y} is smallest")

else:
    print(f"{z} is smallest")

'''


#wap to check according to age eligiblity of marriage
'''
age=eval(input("Enter age:"))

if age<17:
    print("child Marriage")

elif age==18:
    print("Eligible ")

elif 18<=age<=25:
    print("Love M")

elif 25<=age<=30:
    print("Arrange M")
    
elif 30<=age<=40:
    print("Yourwish")
'''


#wap to check data is sequence/iterable/individual

'''
a=eval(input("Enter data:"))

if isinstance(a,(str,list,tuple)):
    print("Its sequence data type")

elif isinstance(a,(str,list,set,tuple,dict)):
    print("Its Iterable data type")

elif isinstance(a,(int,float,complex,bool)):
    print("Its Individual data type")

else:
    print("Invalid data")
'''


#.wap if input is string return its length,else if input is list pop element,else
# if input is tuple reverse else invalid input
'''
a=eval(input("Enter data:"))

if isinstance(a,str):
    print("length of string:",len(a))

elif isinstance(a,list):
    a.pop()
    print(a)

elif isinstance(a,tuple):
    print(a[::-1])

else:
    print("Invalid input")
'''

#wap to check a age belongs to category 0 to 17 child and 18 to 30 ur adult,
#31 to 60 ur men,
#61 to 100 senior citizen,else
 #invalid

'''
a=eval(input("Enter age:"))

if 0<=a<=17:
    print("Child")

elif 18<=a<=30:
    print("You are adult")

elif 31<=a<=60:
    print("You are men")

elif 61<=a<=100:
    print("senior citizen")


else:
    print("Invalid")
'''



#wap to take marks of 5 sub,calculate the average if the average is b/w 90-100
#print Distinction
#if 75-89 print first class and
#if it's 60-74 print second class, if 50-59 print Third class,below 50 is fail
#note:-->max marks is 100
'''
math=eval(input("Enter math marks:"))
sci=eval(input("Enter sci marks:"))
eng=eval(input("Enter eng marks:"))
hist=eval(input("Enter hist marks:"))
geo=eval(input("Enter geo marks:"))

avg=(math+sci+eng+hist+geo)/5
print(avg)

if 90<=avg<=100:
    print("Distinction")

elif 75<=avg<=89:
    print("First Class")
elif 60<=avg<=74:
    print("Second class")

elif 50<=avg<=59:
    print("Third class")

else:
    print("Fail")
'''


#consider a character input if it is uppercase convert it into lowercase
#if it is lower-> upper if it is digit print remiander when it is
#divided by 3 else if it is spceial character prints its acii value
'''
ch=eval(input("Enter character:"))

if 'A' <= ch <= 'Z':
    print("Lowercase:", ch.lower())
2
elif 'a' <= ch <= 'z':
    print("Uppercase:", ch.upper())

elif '0' <= ch <= '9':
    print("Remainder:", int(ch) % 3)


else:
    print(ord(ch))


'''



num=eval(input("Enter number:"))

if num%3==0:
    print("Fizz")

elif num%5==0:
    print("buzz")

elif num%3==0 and num%5==0:
    print("Fizzbuzz")
