Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Identifiers
#identifiers is nothing but the name of python program like variable, module, object


#Rule

# 1. Identitfiers part we can use alphabet (uppercase / lowercase/ combintion
# 2. In Identitfiers part shouldn't start with number but we can use in  between /last

45ab = 'hi'
SyntaxError: invalid decimal literal
ab45='hi'
ab45
'hi'
>>> a2b3=9000
>>> a2b3
9000
>>> 
>>> # 3. In Identitfiers part we can't use special character excep underscore(_)
>>> # 4. In Identifiers part we can't use keywords
>>> # 5. In Identifiers part we can pass unlimited character but according to the pep8 rule we can pass 79 character
>>> 
>>> 
>>> #how to check whether the given identifiers is valid or not
>>> # "identifier_Part".isidentifier()
>>> 
>>> #-> note: if the rule is valid output should be  --> True
>>> 
>>> #-> note: if the rule is In-valid output should be  --> False
>>> 
>>> 
>>> #Example :
>>> "ca$h".isidentifier()
False
>>> 
>>> "_".isidentifier()
True
>>> "123abc".isidentifier()
False
>>> "abc223".isidentifier()
True
>>> ->difference between in variable $ identififer
SyntaxError: invalid syntax
>>> variable is container where we store value or information
SyntaxError: invalid syntax
