Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


#Membership Operators:->

# It will check whether the specified value is present in the collection  or not
#There are 2 types of memebership operator;
#1.in operator
#2.not in operator

#1.in operator:-> It will give the result True only if the value is present in the colle.
#Syntax:-> value in collection

#We can check:
#1.value in collection
#2.collection in nested collection
#but not collection in collection and value in individual D.T#1.in operator


#2.not in operator:-> It will give the result as True only if value is not present in the given collection .
>>> 
>>> #Syntax:-> value not in collection
>>> 
>>> 
>>> 10 in (45,10,56)
True
>>> 
>>> [10,20] in [10,20,30]
False
>>> 
>>> [10,20] in [[10,20],30]
True
>>> 
>>> '3' in '3456'
True
>>> 
>>> 
>>> 10 not in (45,10,56)
False
>>> 
>>> [10,20] not in [10,20,30]
True
>>> 
>>> 34 not in [10,20]
True
>>> 
