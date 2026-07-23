Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Logical Operator:->

#There are 3 types of logical operators.
#1.Logical and (and)
#2.Logical or (or)
#3.Logical not (not)

#All logical operators are keywords

#1.Logical and (and):->
# It will perform logical and operation for the given operand
#Syntax:-> op1 and op2

#Case 01:-> If operand1 is non default value then oytput will be always         "operand2"

#Case 02:-> If operand1 is default value then o/p will be "operand1"


#EX:

True and False
False

0 and 1
0

90 and 45
45

78 and 63
63

{} and 78
{}

() and {}
()

(1,)and'shruuu'
'shruuu'



#2.Logical or (or):->
#It will perform logical or operation for the given operand.

#Syntax:->  op1 or op2

##Case 01:-> If operand1 is non default value then oytput will be always "operand1"
#Case 02:-> If operand1 is default value then o/p will be "operand2"

(1,)or'shruuu'
(1,)

()or{}
{}

0 or 1
1

90 or 45
90

#3.Logical not (not):->
#Logical not will work only on one operand
#Syntax:-> not op1

#It will the result in boolean formal[either True/False]

#EX:

not True
False

not 5
False

not ''
True

not 0
True

not 'vii'
False
>>> 
>>> not {}
True
>>> 
>>> not ()
True
>>> 
>>> not  9 and 0
False
>>> 
>>> 12 and 7
7
>>>  12 and 7 or 56
...  
SyntaxError: unexpected indent
>>> 12 and 7 or 56
7
>>> 
>>> not set()
True
>>> 
>>> 
>>> {} and ''
{}
>>> {} or ''
''
