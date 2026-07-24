Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> #Input & Output:->
>>> 
>>> #input():-> It is a inbuilt method used to take input from the user.
>>> #       Syntax:->   var = dataType(int('msg'))
>>> #       Ex:->       a = int(input('Enter Number:'))
>>> 
>>> #By default input() will take string as default value.
>>> 
>>> #eval():->  It is a inbuilt function used to take input from the user, sepecially for                   Collection Data type.
>>> #Syntax:->  varname = eval(input('msg'))
>>> 
>>> 
>>> #Ex:->
>>> 
>>> 
>>> #For single value D.T
>>> 
>>> a=int(input('Enter int number: '))
Enter int number: 45
>>> a
45
>>> 
a=float(input('Enter float number:'))
Enter float number:45.5
a
45.5

a=complex(input('Enter complex number:'))
Enter complex number:4+5j
a
(4+5j)

a=bool(input('Enter bool value:'))
Enter bool value:1
a
True


#For collection D.T (eval())

a=eval(input('Enter list values:'))
Enter list values:[78,98,45,'df']
a
[78, 98, 45, 'df']

a=eval(input('Enter tuple values:'))
Enter tuple values:45,'a',65,'sd'
a
(45, 'a', 65, 'sd')

a=eval(input('Enter set values:'))
Enter set values:{45,54}
a
{45, 54}

a=eval(input('Enter dict values:'))
Enter dict values:{4:40,5:50}
a
{4: 40, 5: 50}

#for string we don't have to define any datatype because input() it takes bydefault string

a=input('Enter string values:')
Enter string values:45
a
'45'
a
'45'



a=bool(input('Enter bool number:'))
Enter bool number:True
a
True

a=bool(input('Enter bool number:'))
Enter bool number:False
a
True
