Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> #sum and average of all numbers in a list
>>> 
>>> num=[10,20,30,40,50]
>>> print(sum(num))
150
>>> 
>>> average=sum(num)/len(num)
>>> print(average)
30.0
>>> 
>>> 
>>> #find maximum and minimum from list
>>> data=[45,12,89,2,67]
>>> 
>>> print(max(data))
89
>>> print(min(data))
2
>>> 
>>> #calculate the product of all elements

#count even and odd numbers

p=[10,21,4,45,66,93,11]

even= p%2==0
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    even= p%2==0
TypeError: unsupported operand type(s) for %: 'list' and 'int'


#reverse a list
list=[100, 200, 300, 400, 500]

list[::-1]
[500, 400, 300, 200, 100]


#sort a list
sort=[56,12,89,3,22]

sort.sort()
sort
[3, 12, 22, 56, 89]


#create a copy of list

fruits=["Apple","Banana","Cherry"]
newfruits=fruits
newfruits
['Apple', 'Banana', 'Cherry']


#combine two lists

a=["physics","Chemistry"]
b=["Maths","Biology"]

a.union(b)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.union(b)
AttributeError: 'list' object has no attribute 'union'
a*b
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'
a.extend(b)
a
['physics', 'Chemistry', 'Maths', 'Biology']



#list slicing:

w=[10, 20, 30, 40, 50, 60, 70]
w[2:5:1]
[30, 40, 50]


#swap two elements
f=[23,65,19,90]
f[0]=19
f[2]=23
f[3]=23
f
[19, 65, 23, 23]
f[3]=90
f
[19, 65, 23, 90]

#access nested list simple indexing

nested=[[1, 2], [3, 4, 5], [6, 7]]

nested[1]
[3, 4, 5]

nested[1][2]
5

#count occurrences of an item
k=[10, 20, 30, 10, 40, 10, 50]

k.count(10)
3

#remove item
l=[5, 20, 15, 20, 25, 50, 20]

l.remove(20)
l
[5, 15, 20, 25, 50, 20]
