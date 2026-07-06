Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


#String Method

# 1. upper() -> syntax ---> var_name.upper()  or "String".upper()

a = "python"
a.upper()
'PYTHON'
"python".upper()
'PYTHON'


# 2. lower() -> synatx -> var.name()  or "String".lower()

a="PYTHON"
a.lower()
'python'

"PYTHON".lower()
'python'


#3. swapcase() -> synatx -> var_name.swapcase() or "String".swapcase()
# uppercase -> lowercase
# lowercase -> uppercase

s ="Python CLASS"
s.swapcase()
'pYTHON class'


# 4.capitalize() -> syntax -> var_name.capitalize() or "String".capitalize()
# in the given string only 1st character becomes uppercase

s ="good morning"
s.capitalize()
'Good morning'

# 4.title()  -> syntax --> var_name.title() or "String".title()
>>> # first word 1st character be uppercase and second word 2nd character be uppercase  (if in given statement the mut
>>> #multiple words then all words first charater be in uppercase
>>> 
>>> a = "hi hello how are you"
>>> a.title()
'Hi Hello How Are You'
>>> 
>>> b="good morning "
>>> b.title()
'Good Morning '
>>> 
>>> #string data type is a immutable data type
>>> # immutable data type -->
>>> # here we can't change orginal object but we can do the modification.
>>> 
>>> 
>>> a =" evening" #--> orginal object
>>> a.upper() #--> modification data
' EVENING'
>>> 
>>> a
' evening'
>>> #it gives only orginal object because of immutable data type
>>> 
>>> 
>>> m="pyThOn" #--> orginal object
>>> m.captialize() #--> modification data
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    m.captialize() #--> modification data
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
