Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> s={"apple","banana","mango"}
>>> 
>>> #Print the set
>>> s
{'banana', 'apple', 'mango'}
>>> 
>>> #find the length of the set
>>> len(s)
3
>>> 
>>> #find the id address of set
>>> id(s)
2534595105440
>>> 
>>> #add one item
>>> s.add("orange")
>>> s
{'banana', 'orange', 'apple', 'mango'}
>>> 
>>> #add multiples items
s.update({"grapes","kiwi"})
s
{'kiwi', 'apple', 'orange', 'grapes', 'banana', 'mango'}


#remove an items using remove()

s.remove("banana")

s
{'kiwi', 'apple', 'orange', 'grapes', 'mango'}

#remove an items using discard()
s.discard("kiwi")
s
{'apple', 'orange', 'grapes', 'mango'}

#remove an random item pop()
s.pop()
'apple'
s
{'orange', 'grapes', 'mango'}

#clear all items
s.clear()
s
set()

s={'kiwi', 'apple', 'orange', 'grapes', 'banana', 'mango'}

#copy a set
a=s
a
{'kiwi', 'apple', 'orange', 'grapes', 'banana', 'mango'}


#Union of two sets
a={1,2,3}
b={3,4,5}

a.union(b)
{1, 2, 3, 4, 5}


#Intersection
a.intersection(b)
{3}

#difference
a.difference(b)
{1, 2}

b.difference(a)
{4, 5}

#symmetric difference
a.symmetric_difference(b)
{1, 2, 4, 5}
b.symmetric_difference(a)
{1, 2, 4, 5}



#create an empty set

d=set()
d
set()
type(d)
<class 'set'>
