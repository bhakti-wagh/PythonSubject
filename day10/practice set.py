Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> #Set Data Type
>>> 
>>>  #Write a program to create set add a new element to it , remove an element using remove() and discard an element using discard()
>>> 
>>> fruits=set()
>>> 
>>> fruits
set()
>>> 
>>> fruits.update({"apple","banana","cherry"})_
SyntaxError: invalid syntax
>>> 
>>> fruits.update({"apple","banana","cherry"})
>>> fruits
{'banana', 'cherry', 'apple'}

print("After add:",fruits)
After add: {'banana', 'cherry', 'apple'}


fruits.remove("banana")
print("After remove: ",fruits)
After remove:  {'cherry', 'apple'}

fruits.add("mango")
print("After add :",fruits)
After add : {'mango', 'cherry', 'apple'}

fruits.discard("Grapes")
print("After discard not presetn:",fruits)
After discard not presetn: {'mango', 'cherry', 'apple'}




# clear all elements
colors={"red","green","blue"}

colors.clear()
colors
set()


#find the length of a set

animals={"cat","dog","bird","fish"}
len(animals)
4


#check if a set is empty
data=set()
data
set()
print("the set is empty",data)
the set is empty set()


#union of sets
set_a={1,2,3,4}
set_b={3,4,5,6}

set_a.union(set_b)
{1, 2, 3, 4, 5, 6}


#intersection of sets
set_a
{1, 2, 3, 4}
set_b
{3, 4, 5, 6}

set_a.intersection(set_b)
{3, 4}


#difference of sets
set_a.difference(set_b)
{1, 2}

#symmetric_difference of sets

set_a.symmetric_difference(set_b)
{1, 2, 5, 6}



#find max and min
numbers={42,7,19,85,5,56}

print("Max:",max(numbers))
Max: 85

print("Min:",min(numbers))
Min: 5



#sum of set elements

numbers={10,20,30,40,50}
print("sum:",sum(numbers))
sum: 150


#add a list of elements
fruits={"apple","banana"}
new_fruits={"cherry","mango","apple"}

update_fruits.update(new_fruits)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    update_fruits.update(new_fruits)
NameError: name 'update_fruits' is not defined
fruits.update(new_fruits)
print("updated set:",fruits)
updated set: {'banana', 'apple', 'mango', 'cherry'}



#update with multiple iterables

base={1,2}
from_list=[3,4]
from_tuple=(5,6)
from_set={7,8}

base.update(from_list,from_tuple,from_set)
base
{1, 2, 3, 4, 5, 6, 7, 8}


#intersection check with isdisjoint

set_a={1,2,3}
set_b={4,5,6}

set_a.isdisjoint(set_b)
True


#set difference update
a={1,2,3,4,5}
b={3,4,5,6,7}

a.difference_update(b)
print("a:",a)
a: {1, 2}


#set intersection update
a={1,2,3,4,5}
b
{3, 4, 5, 6, 7}

a.intersection_update(b)
a
{3, 4, 5}


#set symmetric difference update
a={1,2,3,4,5}
b
{3, 4, 5, 6, 7}

a.symmetric_difference_update(b)
a
{1, 2, 6, 7}


#remove items simultaneously
items={10,20,30,40,50,60}
to_remove={20,40,60}

items.difference_update(to_remove)

print("items:",items)
items: {50, 10, 30}


#pop operation
s={100,200,300}
s.pop()
100
