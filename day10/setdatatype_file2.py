Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Intersection_update()

#syntax:-> var1.intersection_update(var2) :-> var1--> orginal set, var2--> reference set

#intersection update means always it consider orgianal set

x={100,200,300,400,500}
y={300,600,700}

x.intersection_update(y) #here first show blankspace

x
{300}
#when we calling x it will show updated one not original one
x
{300}

y.intersection_update(x)
y
{300}
y
{300}





#symmetric_difference()
#Syntax:->  var1.symmetric_difference_update(var2)

#here check uncommon element form both side but it will consider updated one always

x={"morning","evening","hi","bye","hello","snap"}
y={"insta","walmart","good","bad","hello","snap","hi"}

x.symmetric_difference_update(y)
x
{'insta', 'bad', 'morning', 'evening', 'walmart', 'bye', 'good'}
x
{'insta', 'bad', 'morning', 'evening', 'walmart', 'bye', 'good'}
y
{'hello', 'snap', 'insta', 'walmart', 'bad', 'good', 'hi'}
>>> 
>>> y.symmetric_difference_update(x)
>>> y
{'hello', 'evening', 'bye', 'hi', 'snap', 'morning'}
>>> y
{'hello', 'evening', 'bye', 'hi', 'snap', 'morning'}
>>> x
{'insta', 'bad', 'morning', 'evening', 'walmart', 'bye', 'good'}
>>> 
>>> 
>>> #difference_update:-> var1.difference_update(var2)
>>> 
>>> #here also check uncommon element for origial set but it will always consider latest one
>>> 
>>> x={400,500,900,600}
>>> y={500,200,100,600}
>>> 
>>> x.difference_update(y)
>>> 
>>> x
{400, 900}
>>> 
>>> y.difference_update(x)
>>> y
{600, 100, 500, 200}
