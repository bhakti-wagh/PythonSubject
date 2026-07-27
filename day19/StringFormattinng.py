Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#String Formatting

# inserting the variable/ values into a string

#Types of String formatting
#1.Formatting with placeholder(%):->
# %s---> String Data Type
# %d---> Integer Data type
# %f---> Float Data Type

s="My name is %s and my age is %d"%("bhakti",22)
print(s)
My name is bhakti and my age is 22


b="My bank balance is  %f"%(35.12)#by default it take 000
print(b)
My bank balance is  35.120000

b="My bank balance is  %2f"%(35.12)
print(b)
My bank balance is  35.120000
b="My bank balance is  %.2f"%(35.12)
print(b)
My bank balance is  35.12

b="My bank balance is  %.1f"%(35.12)
print(b)
My bank balance is  35.1



e="My subject Name is %s and total score is  %d and current CGPI is %.2f"%("Python",99,8.25)

print(e)
My subject Name is Python and total score is  99 and current CGPI is 8.25





#2. .Format Method({}):->

a="My name is {} and My age is {}".format("Bhakti",22)
print(a)
My name is Bhakti and My age is 22


#here we can replace the data
a="My name is {} and My age is {}".format(22,"Bhakti")

print(a)
My name is 22 and My age is Bhakti


#we can pass index/postion for replace or output
a="My name is {1} and My age is {0} and subject is {2}".format(22,"Bhakti","pyhotn")
print(a)
My name is Bhakti and My age is 22 and subject is pyhotn
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #3. Formatting with f-literals({}):->
>>> #
>>> # inside the {} we have to pass variable Name
>>> # Before the quotes we have to mention either F/f -> it is very imp for programming
>>> 
>>> name="joy"
>>> age=35
>>> 
>>> msg= f"My name is {name} and My age is {age}"
>>> print(msg)
My name is joy and My age is 35
>>> 
>>> msg= F"My name is {name} and My age is {age}"
>>> print(msg)
My name is joy and My age is 35
>>> 
>>> msg
'My name is joy and My age is 35'
