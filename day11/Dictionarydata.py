Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Dictionary methods
... 
... #1. create dictionary with name, age,and city .print all keys
>>> 
>>> info={'name':'bhakti','age':22,'city':'pune'}
>>> print(info)
{'name': 'bhakti', 'age': 22, 'city': 'pune'}
>>> 
>>> #2.print all values
>>> info.values()
dict_values(['bhakti', 22, 'pune'])
>>> 
>>> #3.Print all key-values pairs
>>> info.items()
dict_items([('name', 'bhakti'), ('age', 22), ('city', 'pune')])
>>> 
>>> #4.get age value
info.get('age')
22

#add course
info.update({'course':'Python'})
info
{'name': 'bhakti', 'age': 22, 'city': 'pune', 'course': 'Python'}

#copy dictionary into another variable
x=info.copy()
x
{'name': 'bhakti', 'age': 22, 'city': 'pune', 'course': 'Python'}

#remove city using pop()

x.pop('city')
'pune'
x
{'name': 'bhakti', 'age': 22, 'course': 'Python'}

#remove last inserted key-value
x.popitems()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x.popitems()
AttributeError: 'dict' object has no attribute 'popitems'. Did you mean: 'popitem'?
x.popitem()
('course', 'Python')

x
{'name': 'bhakti', 'age': 22}

#clear the entire dictionary
x.clear()
x
{}



#2. set Methods

#create set of five fruits and add 'kiwi'

fruits={"apple","banana","cherry","mango","orange"}
fruits
{'orange', 'mango', 'apple', 'cherry', 'banana'}

fruits.add('kiwi')
fruits
{'orange', 'mango', 'apple', 'cherry', 'banana', 'kiwi'}

#remove apple form set
fruits.remove('apple')
fruits
{'orange', 'mango', 'cherry', 'banana', 'kiwi'}

#use discard() to remove "banana"
fruits.discard("banana")
fruits
{'orange', 'mango', 'cherry', 'kiwi'}


#remove and print random element using pop
fruits.pop()
'orange'

#copy a set into another variable

newvar=fruits

newvar
{'mango', 'cherry', 'kiwi'}

#clear all elements from set
newvar.clear()
newvar
set()


#create two sets and find their union
x={1,3,4,5,6}
y={4,5,6,8,9,3}

x.union(y)
{1, 3, 4, 5, 6, 8, 9}

#intersection
x.intersection(y)
{3, 4, 5, 6}

#difference
x.diference(y)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    x.diference(y)
AttributeError: 'set' object has no attribute 'diference'. Did you mean: 'difference'?
x.difference(y)
{1}



#Tuple Methods
p=(5,2,5,8,5,1)
p.count(5)
3

a="Python"
a.index("Python")
0

b=(50,100,150,200)
b.index(100)
1

c=('a','b','a','c','a').
SyntaxError: invalid syntax
c=('a','b','a','c','a')
c.count('a')
3

