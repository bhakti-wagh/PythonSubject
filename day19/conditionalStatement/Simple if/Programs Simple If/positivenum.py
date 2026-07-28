#check Positive Number

'''
num=eval(input("Enter number:"))

if num>=0:
    print(f"{num} is positive")
'''
#check negative number
'''
num1=eval(input("Enter number:"))

if num1<0:
    print(f"{num1} is negative number")
'''
#check zero
'''
num3=eval(input("Enter number:"))

if num3==0:
    print(f"{num3} is zero")
'''

#Eligible to vote
'''
age=eval(input("Enter age :"))

if age>=18:
    print("You are Eligible to vote")
'''

#Driving License
'''
age=eval(input("Enter age:"))

if age>=21:
    print("You can make Driving License")
'''

#Pass student
'''
marks=eval(input("Enter your Marks:"))

if marks>35:
    print("you are pass ")
'''

#Salary Eligible
'''
sal=eval(input("Enter salary:"))

if sal>=10000:
    print("you are Eligible for loan")
'''

#Adult person
'''
age=eval(input("Enter your age:"))

if age>=18:
    print(f"{age} you are adult person")
'''

#Temperature check
'''
temp=eval(input("Enter temperature:"))

if temp>=35:
    print("too hot")'''


#ATM Balance
'''
bal=eval(input("Enter balance:"))

if bal>=0:
    print("sufficeint balance")
'''

#Even number
'''
even=eval(input("Enter number:"))

if even%2==0:
    print(f"{even} is even number")
'''

#odd number
'''
odd=eval(input("Enter number:"))

if (odd%2)!=0: #(odd&1)==1
    print(f"{odd} is odd number")
'''

#Divisible by 5
'''
num=eval(input("Enter number:"))

if num%5==0:
    print(f"{num} is divisible by 5")
'''
#Divisible by 10
'''
num1=eval(input("Enter number:"))

if num1%10==0:
    print(f"{num1} is divisible by 10")
    '''
#Divisible by 3
'''
num2=eval(input("Enter number:"))

if num2%3==0:
    print(f"{num2} is divisible by 3")
'''
#Multiple of  7
'''
num3=eval(input("Enter number:"))

if num3%7==0:
    print(f"{num3} is multiple by 7")
'''

#Check Leap Year
'''
year=eval(input("Enter year:"))

if year%4==0:
    print(f"{year} is leap year")
    
'''

#square greater than 100
'''
squ=eval(input("Enter number:"))

if (squ**2)>=100:
    print(f"{squ} square is greater than 100")
    print(squ**2)
'''

#cube greater tha 500
'''
cube=eval(input("Enter number:"))

if (cube**3)>=500:
    print(f"{cube} cube is greater than 500")
    print(cube**3)
'''

#number ends with zero
'''
num=eval(input("Enter number:"))

if num.endswith('0'):
    print(f"{num} ends with  zero")
'''


#Empty string
'''
string=eval(input("Enter string :"))

if ''==string:
    print("Empty string")
'''

#Name starts with A
'''
string=eval(input("Enter string:"))

if string.startswith('A'):
    print("Starts with A")
'''

#Name Ends with n
'''
string=eval(input("Enter string:"))

if string.endswith('n'):
    print("ends with n")
'''

#Length greater than 5
'''
string=eval(input("Enter string:"))

if len(string)>=5:
    print("string length is greater than 5")
'''

#check uppercase

'''
string=eval(input("Enter string:"))

if string.isupper():
    print(f"{string} in uppercase")
'''

#check lowercase
'''
string=eval(input("Enter string:"))

if string.islower():
    print(f"{string} in lowercase")
'''

#check alphabet only
'''
string=eval(input("Enter string:"))

if string.isalpha():
    print(f"{string} contain only alphabet")
'''

#check digits only
'''
num=eval(input("Enter number:"))

if num.isdigit():
    print(f"{num} is contain only digits")
'''

#check alphanumeric
'''
num=eval(input("Enter number:"))

if num.isalnum():
    print(f"{num} is alpha numeric")
'''
#check space
'''
num=eval(input("Enter number:"))

if num.isspace():
    print("space")
'''

#check list empty
'''
x=eval(input("Enter number:"))

if x==[]:
    print("list is empty")
'''

#check list length greater than 5
'''
x=eval(input("Enter number:"))

if len(x)>=5:
    print("list length greater than 5")
'''

#largest element greater than 100
'''
x=eval(input("Enter number:"))

if max(x)>=100:
    print(f"{max(x)} greater than 100")
'''

#smallest element less than 0
'''
x=eval(input("Enter number:"))

if min(x)<=0:
    print(f"{min(x)} less than 0")
'''

#sum greater than 500
'''
x=eval(input("Enter number:"))

if sum(x)>=500:
    print(f"{sum(x)} greater than 500")
'''

#wap to check age>18 and salary is greater than
#30000
'''
age=eval(input("Enter age:"))
salary=eval(input("Enter salary:"))

if age>=18 and salary>=30000:
    print("eligible")
    '''

#wap to match username and password match
'''
username=eval(input("Enter username:"))
password=eval(input("Enter password:"))

if (username=="admin")==(password==123):
    print("Match")
    
'''

#wap to check marks>35 and attendance>75
'''
marks=eval(input("Enter marks:"))
attendance=eval(input("Enter attendance:"))

if marks>=35 and attendance>=75:
    print("eligible")
'''

#wap to check given number even and positive
'''
num=eval(input("Enter number:"))

if num%2==0 and num>=0:
    print(f"{num} is even and positive")
'''

#wap to check given number between 1 and 100
'''
num=eval(input("Enter Number:"))

if num>=1 and num<=100:
    print(f"{num} is between 1 and 100")
'''

#wap to check given number Divisible by 3 and5
'''
num=eval(input("Enter number:"))

if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
'''
 
#wap to check given number divisibleby 2 or 7
'''
num=eval(input("Enter number:"))

if num%2==0 or num%7==0:
    print(f"{num} is divisible by 2 and 7")
    '''
#Wap to check name starts with A and Ends with a
'''
word=eval(input("Enter string:"))

if word.startswith('A') and word.endswith('a'):
    print("pass")

'''

#wap to check salary>50000 or Experience>5
'''
sal=eval(input("Enter salary:"))
exp=eval(input("Enter Experience:"))

if sal>50000 or exp>5:
    print("Eligible")
    '''
#wap to check temperature>35 and humidity>80
'''
temp=eval(input("Enter temperature:"))
humidity=eval(input("Enter humidity:"))

if temp>35 and humidity>80:
    print("temp and humidity")
'''

#wap to check if the student has scored 70%
#print good luck
'''
marks=eval(input("Enter marks:"))

if marks>=70:
    print("good luck")
'''

#wap to check which number is greater using if
'''
a=eval(input("Enter num:"))
b=eval(input("Enter num2:"))

if a>b or b>a:
    print(f"greater")
'''

#50.wap to check if the given string has even
#length of character

'''
s="hey guys you all are Osam"
print(len(s))
if len(s)%2==0:
    print("even")
'''

#wap to check if the givem number is divible by 5
'''
num=eval(input("Enter number:"))

if num%5==0:
    print("divisible by 5")

'''

#wap to check eligible to vote take user input age'
'''
age=eval(input("Enter age:")
if age>=18:
    print("eligible to vote")
'''
#wap to check if given number is positive
'''
num=eval(input("Enter number:"))

if num>0:
    print("number is positive")
'''

#wap to check if the given string is palindrome[

'''
word=eval(input("Enter word:"))

if word== word[::-1]:
    print("word is palindrome")

'''

#wap to check if the first letter in given string is consonant
'''
s="Lahari is good student"

if s in 'a e i o u A E I O U':
    print("consonant")
'''

#wap to check the given string is uppercase or not
'''
s=eval(input("Enter string"))

if s.upper():
    print("uppercse")

'''
#wap to display "python coding "if the number is greater than 1 and less than 5
'''
s=eval(input("Enter number"))

if s>1 and s<5:
    print("Python coding")

'''

#wap to check whether given number is negative and pring"its negative guys"
'''
num=eval(input("Enter number:"))

if num<0:
    print("negative guys")
'''

#wap to check whether given input is divisibley by 2 and 6 if condition is True, convert
#given number to complex
'''
num=eval(input("Enter number"))

if num%2==0:
    print(complex(num))
'''

#wap to check whether the given number is evern or not, if even store the value inside the list
'''
num=eval(input("Enter number:"))
k=[]

if num%2==0:
    k.append(num)
    print(k)
'''

#.wap to check whether a given value is divisible by 5
#and 7,if the value is divisible then display
#the square of the values (take user input)
'''
num=eval(input("Enter number:"))

if num%7==0:
    print(num**2)
'''

#wap to check whether a given value is present in between 45 and 200
#and the number should be divisible by 4 and 5
#,if satisfied, display the ascii characters (take user input)
'''
num=eval(input("Enter number:"))

if (num%4==0 and num%5==0) and (num>45 and num<200):
    print(chr(num))
'''

#wap to checking if a string contaisn a substring
'''
string = "hello world"
substring = "world"

if substring in string:
    print(f'"{substring}" is present in the string.')
'''

#Write a program to check if a string ends with a period ('.').
'''
string = input("Enter a string: ")

if string.endswith("."):
    print("The string ends with a period.")
    
'''

#Write a program to check if 'a' is present in the string s = 'apple'.

s = "apple"

if "a" in s:
    print("'a' is present in the string.")

# Write a program to check if the first and last characters of a string are the same (e.g., x = 'level').
'''
x = "level"

if x[0] == x[-1]:
    print("The first and last characters are the same.")

'''

#. WAP to check if a character is a vowel.
