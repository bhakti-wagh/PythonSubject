Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.



#Inbuilt Functions

#1.type()
#2.id()
#3.ord('character')
#4.chr(number)
#5.abs()
#6.round()
#7.isinstance(0
#8.len()
#9.max()
#10. min()
#11.sum()


#isinstance:-> to check the data type

#syntax:-> isinstance(value, datatype) -> single data type
#syntax:-> isinstance(value,(datatype1, datatype2...))-> multiple data type

isinstance(600,int)
True

isinstance(600,float)
False

isinstance(600,(int, float,complex,bool,str))
True

isinstance(600,( float,complex,bool,str))
False



#abs()-> absolute it convert a negative number to posititve number

x= -1235
abs(x)
1235

x=65464
abs(x)
65464

x= -545654
abs(x)
545654


#to convert postive to number (but it is not fixed function )

x=545

-abs(x)
-545


#round()--> before the if you are using odd number it always it will roundup to nex number
a=13.5
round(a)
14

#if i use even number output will be as it is

b=12.5
round(b)
12

round(17.4
    )
17

round(17.6)
18
>>> 
>>> round(23.5)
24
>>> 
>>> round(22.4)
22
>>> 
>>> round(8.4)
8
>>> round(8.9)
9
>>> 
>>> 
>>> 
>>> #max()--> maximum number
>>> t=[100,200,5,5.0,900,1000]
>>> max(t)
1000
>>> 
>>> #min()--> minumum number
>>> min(t)
5
>>> 
>>> #sum()-> to add element
>>> sum(t)
2210.0
