Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


#Identity Operator:->
#It will check whether the memory address of given operands are same or not
#there are 2 type of Identity operator:
#1.is operator
#2. is not operator

#1.is operator:-> it will give the result as same only if address of operands's are having  same address
#Syntax: -> operand1 is operand2

a=10
b=10

a is b
True

a=10.5

>>> a is b
False
>>> 
>>> 
>>> f=[35]
>>> g=f.copy()
>>> 
>>> f is g
False
>>> 
>>> 
>>> #1.is not operator:-> it will give the result as same only if address of operands's are  different
>>> #Syntax:-> op1 is not op2
>>> 
>>> a is not b
True
>>> 
>>> f is not g
True
>>> 
>>> c=10
>>> d=10
>>> c is not d
False
>>> 
