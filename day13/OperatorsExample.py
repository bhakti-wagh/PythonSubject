Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

# Arithmatic Operator

#1.Addition opration:->

x=5
y=10

x+y
15

[2,3,4]+[7,6,8]
[2, 3, 4, 7, 6, 8]


(6,4)+(7,8)
(6, 4, 7, 8)

#For collection data type it will give concatination as response

(3+2j)+(4+8J)
(7+10j)


#for set and dict it will not work
{3,4,5}+{4,5,6}
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    {3,4,5}+{4,5,6}
TypeError: unsupported operand type(s) for +: 'set' and 'set'

{3:30}+{4:40}
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    {3:30}+{4:40}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'


[8,9]+(8,9)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    [8,9]+(8,9)
TypeError: can only concatenate list (not "tuple") to list

#two different collection data type it will't work



>>> #Substraction operation :->
>>> 
>>> 45-18
27
>>> 
>>> True-False
1
>>> 
>>> 45.6-85.6
-39.99999999999999
>>> 
>>> 'hiiii'-'hii' #substraction operation don't support concatination
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    'hiiii'-'hii' #substraction operation don't support concatination
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> 
>>> # list ,tuple data type also not support to substraction operation
>>> 
>>> {45,18,7}-{10,7,19}
{18, 45}
>>> #in set 1 is result if any common element the it will remove and set1 result
>>> 
>>> {'hi','hello'}-{'Good','Morning'}#always set1 is result
{'hello', 'hi'}
>>> 
>>> 1*1
1

45.8*35.6
1630.48

(2+4j)*(4+5j)_
SyntaxError: invalid syntax
(2+4j)*(4+5j)
(-12+26j)

True*False
0

'hi'*'bye'
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    'hi'*'bye'
TypeError: can't multiply sequence by non-int of type 'str'

'hi'*2
'hihi'

[10,40]*[40,30]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    [10,40]*[40,30]
TypeError: can't multiply sequence by non-int of type 'list'

[10,40]*2
[10, 40, 10, 40]


(10,30)*2
(10, 30, 10, 30)

{10,20}*2
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    {10,20}*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'

{10:2}*2
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    {10:2}*2
TypeError: unsupported operand type(s) for *: 'dict' and 'int'



#Division

18/4
4.5

35.7/2
17.85

(3+2j)/(6+2j)
(0.5499999999999999+0.15j)

18//4
4
#Only integer part it will show

18%4
2


'hi'/'hii'
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    'hi'/'hii'
TypeError: unsupported operand type(s) for /: 'str' and 'str'
[34,56]/[87,90]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    [34,56]/[87,90]
TypeError: unsupported operand type(s) for /: 'list' and 'list'
(34,56)/(87,90)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    (34,56)/(87,90)
TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'

#Not support for string,list,tuple,set,dict


6**3
216

2**2
4

2**4
16

7**3
343

10**3
1000
SyntaxError: multiple statements found while compiling a single statement
6**3
216

2**2
4

3**3
27

4**4
256

5**5
3125

10*2
20

10*2
20
10*3
30
