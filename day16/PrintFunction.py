Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Print statement or Function
#print():->
#           To display output in python [on screen] we use print().
#Syntax:-> print(val1,val2,....valN,end='\n',sep='')-> sep=bydefault space shows

#-> end=''-> it will take next line as value
>>> 
>>> print("hello")
hello
>>> print("hello") print("good") print("Morning")
SyntaxError: invalid syntax
>>> 
>>> a="hello"
>>> b="Good"
>>> c="Morning"
>>> 
>>> print(a,b,c)
hello Good Morning
>>> print(a,b,c,end='')
hello Good Morning
>>> print(a,b,c,end='',sep='%')
hello%Good%Morning
>>> 
>>> 
>>> 
>>> d="Bhakti"
>>> print(a,b,c,end='d')
hello Good Morningd
>>> print(a,b,c,end=(d))
hello Good MorningBhakti
>>> 
>>> 
