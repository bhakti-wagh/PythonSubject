Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> # Boolean Methods Tasks
>>> 
>>> #1. check whether "Python" contains only alphabets
>>> a="Python"
>>> a.isalpha()
True
>>> 
>>> #2. check whether "Python123" contains only alphabets
>>> b="Python123"
>>> b.isalpha()
False
>>> 
>>> #because in isalpha() -> contains only alphabets not numbers or specail character or space
>>> 
>>> 
>>> #3. Check whether "Programming" contains only alphabet
>>> c="Programming"
>>> c.isalpha()
True
>>> 
>>> #4. Check whether "Hello World" contains only alphabet
>>> d="Hello World"
>>> d.isalpha()
False
#beacuse space is given

#5.check whether "JAVA" contains only alpahbets
e="JAVA"
e.isalpha()
True
#because all alphabets(uppercase/lowercase/combination)


#6. check whether "12345" contains only digits
f="12345"
f.isdigit()
True

#7.Check whether "2026" contains only digits.
g="2026"
g.isdigit()
True

#8.Check whether "12a34" contains only digits.
h="12a34"
h.isdigit()
False
#because it takes only number but no in quotes

#9.Check whether "007" contains only digits.
i="007"
i=isdigit()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    i=isdigit()
NameError: name 'isdigit' is not defined
i.isdigit()
True

#10.Check whether "98.6" contains only digits.
j="98.6"
j.isdigit()
False
#. is special character



#11. check whether "Python123" is alphanumeric
k="Python123"
k.isalnum()
True

#12.Check whether "Hello123" is alphanumeric.
l="Hello123"
l.isalnum()
True

#13.Check whether "Python 123" is alphanumeric.
m="Python 123"
m.isalnum()
False
#space given

#14. check whether "ABC123XYZ" is alphanumeric
n="ABC123XYZ"
n.isalnum()
True

#15.Check whether "Hello@123" is alphanumeric.
o="Hello@123"
o.isalnum()
False
#@ is specail character



#16. check whether "Python" is lowercase
p="python"
p.islower()
True

#17.check whether "python123" is lowercase
q="python123"
q.islower()
True

#18.check whether "Python"is lowercase
r="Python"
r.islower()
False

#P is uppercase

#19.check whether "hello world" is lowercase
s="hello world"
s.islower()
True

#20. check whether "hello123" is lowercase
t="hello123"
t.islower()
True


#21. check whether "PYTHON" is uppercase
v="PYTHON"
v.isupper()
True

#22. check whether "HELLO123" is uppercase
x="HELLO123"
x.isupper()
True

#23. check whether "Hello" is uppercase
z="Hello"
z.isupper()
False

#24. check whether "WELCOME HOME" is uppercase
y="WELCOME HOME"
y.isupper()
True



#25. check whether "Hello World" is title case
A1="Hello World"
A1.istitle()
True

#26.check whether "Python Programming" is title case
B2="Python Programming"
B2.istitle()
True

#27. check whether "python programming" is title case
C2="python programming"
C2.istitle()
False

#28. check whether "My Name Is Bhakti" is title case
D3="My Name Is Bhakti"
D3.istitle()
True


#29. Check whether " " (five spaces) contains only spaces.
e4="     "
e4.isspace()
True


#30. Check whether " Hello " contains only spaces.
F5=" Hello "
F5.isspace()
False
