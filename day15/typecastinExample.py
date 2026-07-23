Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> a=123
>>> 
>>> int(a)
123
>>> 
>>> float(a)
123.0
>>> 
>>> complex(a)
(123+0j)
>>> 
>>> bool(a)
True
>>> 
>>> str(a)
'123'
>>> 
>>> 
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable

tuple(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable

set(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable

dict(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable


b=230.40

int(b)
230

float(b)
230.4

complex(b)
(230.4+0j)

bool(b)
True

str(b)
'230.4'

list(b)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable

tuple(b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable

set(b)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable



c=3+2j
c
(3+2j)

int(c)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

float(c)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'

bool(c)
True

str(c)
'(3+2j)'

list(c)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable


c=True

int(c)
1

float(c)
1.0

complex(c)
(1+0j)


str(c)
'True'

list(c)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list(c)
TypeError: 'bool' object is not iterable

tuple(c)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    tuple(c)
TypeError: 'bool' object is not iterable




x="hi"

int(x)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: 'hi'

float(x)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    float(x)
ValueError: could not convert string to float: 'hi'

complex(x)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    complex(x)
ValueError: complex() arg is a malformed string

bool(x)
True

list(x)
['h', 'i']

tuple(x)
('h', 'i')

set(x)
{'i', 'h'}


dict(x)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dict(x)
ValueError: dictionary update sequence element #0 has length 1; 2 is required


z=[10,20]

int(z)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    int(z)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

complex(z)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    complex(z)
TypeError: complex() first argument must be a string or a number, not 'list'

bool(z)
True

str(z)
'[10, 20]'

tuple(z)
(10, 20)

set(z)
{10, 20}

dict(z)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    dict(z)
TypeError: cannot convert dictionary update sequence element #0 to a sequence


s=(40)

int(s)
40

s=(40,50)
int(s)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'

float(s)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'tuple'

complex(c)
(1+0j)

bool(c)
True

str(c)
'True'

complex(s)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'tuple'

bool(s)
True
str(s)
'(40, 50)'


v={3,4}
int(v)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    int(v)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'

float(v)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    float(v)
TypeError: float() argument must be a string or a real number, not 'set'

complex(v)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    complex(v)
TypeError: complex() first argument must be a string or a number, not 'set'

bool(v)
True

str(v)
'{3, 4}'

list(v)
[3, 4]

tuple(v)
(3, 4)


dict(v)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    dict(v)
TypeError: cannot convert dictionary update sequence element #0 to a sequence



d={1:20}

int(d)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'

bool(d)
True

str(d)
'{1: 20}'

list(d)
[1]

tuple(d)
(1,)

set(d)
{1}

