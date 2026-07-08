Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


#1. convert to uppercase
a="python"
a.upper()
'PYTHON'


#2. convert to lowercase
b="HELLO"
b.lower()
'hello'


#3.convert to title case
c="my name is bhakti"
c.title()
'My Name Is Bhakti'

#4.Capitalize first letter
d="welcome"
d.capitalize()
'Welcome'

#5.Swap uppercse to lowercase
e="PyThOn"
e.swapcase()
'pYtHoN'

#6.Count letter 'a'
f="banana"
f.count('a')
3

#7.count letter 'p'
g="apple pie"
g.count('p')
3

#8.convert a sentence to uppercase
h="i love coding"
h.upper()
'I LOVE CODING'

#9.convert a sentence to lowercase
i="PYTHON IS EASY"
i.lower()
'python is easy'


#10. Title case a sentence
j="leaning python step by step"
j.title()
'Leaning Python Step By Step'

#11. Capitalize a city name
k="punt"
k.capitalize()
'Punt'

#12. Swap case of word
l="HeLLo
SyntaxError: unterminated string literal (detected at line 1)
#12. Swap case of word
l="HeLLo"
l.swapcase()
'hEllO'


#13. count spaces
m="I Love Python"
m.count()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    m.count()
TypeError: count expected at least 1 argument, got 0
#13. count spaces
m="I Love Python"m.count()
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax



#13. count spaces
m="I Love Python"
m.count("")
14
m.count(" ")
2
#only tab space it check


#14.count letter 'o'
n="programming"
n.count('o')
1

#15.Uppercase a mixed word
o="PyThOn
SyntaxError: unterminated string literal (detected at line 1)
o="PyThOn"
o.upper()
'PYTHON'

#16.lowercase a mixed word
>>> p="PyThOn"
>>> p.lower()
'python'
>>> 
>>> 
>>> #17. Title case a movie name
>>> q="3 idiots"
>>> q.title()
'3 Idiots'
>>> 
>>> 
>>> #18.Capitalize a sentence
>>> r="python is powerful
SyntaxError: unterminated string literal (detected at line 1)
>>> r="python is powerful"
>>> r.capitalize()
'Python is powerful'
>>> 
>>> 
>>> #19.Swap case of sentence
>>> s="Python Is Fun"
>>> s.swapcase()
'pYTHON iS fUN'
>>> 
>>> 
>>> #20. count letter 'n'
>>> v="banana"
>>> v.count('n')
2
