Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> #Sort Method in List
>>> 
>>> #Sort()-> by default it will conver (lower)ascending to (bigger)decending
>>> #Sort()--> it will accept only homogeneous element(same type of data)
>>> 
>>> #Syntax-->  1. variableName.sort()
>>> #           2. variableName.sort(reverse=False)(False--< asc to dec)
>>> #           3. VariableName.sort(reverse=True) (True--< dec to asc)
>>> 
>>> 
>>> #sort()
>>> 
>>> c=[100,34,1,0.4,2,65,55,35,88]
>>> c.sort()
>>> c
[0.4, 1, 2, 34, 35, 55, 65, 88, 100]
>>> c.sort(reverse=False)
>>> c
[0.4, 1, 2, 34, 35, 55, 65, 88, 100]
>>> 
>>> c.sort(reverse=True)
>>> c
[100, 88, 65, 55, 35, 34, 2, 1, 0.4]
