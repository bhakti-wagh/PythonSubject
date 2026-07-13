Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Sort Method in List

#Sort()-> by default it will conver (lower)ascending to (bigger)decending
#Sort()--> it will accept only homogeneous element(same type of data)

#Syntax-->  1. variableName.sort()
#           2. variableName.sort(reverse=False)(False--< asc to dec)
#           3. VariableName.sort(reverse=True) (True--< dec to asc)


#sort()

c=[100,34,1,0.4,2,65,55,35,88]
c.sort()
c
[0.4, 1, 2, 34, 35, 55, 65, 88, 100]
c.sort(reverse=False)
c
[0.4, 1, 2, 34, 35, 55, 65, 88, 100]

c.sort(reverse=True)
c
[100, 88, 65, 55, 35, 34, 2, 1, 0.4]



d=["apple","Apple","ball","Ball","cat","Cat"]
d.sort()
d
['Apple', 'Ball', 'Cat', 'apple', 'ball', 'cat']
#here first comes uppercase and then lowercase because  of ascii value (65-90) and(97-122)

d.sort(reverse=False)
d
['Apple', 'Ball', 'Cat', 'apple', 'ball', 'cat']
#uppercase value(65-90) to lowercase(97-122)

d.sort(reverse=True)
d
['cat', 'ball', 'apple', 'Cat', 'Ball', 'Apple']
#lowercase value(97-122) to uppercase(65-90)


x=['apple','apply']
x.sort()
x
['apple', 'apply']
#here 1st character same it will ignore
#here 2nd character also same it will ignore
#here 3rd and 4th also same ite will ignore it will go to 5th
#here 5th character different e(101) and y(121)

#here if all characters are same then at last it will check length of character if length also same the First Come First Serve





x
s=['apple','apple']
s.sort()
s
['apple', 'apple']
#here if all characters are same then at last it will check length of character if length also same the First Come First Serve


z=["snapchat","instagram","wallmart","sql","fb","A"]
#syntax:--> for character 1. var_Name.sort(key=len, reverse=False) asc to dec
#                         2. var_Name.sort(key=len, reverse=True) dec to asc

#len()--> funtion we cant use with single type of data , we can use with mutliple type of data

z
['snapchat', 'instagram', 'wallmart', 'sql', 'fb', 'A']

z.sort(key=len)
z
['A', 'fb', 'sql', 'snapchat', 'wallmart', 'instagram']
z.sort(key=len,reverse=False)
z
['A', 'fb', 'sql', 'snapchat', 'wallmart', 'instagram']


z.sort(key=len,reverse=True)
z
['instagram', 'snapchat', 'wallmart', 'sql', 'fb', 'A']


n=[89,45,70,6,40,23,38,99,13,6]
n.sort()
n
[6, 6, 13, 23, 38, 40, 45, 70, 89, 99]

n.sort(reverse=False)
n
[6, 6, 13, 23, 38, 40, 45, 70, 89, 99]

n.sort(reverse=True)
n
[99, 89, 70, 45, 40, 38, 23, 13, 6, 6]


l=['G','b','e','T','w','x','K','L','v']
l.sort()
l
['G', 'K', 'L', 'T', 'b', 'e', 'v', 'w', 'x']
l.sort(key=len,reverse=False)
l
['G', 'K', 'L', 'T', 'b', 'e', 'v', 'w', 'x']
l.sort(key=len,reverse=True)
l
['G', 'K', 'L', 'T', 'b', 'e', 'v', 'w', 'x']
len(l)
9

len(n)
10

dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


to concat two list
SyntaxError: invalid syntax

#to concat two list

a=[1,2,3,4,5]
b=[10,20,30,40,50]

a+b
[1, 2, 3, 4, 5, 10, 20, 30, 40, 50]

#Unpacking--->(*)
>>> 
>>> print(*a)
1 2 3 4 5
>>> 
>>> print(*b)
10 20 30 40 50
>>> 
>>> x=[*a,*b]
>>> x
[1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
>>> 
>>> 
>>> 
>>> 
>>> #sequence Data Type:-->
>>> 
>>> #which data type we are doing indexing and slicing that type of dat
>>> #we can call it as a sequence Data Type
>>> 
>>> #ex:-> string,list,Tuple
>>> 
>>> #iterable:-> all collection data type we can call it as a iterable.
>>> 
>>> #ex:-> string, list, tuple,set dictionary
>>> 
>>> #all sequence data type are iterable
