Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> #Boolean Method file 2
>>> 
>>> #1.Find "P" in "Python"
>>> a="Python"
>>> a.find("P")
0
>>> 
>>> #2.Find "gram" in "Programming".
>>> b="Programming"
>>> b.find("gram")
3
>>> 
>>> #3.Find "o" in "Hello World".
>>> c="Hello World"
>>> c.find('o')
4
>>> 
>>> #4.Find "Java" in "Python Programming".
>>> d="Python Programming"
>>> d.find("Java")
-1
>>> 
>>> #5.Find "a" in "banana".
>>> e="banana"
>>> e.find('a')
1


#6. Find "H" in "Hello".
f="Hello"
f.index('H')
0


#7. Find "o" in "Good Morning".
g="Good Morning"
g.index('o')
1

#8.Find "Python" in "I Love Python".
h="I Love Python"
h.index("Python")
7

#9. Find "g" in "Programming"
i="Programming"
i.index('g')
3

#10. Find "z" in "Apple".
j="Apple"
j.index('z')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    j.index('z')
ValueError: substring not found


#11. Replace "Java" with "Python" in "I Love Java"
k="I Love Java"
k.replace("Python")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    k.replace("Python")
TypeError: replace() takes at least 2 positional arguments (1 given)

k.replace("Java","Python")
'I Love Python'

#12.Replace "cat" with "dog" in "cat is cute".
#12.Replace "cat" with "dog" in "cat is cute".

l="cat is cute"
l.replace("cat","dog")
'dog is cute'

#13. Replace "2025" with "2026" in "Happy New Year 2025".
m="Happy New Year 2025"
m.replace("2025","2026")
'Happy New Year 2026'

#14. Replace "red" with "blue" in "red rose".
n="red rose"
n.replace("red", "blue")
'blue rose'

#15. Replace all spaces with "-" in "Python Programming Language".

o="Python Programming Language"
o.replace(" ","-")
'Python-Programming-Language'


#16. Remove spaces from " Python ".
p=" Python "
p.strip()
'Python'

#17. Remove spaces form " Hello World "
q=" Hello World "
q.strip()
'Hello World'

#18. Remove spaces from " Programming"
r=" Programming"
r.strip()
'Programming'


#19. Remove left-side spaces from " Apple".
s=" Apple"
s.lstrip()
'Apple'

#20. Remove left-side spaces form  " Mango "
t=" Mango "
t.lstrip()
'Mango '

#21. Remove left-side spaces from " Banana"
u=" Banana"
u.lstrip()
'Banana'

#22. Remove right-side spaces from "Python "
v="Python "
v.rstrip()
'Python'

#23.Remove right-side spaces from "Hello World ".
w="Hello World "
w.rstrip()
'Hello World'

#24.Remove right-side spaces from "Orange ".
x="Orange "
x.rstrip()
'Orange'


#25. Check whether "Python" starts with "Py".
y="Python"
y.startswith("Py")
True


#26.Check whether "Programming" starts with "Pro"
z="Programming"
z.startswith("Pro")
True

#27. check whether "Hello World" starts with "hello"
a1="Hello World"
a1.startswith("hello")
False

#28.Check whether "Python" ends with "on".
b2="Python"
b2.endswith("on")
True

#29.Check whether "Programming" ends with "ing".
c3."Programming"
SyntaxError: invalid syntax
c3="Programming"
c3.endswith("ing")
True

#30. Check whether "Apple" ends with "LE".
d4="Apple"
d4.endswith("LE")
False
