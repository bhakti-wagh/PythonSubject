
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

def interest(p,r,t):
    return((p*r*t)/100)

print(interest(10,5,2))




    
    
