Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> # 1. Join() -> it use to join string
... #  syntax -->
... #              'JoiningCharcter'.join(iterable)
... 
... 
... 
... 
... #Ex :
... 
>>> 
>>> a ="Good Morning"
>>> "*".join(a)
'G*o*o*d* *M*o*r*n*i*n*g'
>>> 
>>> 
>>> #join --> in the given string if you want to add any character --< in the start or end we cannot add character but at the between we can add
>>> # we can convert list data into string use ("")
>>> 
>>> #EX :
>>> s = ["Xyz" , "Abc", "Fgh"]
>>> "".join(s)
'XyzAbcFgh'
>>> #like this we can convert  list data into string format
>>> 
>>> #-> we can pass any character (alphabets/number/special character/ also list type , tuple type
>>> 
>>> x='abc'
"$".join(x)
'a$b$c'

b="bhakti"
"*".join(b)
'b*h*a*k*t*i'

c=["Python","Java","C/C++"]
" ".join(c)
'Python Java C/C++'

"-".join(c)
'Python-Java-C/C++'

"---".join(c)
'Python---Java---C/C++'

d=("Walmart","join","upper")
" ".join(d)
'Walmart join upper'
"-".join(d)
'Walmart-join-upper'
"---".join(d)
'Walmart---join---upper'


e={"abcd","defg","hijkl"}
" ".join(e)
'hijkl defg abcd'
"-".join(e)
'hijkl-defg-abcd'
"---".join(e)
'hijkl---defg---abcd'

w={"abc":"xyz", "hello":"hi","get":"key"}
" ".join(w)
'abc hello get'
"-".join(w)
'abc-hello-get'
"---".join(w)
'abc---hello---get'
w
{'abc': 'xyz', 'hello': 'hi', 'get': 'key'}


#iterable-> also called as collection data type , multivalue data type
#Note : in dictionary data type while doing opertion only it will visible key layer because all values are depending on key







# 2.split() --> syntax---> var_Name.split(separater,maxsplit)








# forward --> left to right

#3. rsplit()--> syntax --> var_Name.rsplit(separater,maxsplit)
# forward --> right to left



# split -> return type -> list

#ex :

s1 ="hi hello  python"
s1.split()
['hi', 'hello', 'python']

s2 ="Programming class"
s2.split('m')
['Progra', '', 'ing class']
s2.rsplit('m',1)
['Program', 'ing class']
s2.split('m',1)
['Progra', 'ming class']




#4. remove prefix() --> syntax ---> var_Name.removeprefix('character')
#5. remove suffix() --> syntax ---> var_name.removesuffix('character')

#remove prefix --> it used to if you want to delete bgeining character -->

s="python"
s.removeprefix("p")
'ython'

s2
'Programming class'

s2.removeprefix("Progr")
'amming class'
# if you want to delete middle character the you have to mention also begining character

#removesuffiex---> if you want to delete ending character

s2.removesuffix("ing class")
'Programm'
'Programm'
'Programm'


n="GoodMorning"
n.split('o',5)
['G', '', 'dM', 'rning']
n.rsplit('o',5)
['G', '', 'dM', 'rning']
n.rsplit('o',3)
['G', '', 'dM', 'rning']
n.split('o',3)
['G', '', 'dM', 'rning']
n.rsplit('o',1)
['GoodM', 'rning']
n.split('o',2)
['G', '', 'dMorning']
n.split('o',1)
['G', 'odMorning']



p="class program"
n.split()
['GoodMorning']

n.split('a',2)
['GoodMorning']









p
'class program'
p.split()
['class', 'program']

p.split('a',2)
['cl', 'ss progr', 'm']

p.split('a',1)
['cl', 'ss program']

p.rsplit('a',1)
['class progr', 'm']
p.rsplit('a',2)
['cl', 'ss progr', 'm']



