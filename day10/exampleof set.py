Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

d={"morning","evening","hi","bye","hello","snap"}
e={"insta","walmart","good","bad","hello","snap","hi"}

#intersection set

d.intersection(b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d.intersection(b)
NameError: name 'b' is not defined
d.intersection(e)
{'snap', 'hi', 'hello'}

d
{'hello', 'snap', 'bye', 'evening', 'morning', 'hi'}

e
{'hello', 'good', 'insta', 'snap', 'walmart', 'bad', 'hi'}

#intersection_update

d.intersection_update(e)
d
{'snap', 'hi', 'hello'}
d
{'snap', 'hi', 'hello'}
e
{'hello', 'good', 'insta', 'snap', 'walmart', 'bad', 'hi'}

e.intersection_update(d)
e
{'hello', 'snap', 'hi'}
e
{'hello', 'snap', 'hi'}
d
{'snap', 'hi', 'hello'}



#symmetrice_difference

>>> d.symmetric_difference(e)
set()
>>> 
>>> e.symmetric_difference(d)
set()
>>> 
>>> 
>>> x={"morning","evening","hi","bye","hello","snap"}
>>> y={"insta","walmart","good","bad","hello","snap","hi"}
>>> 
>>> x.symmetric_difference(y)
{'insta', 'evening', 'morning', 'good', 'bye', 'walmart', 'bad'}
>>> 
>>> y.symmetric_difference(y)
set()
>>> y.symmetric_difference(x)
{'insta', 'evening', 'morning', 'good', 'bye', 'walmart', 'bad'}
>>> 
>>> #symmetric_difference_update
>>> 
>>> x.symmetric_difference_update(y)
>>> x
{'insta', 'evening', 'morning', 'good', 'bye', 'walmart', 'bad'}
>>> x
{'insta', 'evening', 'morning', 'good', 'bye', 'walmart', 'bad'}
>>> 
>>> y
{'hello', 'good', 'insta', 'snap', 'walmart', 'bad', 'hi'}

y.symmetric_difference_upate(y)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    y.symmetric_difference_upate(y)
AttributeError: 'set' object has no attribute 'symmetric_difference_upate'. Did you mean: 'symmetric_difference_update'?
y.symmetric_difference_upate(x)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    y.symmetric_difference_upate(x)
AttributeError: 'set' object has no attribute 'symmetric_difference_upate'. Did you mean: 'symmetric_difference_update'?
y.symmetric_difference_update(x)
y
{'evening', 'hi', 'hello', 'morning', 'bye', 'snap'}
y
{'evening', 'hi', 'hello', 'morning', 'bye', 'snap'}
