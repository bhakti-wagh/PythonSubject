Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

# String Data type

str1="James"

str1[0:5:2]
'Jms'


str2="JhonDipPeta"
str2[4:7:1]
'Dip'


str3="PYnative"
str3[::-1]
'evitanYP'


str1 = "Emma is a data scientist who knows Python. Emma works at google."
>>> 
>>> str1.index["Emma"]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    str1.index["Emma"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
>>> str1.rindex("Emma")
43
>>> 
>>>  str1 = "Emma-is-a-data-scientist"
...  
SyntaxError: unexpected indent
>>> 
>>> str1 = "Emma-is-a-data-scientist"
>>> 
>>> str1.split("-")
['Emma', 'is', 'a', 'data', 'scientist']
>>> 
>>> 
>>> 
>>> 
>>> #vowel counter
>>> 
>>> str1="hello world"
>>> 
