Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


#ASCII VALUE


#A-Z(65-90)
#a-z(97-122)
#0-9(48-57)

#ASCII -> American standart code for International interchage value
#Ascii--> two types--> 1.ord() 2.chr()

#Ord() --> ordinal --> always only one character but in quotes
#Syntax--> ord('character')--> o/p Number

ord("A)
    
SyntaxError: unterminated string literal (detected at line 1)
ord("A")
    
65


ord("B")
    
66

ord("C")
    
67

ord("Z")
    
90

ord("a")
    
97
ord("z")
    
122


#2.chr()--> character  -> here we pass number without qoutes
...     
>>> #Syntax--> chr(number)-->o/p character
...     
>>> 
>>> chr(65)
...     
'A'
>>> chr(90)
...     
'Z'
>>> 
>>> chr(97)
...     
'a'
>>> 
>>> chr(122)
...     
'z'
>>> 
>>> ord('e')
...     
101
>>> 
>>> ord('y')
...     
121
