Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> y="Python"
>>> y[2]
't'
>>> y[-3]
'h'
>>>  #Indexing
>>> #the process of extracting single-single character
>>> # two types ----->  forward --> left-> right -> always start from 0
>>> #           -----> backward ---> right-> left --> always start from -1
>>> 
>>> t="Good Boy"
>>> t[4]
' '
>>> t[-5]
'd'
>>> t[0]
'G'
>>> t[-8]
'G'
>>> 
>>> 
>>> # what is meaning of indexing what is the drawback of indexing??
>>> # --> the process of extractin single-single characgter , we can't fetch the multiple character at time it is
>>> # drawback
>>> 
>>> len(t)
8
>>> s ="Well come to all"
>>> s[2]
'l'
s[1]
'e'
s[7]
'm'

s[15]
'l'
s[16]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s[16]
IndexError: string index out of range

s[-15]
'e'

s[-11]
'c'
s[-14]
'l'
s[-3]
'a'
s[13]
'a'
s[10]
't'
s[-5]
'o'
s[-6]
't'
s[t]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s[t]
TypeError: string indices must be integers, not 'str'
s[4]
' '
s[-4]
' '


d="First Step to learn new things"

d[2:5:1]
'rst'

d[11:13:1]
'to'

d[20:23:1]
'new'

d[27:30:1]
'ngs'

d[6:10:3]
'Sp'

d[0:5:4]
'Ft'

d[0:5:2]
'Frt'

d[14:19:4]
'ln'

d[18:23:4]
'nw'
d[20:23:2]
'nw'


d[24:29:2]
'tig'







