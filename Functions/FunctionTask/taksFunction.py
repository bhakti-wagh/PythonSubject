
'''
1. Greeting Function
Write a function that takes a name and prints:
Hello Amit
'''
'''
def greet(name):

    print("Hello",name)

greet("Amit")
'''
#o/p :Hello Amit


'''
2. Add Two Numbers
Write a function that takes two numbers and returns their sum.
Input: 10, 20
Output: 30

'''

'''
def sumN():
    a=10
    b=20
    return a+b

new=sumN()
print(new)

#o/p: 30
'''

'''
3. Find Difference
Write a function that accepts two numbers and returns their difference.
'''
'''
def diff():
    num=eval(input("Enter number:"))
    num1=eval(input("Enter number2:"))
    dif=num-num1

    return dif

NoDiff=diff()

print(NoDiff)

'''

'''
4. Find Maximum
Write a function that accepts two numbers and returns the greater number.

'''
'''
def maxi():
    num1=eval(input("Enter number:"))
    num2=eval(input("Enter number2:"))

    if num1>num2:
        print(f"greater number is num1:{num1}")
    else:
        print(f"greater number is num2:{num2}")

maxi()

'''
'''
5. Find Minimum
Write a function that accepts two numbers and returns the smaller number.
'''
'''
def mini():
    num1=eval(input("Enter number:"))
    num2=eval(input("Enter number2:"))

    if num1<num2:
        print(f"smaller number is num1:{num1}")
    else:
        print(f"smaller number is num2:{num2}")

mini()

'''

'''
6. Check Even or Odd
Write a function that accepts a number and returns "Even" or "Odd".

'''
'''
def check():
    num=eval(input("Enter number:"))

    if num%2==0:
        print("Even number")
    else:
        print("odd number")

check()
'''
'''
7. Check Positive, Negative or Zero
Write a function that accepts a number and returns:
Positive
Negative
Zero
'''
'''
def check():
    num=eval(input("Enter nu"))
'''

'''
12. Calculate Area of Rectangle
Write a function that accepts length and breadth and returns the area.
Area = length × breadth

'''
'''

def area():
    l=int(input("Enter length:"))
    b=int(input("Enter breadth:"))

    return l*b

print(area())


def area1(l,b):
    print("Area of rectangle:",l*b)

area1(10,20)


def area1():
    l=int(input("Enter lenght:"))
    b=int(input("Enter breadth:"))
    print("Area of rectangle:",l*b)

area1()
'''


'''
13. Calculate Simple Interest
Write a function that accepts:
principal
rate
time
and returns simple interest.
SI = (P × R × T) / 100

'''

'''
def interest(p,r,t):
    return((p*r*t)/100)

print(interest(10,5,2))

'''


'''
14. Find Average of Three Numbers
Write a function that accepts three numbers and returns their average.

'''
'''
def avg(a,b,c):
    return (a+b+c)/3

print(avg(10,20,30)) #20.0
'''
    
'''
15.Count Vowels
Write a function that accepts a string and returns the number of vowels.
Input: "education"
Output: 5
'''

'''
def vowel(s):
    count=0
    for i in s:
        if i in 'AEIOUaeiou':
            count+=1
    print(count)

vowel("education")

#o/p:5
'''

'''

16.Count Consonants
Write a function that accepts a string and returns the number of consonants.

'''
'''
def cons(s):
    count=0
    for i in s:
        if i not in 'AEIOUaeiou':
            count+=1
            print(i)
            
    print(count)

cons("education")

#o/p:4

'''

'''
17. Count Digits in a String
Write a function that accepts a string and counts how many digits are present.
Input: "abc123xy5"
Output: 4

'''
'''
def check(d):
    count=0

    for i in d:
        if not i.isalpha():
            count+=1

    print(count)

check("abc123xy5") #4
 '''           

#If i want to sum of digit then
#count=count+int(i)

'''
18.. Reverse a String
Write a function that accepts a string and returns the reversed string.
Input: "python"
Output: "nohtyp"
'''
'''
def rev(s):

    print(s[::-1])

rev("python")

'''
'''
19.Return Only Positive Numbers
Write a function that accepts a list and returns a new list containing only positive numbers.
a = [10, -5, 20, -2, 30]
'''
'''
def check():
    a = [10, -5, 20, -2, 30]
    p=[]

    for i in a:
        if i>0:
            p.append(i)
    return p

print(check())
  '''  


'''
20.wap to perform addition and subtraction
if "a" is greater than "b" return sum else
return difference
'''
'''
def addsub(a,b):   

    if a>b:
        
        return a+b
    else:
        return a-b

print(addsub(20,10)) #30
print(addsub(100,500)) #-400
    
'''        
    

'''
21.waf to check string is palindrome or not
(take user input)
'''
'''
def palindrome():
    val=eval(input("Enter string:"))

    if val==val[::-1]:
        return True,a
    else:
        return False,a
print(palindrome()) 
'''

'''
22.wap to return length of variable
keywords arguments

'''
'''
def length_data(**kargs):
    length=0
    for i in kargs:
        print(i)
        length+=1
    print(length)

length_data(a=10,b=20,c=30,d=[1,2,3,4])
'''
'''
o/p:
a
b
c
d
4
'''



'''
23.wap to return length of the variable
positional arguments

'''

'''
def length_data(*args):
    length=0
    for i in args:
        print(i)
        length+=1
    print(length)

length_data(10,20,30,[1,2,3,4])
'''
'''
o/p:
10
20
30
[1, 2, 3, 4]
4
'''



'''
24.wat to search for character in a given
string and return corresponding index
  string="coding part is done"
'''

'''
def search(s):
    st=eval(input("Enter a string:"))

    for i in range(len(s)):

        if s[i]==st:
            print(i,st)
    return "substring is not found"

search("coding part is done")

'''     


'''
25.wap to squaring of the element in the
given list
l=[1,2,3,4,5]
'''
'''
def sqa(l):

    for i in l:
        print(i**2)

sqa([1,2,3,4,5])
'''
#o/p:  1
#      4
#      9
#      16
#      25
    
'''
26.wap to fetch last digit number
'''
'''
def fetch():
    num=eval(input("Enter number:"))

    return num%10

print(fetch())
'''

'''
27.wap to read 3 numbers from the user,first
two numbers should be added and the result of
addition should be subtracted by third number
'''
'''
def operation():
    a=eval(input("Enter number 1:"))
    b=eval(input("Enter number 2:"))
    c=eval(input("Enter number 3:"))

    sum= a+b

    print("Addition is:",sum)


    result = sum-c

    return "Result is:",result

print(operation())

'''


'''
28.wap to find square,cube,square root and
cube
root of a number


square root=0.5 or 1/2
cube root = 1/3
'''

'''
def  operation(num):
    return num**2,num**3,num**(1/2),num**(1/3)

print(operation(16))


#OR

import math

def operation2(num1):
    return num1**2,num1**3,math.sqrt(num1),math.cbrt(num1)

print(operation2(16))

'''


'''
29.wap to check the given characters is
alphabets or digit or special characters

'''
'''
def check():
    chara=eval(input("Enter characters:"))

    if chara.isalpha():
        print("alphabet")
    elif chara.isdigit():
        print("digit")
    else:
        print("special character")

check()

#OR

def check2():
    char=eval(input("Enter character:"))

    if 'A'<=char<='Z' or 'a'<=char<='z':
        print("Alphabet")
    elif '0'<=char<='9':
        print("Digit")
    else:
        print("special character")

check2()
'''

'''
30.wap to check given iterable is a sequence,
if it is a sequence reverse it,if not add
one extra element to the iterable
'''
'''
def iterable(num):

    if isinstance(num,(list,tuple,str)):
        print(num[::-1])
    else:
        print("Its not sequence")
        iterable.add(10)
        print(iterable)
        
iterable([3,7,9,5,{4,1,2},"dslfj"])
'''

'''
31.write a function to print the below output
func("TRACXN",1)
#should print RCN
'''

'''
def demo(value): #n for index part

    for i in range(1,len(value),2):
        print(value[i],end=" ")

demo("TRACXN")

''' # RCN

'''
32.write a function to print the below output
func("TRACXN",0)
#should print TAX
'''
'''
def demo(value,n): #n for index part

    for i in range(n,len(value),2):
        print(value[i],end=" ")

demo("TRACXN",0)
''' #TAX


'''
33.A function take variable number of positional arguments
as input. how to check if the arguments
are more than 5.
'''

'''
def check(*args):

    if len(args)> 5:
        print("length is Greater than 5")
        
check(1,2,3,4,5,6)
'''


'''
34.wat to return a dictionary with characters
and ascii value pair

'''

'''
def operation(char):
    d={}
    d.update({char:ord(char)})
    return d
print(operation('A'))

#o/p: {'A':65}

'''


'''
35.waf to reverse a iterable if you are
passing string or list or tuple else print
type of the data

'''

'''
def iter(num):
    if isinstance(num,(list,str,tuple)):
        print(num[::-1])
    else:
        print(type(num))

iter({4,7,8})
iter(["abc",34,'ah'])

#o/p: <class 'set'>
# ['ah', 34, 'abc']

'''


'''
36.wap to check if a given character is
alphabet or digit or special character
(without using inbuilt function).
'''
'''
def check2():
    char=eval(input("Enter character:"))

    if 'A'<=char<='Z' or 'a'<=char<='z':
        print("Alphabet")
    elif '0'<=char<='9':
        print("Digit")
    else:
        print("special character")

check2()
check2()
check2()

#o/p:  Enter character:'x'
#        Alphabet
#      Enter character:'8'
#        Digit
#      Enter character:'*'
#        special character
'''

'''
37.wap to return length of an iterable
without using len() function

'''
'''
def iter(value):

    length=0

    for i in value:
        length=length+1

    return length

print(iter([1,2,3,4,5]))
'''

'''
38.wap to count the number of arguments
passed inside the function call(both
positional and keyword)

'''

def check(*args,**kwargs):
    posticount=len(args)
    keyword=len(kwargs)

    print("Positional argument:",posticount)
    print("Keyword argument:",keyword)

check(10,20,c=60,d=90,e=80)
    
#o/p: Positional argument: 2
#     Keyword argument: 3




