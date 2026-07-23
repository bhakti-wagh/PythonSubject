Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Collection Data Type Methods:

# In Collection Data type we have 5 Types

#1.List D.T
#2.Tuple D.T
#3.Set D.T
#4.Dict D.T
#5.String D.T

#1.List D.T :->
# list is collection of homogeneous and     heterogeneous elements
# Ordered Data type
#Mutable Data type
#Allow duplicate values
#supports indexing and slicing
#Not hashable(cannot be used as dict keys)

#list [30] methods
    

dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#1.append():-> varname.append(element)
#keypoints:-> 1. Adds one element at end
#             2. Modifies the orginal list
#             3. Single Value D.T & Multi
#                value D.T allow

#Ex:

a=[1,2]
a.append(3)
a
[1, 2, 3]

a.append(100)
a
[1, 2, 3, 100]
a.append(500)
a
[1, 2, 3, 100, 500]

#2.extend():-> varname.extend(iterable)
#Keypoints:->  1.Adds Multiple elements
#              2.only Multivalue D.T allow
#              3. It remove boundart cond.

#Ex:
a
[1, 2, 3, 100, 500]

a.extend([3,4])
a
[1, 2, 3, 100, 500, 3, 4]
a.extend((10,20))
a
[1, 2, 3, 100, 500, 3, 4, 10, 20]
a.extend({50,60})
a
[1, 2, 3, 100, 500, 3, 4, 10, 20, 50, 60]
a.extend({5:70})
a
[1, 2, 3, 100, 500, 3, 4, 10, 20, 50, 60, 5]

#If we pass single value D.T it will show
#TypeError:'singleV D.T' is not iterable
a.extend(6)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.extend(6)
TypeError: 'int' object is not iterable


#3.insert():->varname.insert(posi,value)
#Keypoints:-> 1.inserts at specified index
#             2.Doesn't replace
#             3. Shifts existing elements
#             4. both Data type allow(s/m)

# If particular position is not present it will won't show any error it will add ele at end of list

#Ex:

b=[10,20]

b.insert(0,100)
b
[100, 10, 20]
b.insert(1,200)
b
[100, 200, 10, 20]
b.insert(5,400)
b
[100, 200, 10, 20, 400]



#4.pop():-> two syntax:->
#   varname.pop():-> it wil automatically remove last element , (-1)
#   varname.pop(position):-> it will remove specified position
# if specified position is not present it will show IndexError :-> out of range

#Example:

b
[100, 200, 10, 20, 400]

b.pop()
400

b.pop(2)
10

b.pop(7) #it wil show IndexError
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    b.pop(7) #it wil show IndexError
IndexError: pop index out of range


#5.remove():-> varname.remove(element)
#
#Keypoints:->  1. here we remove element
#           2. if element is not present                it will show ValueError
#Ex:

b
[100, 200, 20]

b.remove(20)
b
[100, 200]

b.remove(50)#It will show ValueError
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    b.remove(50)#It will show ValueError
ValueError: list.remove(x): x not in list



#5.clear():-> varname.clear()
#Keypoints:->1.It will remove all element               which is present in list
#       2. After clearing all ele it will           show empty list ([])

#       3. to remove empty list also we use one keyword :-> del varname

#EX:

b
[100, 200]

b.clear()
b
[]

del b

b
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    b
NameError: name 'b' is not defined



#7.index():-> varname.index('ele',si,ei+1)
#Keypoints:-> 1.here we pass element we                 get o/p as position
#       2.If the particular element is not     present then it will show ValueError

#Ex:

a
[1, 2, 3, 100, 500, 3, 4, 10, 20, 50, 60, 5]

a.index(2)
1

a.index(500)
4

a.index(1000) #It will show valueError
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    a.index(1000) #It will show valueError
ValueError: 1000 is not in list


#8.count():-> varname.count('element')
#keypoints:-> 1.Returns occurrence count
#       2.If element is not present then    it will show 0 (no Error)

#Ex:

a
[1, 2, 3, 100, 500, 3, 4, 10, 20, 50, 60, 5]

a.count(3)
2

a.count(60)
1

a.count(1000) #it will show 0
0


#8.Sort():-> varname.sort()
#keypoints:->1.Ascending to Dec by default
#       2. it changes original list
#       3. we can't use heterogeneoues ele

#   if we use hetergoeneoues it will show   TypeError

#Ex:
a
[1, 2, 3, 100, 500, 3, 4, 10, 20, 50, 60, 5]

a.sort()
a
[1, 2, 3, 3, 4, 5, 10, 20, 50, 60, 100, 500]
a
[1, 2, 3, 3, 4, 5, 10, 20, 50, 60, 100, 500]

[1,"a"].sort() #It will show TypeError
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    [1,"a"].sort() #It will show TypeError
TypeError: '<' not supported between instances of 'str' and 'int'



#10.reverse():-> varname.reverse()
#Keypoints:-> 1.Reverses original list.
#       2.only we can use with list D.T

a
[1, 2, 3, 3, 4, 5, 10, 20, 50, 60, 100, 500]

a.reverse()
a
[500, 100, 60, 50, 20, 10, 5, 4, 3, 3, 2, 1]
>>> 
>>> 
>>> #11.copy():-> newvarname=oldvarname
>>> #keypoints:-> both varable id should be                 same
>>> 
>>> #Ex:
>>> a
[500, 100, 60, 50, 20, 10, 5, 4, 3, 3, 2, 1]
>>> 
>>> c=a
>>> c
[500, 100, 60, 50, 20, 10, 5, 4, 3, 3, 2, 1]
>>> a
[500, 100, 60, 50, 20, 10, 5, 4, 3, 3, 2, 1]
>>> 
>>> id(a)
2524060407552
>>> id(c)
2524060407552
>>>


