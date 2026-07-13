Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


#how to create empty list in noramal way
a=[]
a
[]

#how to create empty list by using object
list()
[]

e=list()
e
[]

type(e)
<class 'list'>


#list data type os order data type
s=[11,12,13,14,15]
s
[11, 12, 13, 14, 15]

#list data type it will accept duplicate elements
x=[1,2,5,2,1,5,4,2,3,5,6,1]
x
[1, 2, 5, 2, 1, 5, 4, 2, 3, 5, 6, 1]

#in the given string how many elements are present then---> len()
len(x)
12

#in list data type each element separated by comma
c=[1 2 3]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
c=[1 ,2 ,3]
c
[1, 2, 3]


#in list data type wee can do indexing and slicing

e=[100,89.34,True,"Welcome","walmart","goodluck",12]
e[-4]
'Welcome'
e[-6]
89.34

e[4]
'walmart'

e[4][3]
'm'
e[-4] = 100
e
[100, 89.34, True, 100, 'walmart', 'goodluck', 12]

e[2]=False
e
[100, 89.34, False, 100, 'walmart', 'goodluck', 12]

dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#in copy --> shalowcopy & deapcopy


#Adding element into the list
#  1.append()

x=[]
x
[]

#first will add single value data type

x.append(10)
x
[10]

x.append(45.23)
x
[10, 45.23]
x.append(1+2j)
x
[10, 45.23, (1+2j)]

x.append(True)
x
[10, 45.23, (1+2j), True]


#now will add collection data type

x.append("Hello")
x
[10, 45.23, (1+2j), True, 'Hello']

x.append([1,2])
x
[10, 45.23, (1+2j), True, 'Hello', [1, 2]]

x.append( (10,"Good"))
x
[10, 45.23, (1+2j), True, 'Hello', [1, 2], (10, 'Good')]

x.append( {40,300} )
x
[10, 45.23, (1+2j), True, 'Hello', [1, 2], (10, 'Good'), {40, 300}]

x.append( {'fruit':'apple'})
x
[10, 45.23, (1+2j), True, 'Hello', [1, 2], (10, 'Good'), {40, 300}, {'fruit': 'apple'}]





#in append method---> error
x.append()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    x.append()
TypeError: list.append() takes exactly one argument (0 given)

x.append(10,13)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    x.append(10,13)
TypeError: list.append() takes exactly one argument (2 given)



# extend() ---> var.name.extend(iterable)

s=[]
s
[]

s.extend([100,200,300])
s
[100, 200, 300]

s
[100, 200, 300]
[100, 200, 300]
[100, 200, 300]


  # extend() ---> var.name.extend(iterable)
  

z=[]
z
[]

z.extend([100,200,300])
z
[100, 200, 300]

z.extend("Hello")
z
[100, 200, 300, 'H', 'e', 'l', 'l', 'o']

z.extend({555:600},[10,20])
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    z.extend({555:600},[10,20])
TypeError: list.extend() takes exactly one argument (2 given)
z.extend({555:600})s
SyntaxError: invalid syntax
z.extend({555:600})
z
[100, 200, 300, 'H', 'e', 'l', 'l', 'o', 555]




#append vs extend


x=[]
x
[]

x.append("Python")
z
[100, 200, 300, 'H', 'e', 'l', 'l', 'o', 555]
x
['Python']

x.extend("Python")
x
['Python', 'P', 'y', 't', 'h', 'o', 'n']

x.append([900,10000])
x
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000]]

x.extend([900,10000])
x
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000], 900, 10000]

x.append({1,2,3,4})
x
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000], 900, 10000, {1, 2, 3, 4}]

x.extend({1,2,3,4})
x
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000], 900, 10000, {1, 2, 3, 4}, 1, 2, 3, 4]

x.append((900,1000,2000))
x
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000], 900, 10000, {1, 2, 3, 4}, 1, 2, 3, 4, (900, 1000, 2000)]
x.extend((900,1000,2000
          x
          
SyntaxError: '(' was never closed
x.extend((900,1000,2000))
          
x
          
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000], 900, 10000, {1, 2, 3, 4}, 1, 2, 3, 4, (900, 1000, 2000), 900, 1000, 2000]

x.append({45:54})
          
x
          
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000], 900, 10000, {1, 2, 3, 4}, 1, 2, 3, 4, (900, 1000, 2000), 900, 1000, 2000, {45: 54}]
x.extend({45:54})
          
x
          
['Python', 'P', 'y', 't', 'h', 'o', 'n', [900, 10000], 900, 10000, {1, 2, 3, 4}, 1, 2, 3, 4, (900, 1000, 2000), 900, 1000, 2000, {45: 54}, 45]

len(x)
          
21






#insert() ---> var_Name.insert(postion,value)
          
s=[1,2,3,4]
          
s.insert(0,100)
          
s
          
[100, 1, 2, 3, 4]

s.insert(4,"Python")
          
s
          
[100, 1, 2, 3, 'Python', 4]

s.insert(2,[1,2,3])
          
s
          
[100, 1, [1, 2, 3], 2, 3, 'Python', 4]

s.insert(6,True)
          
s
          
[100, 1, [1, 2, 3], 2, 3, 'Python', True, 4]
s.insert(10,True)
          
s
          
[100, 1, [1, 2, 3], 2, 3, 'Python', True, 4, True]


#in the insert if the specified postion is not allowed--> then it will not show any error it will add at the end
          

s.insert(-9,200)
          
s
          
[200, 100, 1, [1, 2, 3], 2, 3, 'Python', True, 4, True]




# Removing element into the list
          
#1.pop()
          
#2.remove()
          
#3.clear()
          
#4.keyword---> del var_name
          


#1.POP()---> syntax----> var_name.pop()   or var_Name.pop(postion)
          
s
          
[200, 100, 1, [1, 2, 3], 2, 3, 'Python', True, 4, True]

s.pop()
          
True
s
          
[200, 100, 1, [1, 2, 3], 2, 3, 'Python', True, 4]
s.pop(0)
          
200
s
          
[100, 1, [1, 2, 3], 2, 3, 'Python', True, 4]

#always use postion for pop
          
s.pop(2)
          
[1, 2, 3]
s
          
[100, 1, 2, 3, 'Python', True, 4]

#in pop method we can't pass more than one element
          


#2.remove()---> syntax----> var_Name.remove(element)
          

#if i not pass element then it will show error--> one argument is mandatory
          

s
          
[100, 1, 2, 3, 'Python', True, 4]

s.remove('Python')
          
s
          
[100, 1, 2, 3, True, 4]




#3.clear()--->  Sytax---> var_name.clear()
          
#if you want to delete all element inside the list ---> then it will give empty list
          

s
          
[100, 1, 2, 3, True, 4]
s.clear()
          

s
          
[]

#to delete list also then
          
# del var_name
          
del s
          
s
          
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> 
>>> x=[1,2,3,4,5,[90,100,200],"hello",89.5]
...           
>>> x[5]
...           
[90, 100, 200]
>>> x[5].pop(1)
...           
100
>>> x
...           
[1, 2, 3, 4, 5, [90, 200], 'hello', 89.5]
>>> 
>>> x[5].clear()
...           
>>> x
...           
[1, 2, 3, 4, 5, [], 'hello', 89.5]
>>> 
>>> del x[5]
...           
>>> x
...           
[1, 2, 3, 4, 5, 'hello', 89.5]
>>> 
>>> 
>>> r=[[100,300,600],9000,1000]]
...          
SyntaxError: unmatched ']'
r=[[100,300,600],9000,1000]
         
r
         
[[100, 300, 600], 9000, 1000]


y=[[[100, 300, 600], 9000, 1000]]
         
y
         
[[[100, 300, 600], 9000, 1000]]

r[0]
         
[100, 300, 600]
y[0]
         
[[100, 300, 600], 9000, 1000]
y[0][0]
         
[100, 300, 600]
r[0][0].remove(300)
         
Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    r[0][0].remove(300)
AttributeError: 'int' object has no attribute 'remove'
y[0][0].remove(300)
         
y
         
[[[100, 600], 9000, 1000]]


dir(list)
         
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


d=[100,200,300,100,300]
         
d.count(100)
         
2
d.count(400)
         
0


#index()---> var_name.index(element,si,ei+1)
         
d
         
[100, 200, 300, 100, 300]
d.index(100)
         
0
d.index(100,3)
         
3
d.index(100,2)
         
3

d.index(10000)
         
Traceback (most recent call last):
  File "<pyshell#288>", line 1, in <module>
    d.index(10000)
ValueError: 10000 is not in list
d.count(400)
         
0



#reverse()--> varname.reverse()--> only for list not to other data type
         
e=[1,2,3,4,5,[800,900,100],"hello"]
         
e
         
[1, 2, 3, 4, 5, [800, 900, 100], 'hello']
e.reverse()
         
e
         
['hello', [800, 900, 100], 5, 4, 3, 2, 1]

e[0].reverse()
         
Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    e[0].reverse()
AttributeError: 'str' object has no attribute 'reverse'
e[1].reverse()
         
e
         
['hello', [100, 900, 800], 5, 4, 3, 2, 1]

e[0].reversed()
         
Traceback (most recent call last):
  File "<pyshell#303>", line 1, in <module>
    e[0].reversed()
AttributeError: 'str' object has no attribute 'reversed'
