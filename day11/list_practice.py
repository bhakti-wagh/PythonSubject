Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#List data Type

num=[10,20,30,40,50]
#access of third element
num[2]
30
#length of list
len(num)
5

isempty=len(num)==0
print(f"Is the list empty? {is_empty}")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(f"Is the list empty? {is_empty}")
NameError: name 'is_empty' is not defined. Did you mean: 'isempty'?
print(f"Is the list empty? {isempty}")
Is the list empty? False


#perform list manipulation
list=[100,50,400,500]
list[1]=200
list
[100, 200, 400, 500]
list.append(600)
list
[100, 200, 400, 500, 600]

list.insert(2,300)
list
[100, 200, 300, 400, 500, 600]

list.pop(600)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list.pop(600)
IndexError: pop index out of range
list.pop()
600

list.popitems(0)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list.popitems(0)
AttributeError: 'list' object has no attribute 'popitems'
list.remove(100)
list
[200, 300, 400, 500]



#sum and average of all numbers in list
numbers=[10,20,30,40,50]
print(sum(numbers))
150
>>> print(sum/len(numbers))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(sum/len(numbers))
TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'int'
>>> print(sum/len(numbers))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(sum/len(numbers))
TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'int'
>>> sum/len(numbers)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sum/len(numbers)
TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'int'
>>> x=sum/5
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x=sum/5
TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'int'
