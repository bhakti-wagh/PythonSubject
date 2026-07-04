Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


# what is the meaning of keywords ???

# how to get all 35 keywords in group format??

## how to get all 35 keywords in group format??# how to get all 35 keywords in group format??
help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 


#how to get all 35 keywords in list format??

#need to follow two step
import keyword

keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

>>> 
>>> #we can't assign any value to the keywords  ?
>>> # not = 100 -> synatx error throw
>>> 
>>> 
>>> #how to check whether the given keyword is valid or not
>>> #here we need to follow the syntax
>>> #import keyword
>>> #keyword.iskeyword("keyword")
>>> 
>>> # note --> if the given keyword id valid --> output should be true
>>> #          if the given keyword is invalid ---> output should be false
>>> 
>>> import keyword
>>> keyword.iskeyword('python')
False
>>> 
>>> import keyword
>>> keyword.iskeyword('else')
True
>>> 
>>> import keyword
>>> keyword.iskeyword('sql')
False
>>> 
>>> import keyword
>>> keyword.iskeyword('if')
True
>>> 
>>> #in python 35 keyword are there but among them 3 are special keywords ( True , False, None --> because they in uppercase)
>>> 

# variables rule
# -> In the place of variable we can use alphatbets (uppercase / lowercase/ combination uppercase+lowercase
#-> In the place of variable should not start with number but we can use number in between or last
#-> In the place of variable we can't use special character except underscore(_)
#-> in the place of variable we can use unlimited character but according to role we can pass 79 character
#-> Rule_name-> PEP8 ( it is nothig but rule p-> python , E-Enhancement, p-proposal , 8 -> version) -> if you want to follow rule the guidline

