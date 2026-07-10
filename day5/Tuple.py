Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> 
>>> #Tuple ---> keyPoints
>>> 
>>> #Tuple is order data type
>>> #Tuple data type it wil accept duplicate elements
>>> #In tuple data type each element separated by comma
>>> #In typle data type boundary condition is not a mandatory but comma is mandatory
>>> 
>>> 
>>> #Syntax --> var_Name=(ele1,ele2,ele3.........)
>>> 
>>> #len()---> len(Var_Name) or len(tuple)
>>> 
>>> 
>>> #How to create empty typle in normal way
>>> 
>>> a=()
>>> a
()
>>> 
>>> type(a)
<class 'tuple'>
>>> 
>>> #How to create empty tuple by using object
>>> 
>>> 
>>> tuple()
()

y=tupe()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    y=tupe()
NameError: name 'tupe' is not defined. Did you mean: 'tuple'?
y=tuple()
y
()

#How to create single value tuple\
c=(900,)
c
(900,)
type(c)
<class 'tuple'>

k=("Hiii",)
k
('Hiii',)
type(k)
<class 'tuple'>
<class 'tuple'>
SyntaxError: invalid syntax


#tuple data type also immutable data type
#Tuple data type we cannto modify0



# in tuple datat type ---> count(), index() method

#tuple datat ype is immutable data type

#Key--points-->

#here we can't do modification
#here it will won't supperot assignment operator(=)
#in tuple if we want do modification we don't have methods



#to update value
#syntax--> var_name[postion]=value

s=(10,20,"Hello",[1,2,3])
s[2]
'Hello'
s[2].upper()
'HELLO'

s
(10, 20, 'Hello', [1, 2, 3])

s[3]
[1, 2, 3]
s[3][0].isalnum('100')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s[3][0].isalnum('100')
AttributeError: 'int' object has no attribute 'isalnum'
s[3][0].isdigit('100')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s[3][0].isdigit('100')
AttributeError: 'int' object has no attribute 'isdigit'
s[3][0]=100
s
(10, 20, 'Hello', [100, 2, 3])





#immutable data type--->
#here we can't change orignal object but we can do modification
#Ex:--> string, tuple


#Mutable:--> here we can change orginal object
#Ex:--> list, set, dictionary

v="Morning class"
v.swapcase()
'mORNING CLASS'
v
'Morning class'


#mutable datat type ex
x=[1,2,3,4,5]
x[4]='hi'
x
[1, 2, 3, 4, 'hi']

x=[3]='heyo'
SyntaxError: cannot assign to literal
x[3]='heyo'
x
[1, 2, 3, 'heyo', 'hi']

#syntax--> var_Name[postion]=value

x[1]=500
x
[1, 500, 3, 'heyo', 'hi']


d=(34,["abc","walmart",'python'],600,{67,909})
d
(34, ['abc', 'walmart', 'python'], 600, {67, 909})
d[1]
['abc', 'walmart', 'python']
d[1][1]
'walmart'
d[1][1]=100
d
(34, ['abc', 100, 'python'], 600, {67, 909})
d[3]
{67, 909}
d[3][0]="hi"
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    d[3][0]="hi"
TypeError: 'set' object does not support item assignment
d[3][1]=100
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    d[3][1]=100
TypeError: 'set' object does not support item assignment
File "<pyshell#114>", line 1, in <module>
SyntaxError: invalid syntax


e=(100,67,"abc","python',"walmart","instagram")
   
SyntaxError: unterminated string literal (detected at line 1)
e
   
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    e
NameError: name 'e' is not defined
e=(100,67,"abc","python',"walmart","instagram")
   
SyntaxError: unterminated string literal (detected at line 1)
e=(100,67,"abc","python","walmart","Instagram")
   
e
   
(100, 67, 'abc', 'python', 'walmart', 'Instagram')
e[-3]
   
'python'
e[5]
   
'Instagram'

           

w=(100,500,True,False,"snapchat","walmart","Marker","penset")
   
w[4]
   
'snapchat'
w[-4]
   
'snapchat'

w[2]
   
True
w[1]
   
500
w[-7]
   
500
w[6]
   
'Marker'
w[-2]
   
'Marker'

w[0]
   
100
w[-8]
   
100

w[20]
   
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    w[20]
IndexError: tuple index out of range
w[-30]
   
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    w[-30]
IndexError: tuple index out of range


#slicing--> var_name[startindex:endindex+1:stepvalue]
   
w=[1:5:1]
   
SyntaxError: invalid syntax
w[1:5:1]
   
(500, True, False, 'snapchat')

w[0:7:2]
   
(100, True, 'snapchat', 'Marker')
w[::]
   
(100, 500, True, False, 'snapchat', 'walmart', 'Marker', 'penset')


#indexing+slicing
   
w
   
(100, 500, True, False, 'snapchat', 'walmart', 'Marker', 'penset')

w[5]
   
'walmart'
w[4]
   
'snapchat'
w[4:8]
   
('snapchat', 'walmart', 'Marker', 'penset')
w[4][4:8:1]
   
'chat'

w[6]
   
'Marker'
w[6][1:4:1]
   
'ark'

w[5]
   
'walmart'
w[5][0:7:1]
   
'walmart'
w[5][0:7:6]
   
'wt'

w[4][2:7:2]
   
'aca'
w
   
(100, 500, True, False, 'snapchat', 'walmart', 'Marker', 'penset')
w[7][3:6:1]
   
'set'

z=["India","Abroad","classes","germany","Australia","canada")
   
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
z=["India","Abroad","classes","germany","Australia","canada"]
   
z[1][2:6:1]
   
'road'

z[2][4:7:1]
   
'ses'

z[3][4:7:1]
   
'any'

z[4][6:9:1]
   
'lia'

z[5][3:6:1]
   
'ada'

z[1:3:1]
   
['Abroad', 'classes']
z[0:5:2]
   
['India', 'classes', 'Australia']
['India', 'classes', 'Australia']
   
['India', 'classes', 'Australia']



#count()---> var_name.count(element)
   

z
   
['India', 'Abroad', 'classes', 'germany', 'Australia', 'canada']
e.count("India")
   
0
e.count("India")
   
0

z.count("India")
   
1

z.count("Abroad")
   
1


z
   
['India', 'Abroad', 'classes', 'germany', 'Australia', 'canada']
z.count("classes")
   
1

e=(10,20,30,10,50,20)
   
#index()---> var_name.index(element,si,ei+1)
   
e.index(10)
   
0
e.index(10,1)
   
3

e.index(50)
   
4

e.index(500)
   
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    e.index(500)
ValueError: tuple.index(x): x not in tuple
e[500]
   
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    e[500]
IndexError: tuple index out of range
dir(tuple)
   
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


# what are the things rememeber
   

#defination
   
#what is difference between homogeneus & hetergoenus
   
#tuple is order or unorder
   
#it is immutable or mutable
   
#Mutable another name--> unhasable
   
