Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> # List Methods
>>> 
>>> #--->  Copy <---
>>> 
>>> #--> copy ---> 1. shallow copy --> 2.deep copy
>>> 
>>> #it will copytin grom variable to another variable
>>> #syntax--> new Var_Name= old Var_name
>>> 
>>> #Note:-> in Normal copy/copy both variable id address should be same.
>>> #If i dont modifiaction in old variable then new variable also affected
>>> 
>>> 
>>> #Ex :
>>> a=[10,20,30,40]
>>> 
>>> b=a
>>> 
>>> a
[10, 20, 30, 40]
>>> b
[10, 20, 30, 40]
>>> 
id(a)
1816662357888
id(b)
1816662357888



#modification in a variable

#append()----> var_name.append(element)

a.append(100)
a
[10, 20, 30, 40, 100]
b
[10, 20, 30, 40, 100]



#modification in b variable

#insert()---> var_Name.insert(position, value)

b.insert(3,200)
b
[10, 20, 30, 200, 40, 100]
a
[10, 20, 30, 200, 40, 100]


#modification in a variable without using  inbuilt function

#syntax:--> var_name[postion]=value

a
[10, 20, 30, 200, 40, 100]

a[1]
20
a[1]="Morning"
a
[10, 'Morning', 30, 200, 40, 100]
b
[10, 'Morning', 30, 200, 40, 100]

#modification in a variable without using  inbuilt function
#syntax:--> var_name[postion]=value

b
[10, 'Morning', 30, 200, 40, 100]

b[5]
100

b[5]='unique'
b
[10, 'Morning', 30, 200, 40, 'unique']

a
[10, 'Morning', 30, 200, 40, 'unique']


a[5]
'unique'

a[5]="evening"
a
[10, 'Morning', 30, 200, 40, 'evening']
b
[10, 'Morning', 30, 200, 40, 'evening']





# Copy method have two types ---> 1. Shallow copy   2. deep copy

# 1. Shallow Copy:-> It will copying from one variable to another variable

#Syntax :-->  NewVariableName = old_var_name.copy()

#Case--->01

x=["abc","xyz","mno", "Pqr"]

y=x.copy()

x
['abc', 'xyz', 'mno', 'Pqr']

y
['abc', 'xyz', 'mno', 'Pqr']

id(x)
1816706606656

id(y)
1816705485440



#Modification in x varible

x.insert(0,100)
x
[100, 'abc', 'xyz', 'mno', 'Pqr']

y
['abc', 'xyz', 'mno', 'Pqr']

#Modification using without ibuilt function

y[1]=200
y
['abc', 200, 'mno', 'Pqr']

x
[100, 'abc', 'xyz', 'mno', 'Pqr']


#in shallow copy if we are doing any modification then it will not affected to both variable




#Case-->02---> nested list--> list inside list

#Nested list id should be same but normal list id should be different
#if any modification done in nested list it will affect but outside nested list it will not affect


k=[1,2,3,[10,20,30]]
l=k.copy()

k
[1, 2, 3, [10, 20, 30]]
l
[1, 2, 3, [10, 20, 30]]



#completely list Id address----> id(Variable)
id(k)
1816706465216
id(y)
1816705485440

#Nested list id address---> id(var_Name[postion])

id(k[3])
1816662548992
id(l[3])
1816662548992


#modification in k variable
k
[1, 2, 3, [10, 20, 30]]

k[2]=300

k
[1, 2, 300, [10, 20, 30]]
l
[1, 2, 3, [10, 20, 30]]

#modification in l variable
l[0]=100
l
[100, 2, 3, [10, 20, 30]]

k
[1, 2, 300, [10, 20, 30]]


#Modification in Nested list


#Syntax:--> var_name[postion]=value

k
[1, 2, 300, [10, 20, 30]]

k[3]
[10, 20, 30]

k[3][0]="abc"
k
[1, 2, 300, ['abc', 20, 30]]

l
[100, 2, 3, ['abc', 20, 30]]

#Modification in Nested list in L variable

l[3][2]="Pyhton"
;
SyntaxError: invalid syntax
l
[100, 2, 3, ['abc', 20, 'Pyhton']]

k
[1, 2, 300, ['abc', 20, 'Pyhton']]


w=[100,500,"Walmart",["a","b","c","d"]]

n=w.copy()

w
[100, 500, 'Walmart', ['a', 'b', 'c', 'd']]
n
[100, 500, 'Walmart', ['a', 'b', 'c', 'd']]

id(w)
1816706703808
id(n)
1816706597824

#above is complete list id address (id(w) or  id(n))

#nested list id address

id(w[3])
1816706598976
id(n[3])
1816706598976

#modification in outside of nested list

w[1]="snap"
w
[100, 'snap', 'Walmart', ['a', 'b', 'c', 'd']]
n
[100, 500, 'Walmart', ['a', 'b', 'c', 'd']]


n[1]="XYZ"
n
[100, 'XYZ', 'Walmart', ['a', 'b', 'c', 'd']]
w
[100, 'snap', 'Walmart', ['a', 'b', 'c', 'd']]

#modification in  nested list

w[3]
['a', 'b', 'c', 'd']
w[3][0]= 10
w
[100, 'snap', 'Walmart', [10, 'b', 'c', 'd']]
n
[100, 'XYZ', 'Walmart', [10, 'b', 'c', 'd']]


n[3]
[10, 'b', 'c', 'd']
n[3][3]=40
n
[100, 'XYZ', 'Walmart', [10, 'b', 'c', 40]]
w
[100, 'snap', 'Walmart', [10, 'b', 'c', 40]]





#2.deep copy() ---> it will copying from one variable to another variable
#when we perfoming we have to perform 1 step

#step1---> it is mandatory to do

# from copy import deepcopy

#Syntax--> new_var_Name=deepcopy(old_Var_Name)

#Case -->01:

c=[10,100,200,300]

e=deepcopy(c)
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    e=deepcopy(c)
NameError: name 'deepcopy' is not defined

from copy import deepcopy

e=deepcopy(c)

id(c)
1816706612416
id(e)
1816706740288



#Modification in c variable'

c[2]="abc"
c
[10, 100, 'abc', 300]
e
[10, 100, 200, 300]

# it will not affect to e variable because id address be differnt


#Modifcarion in nested list

from copy import deepcopy

r=[10,20,30,40,['a', 'b', 'c']]
u=deepcopy(r)

r
[10, 20, 30, 40, ['a', 'b', 'c']]
u
[10, 20, 30, 40, ['a', 'b', 'c']]

#Complete list id :-->
id(r)
1816706741376
id(u)
1816706464896

#Nested list id:-->
id(r[4])
1816706702656
id(u[4])
1816706692864


#Modification in nested list

r[4]
['a', 'b', 'c']
r[4][1]=100
r
[10, 20, 30, 40, ['a', 100, 'c']]
u
[10, 20, 30, 40, ['a', 'b', 'c']]
