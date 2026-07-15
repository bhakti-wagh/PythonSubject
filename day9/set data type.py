Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> # set Data Type
>>> 
>>> # boundary condition is {}
>>> #if you want to store unique element then we can go for set data type
>>> #set data type is a unorder data type
>>> #set data type is a Mutable data type
>>> #set data type it will accept only Immutable data type & single value data type
>>> 
>>> #Syntax:->  varname={ele1,ele2,ele3...}
>>> 
>>> 
>>> #set data type we can't do indexing and slicing because set data type is unorder DT
>>> 
>>> #set data type we can't create empty set by normal way , If we create empty set in normal way then it act like dictionary data type.
>>> 
>>> 
>>> #how to create empty set by using object??
>>> 
>>> set()
set()
>>> 
>>> e=set()
e
set()

type(e)
<class 'set'>


e={False,1,2.2, (1,2),'hi',(3+4j)}


e
{False, 1, 2.2, (1, 2), 'hi', (3+4j)}

e={False,1,2.2, (1,2),'hi',(3+4j),[1,2]}
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    e={False,1,2.2, (1,2),'hi',(3+4j),[1,2]}
TypeError: unhashable type: 'list'

#In set data type we can't pass mutable data type if we pass it will show TypeErro :unhasable error


t={0,False,True,1,8,8,12}
len(t)
4
#because internally False=0, True=1 , & in set data type won't support duplicate character


dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#set data type (17 methods)

# To adding element in set
# 1.add()
# 2.update()


# 1. add() :->  varName.add(element)-> only single value & immutable data type
#               -> if we pass mutable data type it will show typeError:unhasable error
# we can't predict which postion it will add because set data type is unorder DT

b={1}
b
{1}

type(b)
<class 'set'>

b.add{False}
SyntaxError: invalid syntax
b.add(False)
b
{False, 1}

b.add(100)
b
{False, 1, 100}

b.add(2.5)
b
{False, 1, 2.5, 100}

b.add('hi')
b
{False, 1, 2.5, 100, 'hi'}

b.add(3+2j)
b
{False, 1, 2.5, 100, (3+2j), 'hi'}

b.add( (12,13,17))
b
{False, 1, 2.5, (12, 13, 17), 100, (3+2j), 'hi'}

b.add(100)
b
{False, 1, 2.5, (12, 13, 17), 100, (3+2j), 'hi'}
#when we pass duplicate element it will not add if element is present because set data type duplicate element not allowed

b.add("abc",900) #here we can't pass multiple element at time
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    b.add("abc",900) #here we can't pass multiple element at time
TypeError: set.add() takes exactly one argument (2 given)




#2.update():-> varname.update(iterable)-> collection data type(str,list,tuple,set,dict)

x={1}

x.update(100) #we can't pass single value data type it will show error
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    x.update(100) #we can't pass single value data type it will show error
TypeError: 'int' object is not iterable

x.update("pyhton")
x
{1, 'p', 'y', 'h', 'n', 't', 'o'}

x.update([100,200,300])
x
{1, 'p', 'y', 100, 'h', 200, 'n', 300, 't', 'o'}
#here collection data type boundary conditon will remove

x.update([[1,2,3]])# here we can't pass nested list it will show error
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    x.update([[1,2,3]])# here we can't pass nested list it will show error
TypeError: unhashable type: 'list'

x.update("abc",[45,65],(123,456)) # here we can pass unlimited element at time
x
{1, 'p', 65, 'y', 100, 'h', 200, 456, 'n', 300, 'a', 45, 't', 'o', 123, 'b', 'c'}






# To Remove element
# 1.pop() -> varName.pop()
#2. remove()-> varname.remove(element)
#3.discard()-> varname.discard(element)
#4.clear()-> varname.clear()
#5. del varname


#1. pop():->  varName.pop()-> here it will we can't predict  exact which element will remove

x
{1, 'p', 65, 'y', 100, 'h', 200, 456, 'n', 300, 'a', 45, 't', 'o', 123, 'b', 'c'}

x.pop()
1
x.pop90
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    x.pop90
AttributeError: 'set' object has no attribute 'pop90'
x.pop()
'p'

x.pop()
65

x
{'y', 100, 'h', 200, 456, 'n', 300, 'a', 45, 't', 'o', 123, 'b', 'c'}
x.pop()
'y'




t={"walmart","snap","Insta","python"}
t.pop()
'walmart'

t.pop()
'python'


#2.remove():-> varname.remove(element)
# if specified element is not present then it will show keyError

x
{100, 'h', 200, 456, 'n', 300, 'a', 45, 't', 'o', 123, 'b', 'c'}

x.remove(200)
x
{100, 'h', 456, 'n', 300, 'a', 45, 't', 'o', 123, 'b', 'c'}

x.remove(125)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    x.remove(125)
KeyError: 125



#3.discard():-> varname.discard(element)
#
# If specified element is not present then it will show blankspace

x
{100, 'h', 456, 'n', 300, 'a', 45, 't', 'o', 123, 'b', 'c'}

x.discard(45)
x
{100, 'h', 456, 'n', 300, 'a', 't', 'o', 123, 'b', 'c'}

x.(5000)
SyntaxError: invalid syntax
x.discard(5000)#here show blank space


#4.clear()-> varname.clear()-> to remove all element inside set

t
{'snap', 'Insta'}
t.clear()
t
set()

#5.del varname:-> to delete empty set object
del t



# Intersection Method()-> it print common element in two set
#syntax :-->  var1.intersection(var2)

x={"apple","pen","marker",10}
y={"pen", "marker",15,23}

x.intersection(y)
{'marker', 'pen'}


#if  the common element is not present then it will show empty set()

c={1,5,6,8}
d={7,"abc","dsj"}

c.intersection(d)
set()



#Symmetric_difference()-> if we want to print which is not common element  in two set
#syntax:--> var1.symmetric_difference(var2)

x
{'apple', 'marker', 10, 'pen'}
y
{'marker', 23, 'pen', 15}

x.symmetric_difference(y)
{10, 15, 'apple', 23}



#difference()-> it will print not common element but for only orignal set
#syntax:--> var1.difference(var2)--> var1--> orginal set


x
{'apple', 'marker', 10, 'pen'}

x.difference(y)
{'apple', 10}

y.difference(x)
{15, 23}

y
{'marker', 23, 'pen', 15}





#Boolean Methods

#1.isdisjoint() :-> var1.isdisjoint(var2)
#if in two set not common element then-> True
#if in two set common element then-> False


a={4,6,8}
b={40,60,80}

a.isdisjoint(b)
True


c={4,5,6,8}
d={5,3,1,5,2}

c.isdisjoint(d)
False


#2.issuperset():-> var1.issuperset(var2)--> var1->orginal set, var2->referenceset

#if in var2 all element are present in var1 then -> True
# if in var2 all element are not present in var1 then -> False

z={100,200,300,400,500}
y={100,200,500}

z.issuperset(y)
True

y.issuperset(z)
False


#3.issubset():-> var1.issubset(var2)
#if in var1 all elements are present in var2 then-> True
#if in var1 all elements are not present in var2 then -> false

z
{400, 100, 500, 200, 300}
y
{200, 100, 500}
z.issubset(y)
False

y.issubset(z)
True

