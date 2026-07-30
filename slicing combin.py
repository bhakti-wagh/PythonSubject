Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing combination

#forward:->

x="Morning"

x[1:-3:1]
'orn'

x[-6:4:1]
'orn'


x[3:-1:1]
'nin'

x[-4:6:1]
'nin'

x[-3:7:1]
'ing'


y="Good luck"

y[1:-4:1]
'ood '

>>> y[-8:4:1]
'ood'
>>> 
>>> 
>>> #Luc
>>> 
>>> y[5:-1:1]
'luc'
>>> 
>>> y[-4:8:1]
'luc'
>>> 
>>> 
>>> #doo
>>> 
>>> y[3:-9:-1]
'doo'
>>> 
>>> y[-6:0:-1]
'doo'
>>> 
>>> y[7:-5:-1]
'cul'
>>> 
>>> y[-2:4:-1]
'cul'
