Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Dictionary data type

# - combination of key and value pair
# - Boundary condition :-> {}
# - internally we can represent as a object:-> dict()
# - Syntax :->
#             var_Name={key1:value, key2:value,Key3:value....}

#How to create a empty dictionary by normal way
a={}
a
{}

#How to create a empty dictionary by Object
dict()
{}

e=dict()
e
{}

#Dictionary data types means combination of key and value pair

# in dictionary data types in key part alwways we have to pass
# Single_Vale_datatype and immutable data type

#singe_Value_datatype:--> int/float/comples/bool
#immutable data type:--> string/tuple

#Note1:--> In key part if we pass mutable data type it will
#           show unhasable type of error.

#Note2:--> In value part you can pass any python data type.

a={1:10,False:True, 3.4:"abc",2+4j:100,"hii":"Hello",(1,2,3):900}
a
{1: 10, False: True, 3.4: 'abc', (2+4j): 100, 'hii': 'Hello', (1, 2, 3): 900}


a={1:10,False:True, 3.4:"abc",2+4j:100,"hii":"Hello",(1,2,3):900,[10,20,30]:500}
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a={1:10,False:True, 3.4:"abc",2+4j:100,"hii":"Hello",(1,2,3):900,[10,20,30]:500}
TypeError: unhashable type: 'list'
#here I pass list that's why it will show error


#Dictionary data type is ordered data type
#Dictionary is Mutable data type
#in Dictionary we cant do indexing and slicing
#In Dictionary in key part if you want to pass multiple element here we have to use ()
#_> if you using() it called composite key

#Another name of Tuple is composite key

e={10:100,78:900,234:899,100:200}
len(e)
4
#len function it consider pair


#In dictionary data type How to access value outside ???
e={10:100,78:900,234:899,100:200}
e
{10: 100, 78: 900, 234: 899, 100: 200}

e[78]
900

#Syntax:---> var_Name[key]

e[100]
200

e[10]
100

e[90]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    e[90]
KeyError: 90
#If specified key is not present it will show key error
#and we can't to fetch mutlitple key at time




#2nd : -> using get() Method
#syntax :->  var_Name.get(key,defaultvalue)

e
{10: 100, 78: 900, 234: 899, 100: 200}

e.get(10)
100

e.get(100)
200

e.get(4654)
#here if specified key is not present then it will show blank space or default value

e.get(4565,"Key is not present")
'Key is not present'

e.get(10,1000)
100
e.get(234,"new")
899

e.get(333,"Think")
'Think'


dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']



#3rd setdefault()  method
# Syntax :->  var_name.setdefault(key,defaultvalue)

e
{10: 100, 78: 900, 234: 899, 100: 200}

e.setdefault(10)
100

e.setdefault(888)
#here if specified key is not present then it will not show any error but it will show blank space ,,, at that key is added at last of dictionary  with default value

e
{10: 100, 78: 900, 234: 899, 100: 200, 888: None}
{10: 100, 78: 900, 234: 899, 100: 200, 888: None}
{10: 100, 78: 900, 234: 899, 100: 200, 888: None}


e.setdefault(777,"newValue")
'newValue'
e
{10: 100, 78: 900, 234: 899, 100: 200, 888: None, 777: 'newValue'}
#Like this setdefault work




a={24:500,23:600,22:700,21:800,20:900}
a
{24: 500, 23: 600, 22: 700, 21: 800, 20: 900}

#To access value in dictioanry

#1st is without using inbuilt function:-> key and value syntax
# Syntax:-> varName[key]

a[24]
500
a[22]
700

#2nd with get() method:->  varName.get(key,defaultValue)
a.get[24]
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.get[24]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.get(24)
500

a.get(22)
700

#3rd with setdefault() method:-> varName.setdefault(key,defaultvalue)
a.setdefault(24)
500
a.setdefault(22)
700
a.setdefault(19,"setdefualtvalue")
'setdefualtvalue'
a
{24: 500, 23: 600, 22: 700, 21: 800, 20: 900, 19: 'setdefualtvalue'}


#In dictionary data type we can't do directly indexing and slicing but we can do indirect

w={10:"hello",20:"Python"}

w[10]
'hello'
w[10][0]
'h'

w[10][::-1]
'olleh'

w[89]
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    w[89]
KeyError: 89
w[20]
'Python'

w[20][::-1]
'nohtyP'

a
{24: 500, 23: 600, 22: 700, 21: 800, 20: 900, 19: 'setdefualtvalue'}

#If you want to print all key which present in dictionary data

#Syntax:--> varName.keys()

a.keys()
dict_keys([24, 23, 22, 21, 20, 19])

#If you want to print all values which present in dictionary data
#Syntax:--> varName.values()

a.values()
dict_values([500, 600, 700, 800, 900, 'setdefualtvalue'])

#If you want to print all key and values theb
#Syntax:-->  varName.items()

a.items()
dict_items([(24, 500), (23, 600), (22, 700), (21, 800), (20, 900), (19, 'setdefualtvalue')])



# To add Element in dictionary data type

#1. without using inbuilt function--: we can add only one one pair
# Syntax:  varName[key]=value

#2. update() method--: we can add multiple pair at time
# Syntax: varName.update({Key1:value,Key2:value....})


x={}
x
{}

x[10]=100
x
{10: 100}

x[20]=200

x.update({30:300})
x
{10: 100, 20: 200, 30: 300}

x.update({40:400,50:500})
x
{10: 100, 20: 200, 30: 300, 40: 400, 50: 500}



#To delete element in dictionary data type

#1. pop()--> varName.pop(key,defaultvalue)
#-> in pop method we can delte only one one key pair

# if we not pass any key into pop it will show Error it is mandatory to filed
#If specified key is not present it will show keyError  to avoid Error pass defaultvalue

x
{10: 100, 20: 200, 30: 300, 40: 400, 50: 500}

x.pop()
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    x.pop()
TypeError: pop expected at least 1 argument, got 0
#like this error will come

x.pop(10)
100
x
{20: 200, 30: 300, 40: 400, 50: 500}

x.pop(300)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    x.pop(300)
KeyError: 300
x.pop(300,"key is not present")
'key is not present'




#2. popitem():--> varname.popitem()--> it will atomatically delete last element
#--< and output will show in Tuple Form

x
{20: 200, 30: 300, 40: 400, 50: 500}

x.popitem()
(50, 500)
x
{20: 200, 30: 300, 40: 400}




h={1:2,4:5,8:9}
g=h

id(g)
2417573625600
id(h)
2417573625600

g
{1: 2, 4: 5, 8: 9}

h
{1: 2, 4: 5, 8: 9}

g[4]=10
g
{1: 2, 4: 10, 8: 9}
h
{1: 2, 4: 10, 8: 9}

#In dictionary we have normal copy() method

h.update({8:20})
h
{1: 2, 4: 10, 8: 20}
g
{1: 2, 4: 10, 8: 20}

h.update({"abc":"def"})
h
{1: 2, 4: 10, 8: 20, 'abc': 'def'}
>>> g
{1: 2, 4: 10, 8: 20, 'abc': 'def'}
>>> 
>>> 
>>> 
>>> 
>>> #Pipline Operator(|)-> it will add two variables
>>> 
>>> h|g
{1: 2, 4: 10, 8: 20, 'abc': 'def'}
>>> 
>>> 
>>> #Unpacking--< **
>>> x={**a,**b}
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    x={**a,**b}
NameError: name 'b' is not defined
>>> x={**a,**h}
>>> x
{24: 500, 23: 600, 22: 700, 21: 800, 20: 900, 19: 'setdefualtvalue', 1: 2, 4: 10, 8: 20, 'abc': 'def'}
>>> 
>>> 
>>> 
>>> 


#fromkeys()

#The process of converting from other data type to dictionary data type

#syntax:-->  dict.fromkeys(iterable,fillvalue)

z="pyhton"
dict.fromkeys(z)
{'p': None, 'y': None, 'h': None, 't': None, 'o': None, 'n': None}

dict.fromkeys(z,10)
{'p': 10, 'y': 10, 'h': 10, 't': 10, 'o': 10, 'n': 10}

#here keys are mandatory and values are not mandatory


l=[1,2,3,4]
dict.fromkeys(l)
{1: None, 2: None, 3: None, 4: None}

d=(100,200,"abc","xyz")
dict.fromkeys(d)
{100: None, 200: None, 'abc': None, 'xyz': None}


dict.fromkeys(d,"data")
{100: 'data', 200: 'data', 'abc': 'data', 'xyz': 'data'}
