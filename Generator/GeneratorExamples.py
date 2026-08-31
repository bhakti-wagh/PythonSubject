'''
1.wap to generate a+b,a-b,a*b,a/b by taking
a and b from user
'''
'''
#using return keyword in function

def operation():
    a=eval(input("Enter a number1:"))
    b=eval(input("Enter a number2"))

    return a+b,a-b,a*b,a/b

oper=operation()

print(oper)#(15, -5, 50, 0.5)

#Using yield keyword and next() in generator

def operation():
    a=eval(input("Enter a number1:"))
    b=eval(input("Enter a number2:"))

    yield a+b,a-b,a*b,a/b #At time o/p print

oper=operation()

print(next(oper))#(15, -5, 50, 0.5)

'''
'''
#using yield and next() i want one by one o/p
def operation():
    a=eval(input("Enter a number1:"))
    b=eval(input("Enter a number2:"))

    yield a+b
    yield a-b
    yield a*b
    yield a/b

oper = operation()
print(next(oper))#15
print(next(oper))#-5
print(next(oper)) #50
print(next(oper)) #0.5
print(next(oper))#StopIteration Error because
#   no.of operation = no.of next()
'''

'''
#using print() in function
def operation(a,b):

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

operation(5,10)
#o/p 15, -5, 50, 0.5


#using traversing in generator

def operation(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b

oper=operation(5,10)
print(list(oper)) #o/p:[15, -5, 50, 0.5]
    
'''


'''
2.wap to generate only values which are
divisible by 5

l=[34,55,60,56,78,90,25,40]

'''
'''
#using return in function

def check(l):
    m=[]
    for i in l:
        if i%5==0:
            m.append(i)
    return m

new=check([34,55,60,56,78,90,25,40])
print(new) #o/p: [55, 60, 90, 25, 40]
    

#using print() in function

def check(l):
    for i in l:
        if i%5==0:
            print(i)

check([34,55,60,56,78,90,25,40]) #o/p55 60 90 25 40


#using generator using yield

def check(l):
    for i  in l:
        if i%5==0:
            yield i
new=check([34,55,60,56,78,90,25,40])
print(next(new))
print(next(new))
print(next(new))
print(next(new))
print(next(new))#o/p: 55 60 90 25 40

#Typecasting in generator:

def check(l):
    for i in l:
        if i%5==0:
             yield i

new=check([34,55,60,56,78,90,25,40])
print(list(new))#[55, 60, 90, 25, 40]


#Looping in generator

def check(l):
    for i in l:
        if i%5==0:
             yield i

new=check([34,55,60,56,78,90,25,40])

for i in new:
    print(i)#55 60 90 25 40
    
'''





'''
3.wap to return a iterator which is having
square root of values present in the list

l=[25,36,49,81,9,16]
'''

'''
#using print() in function

import math
def sqrt(l):

    for i in l:
        print(math.sqrt(i))

sqrt([25,36,49,81,9,16])

#using return in function

def sqrt(l):
    x=[]
    for i in l:
       x.append(math.sqrt(i))
    return x

new=sqrt([25,36,49,81,9,16])

print(new) #[5.0, 6.0, 7.0, 9.0, 3.0, 4.0]
 '''

'''
#using yield in generator By Typecasting
import math
def sqrt(l):

    for i in l:
        yield  math.sqrt(i)

new=sqrt([25,36,49,81,9,16])

print(list(new))#[5.0, 6.0, 7.0, 9.0, 3.0, 4.0]


#using yield in generator By Looping

def sqrt(l):

    x=[]
    for i in l:
        yield math.sqrt(i)

new=sqrt([25,36,49,81,9,16])

for i in new:
    print(i) #5.0, 6.0, 7.0, 9.0, 3.0, 4.0
'''
'''
#using yield in generator print one by one
import math
def sqrt(l):

    for i in l:
        yield math.sqrt(i)

new=sqrt([25,36,49,81,9,16])

print(next(new))#5.0
print(next(new)) #6.0
print(next(new)) #7.0
print(next(new)) #9.0
print(next(new)) #3.0
print(next(new)) #4.0


'''



'''
wap to return a iterator having tuples of
word and its len pair and typecast into dictionary

l=["instagram","facebook","whatsapp","meta",
"oracle"]

'''


'''
wap to generate only numeric values in given
list

l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]

'''
'''
#using print() in function
def numeric(l):
    p=[]

    for i in l:
        if isinstance(i,(int,float)):
            p.append(i)

    print(p)

numeric(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])


#using return in function
def numeric(l):
    p=[]

    for i in l:
        if isinstance(i,(int,float)):
            p.append(i)

    return p

numeric(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])


#using yield in generator
def numeric(l):
    p=[]

    for i in l:
        if isinstance(i,(int,float)):
            p.append(i)
    yield p

   

numeric(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])


'''

'''
wap to generate a list if it is individual
data type reverse it else return as it is

l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]

'''

def oper(l):

    

    for i in l:
        if isinstance(i,(int,float,complex,bool)):
           print(i[::-1])
    


oper(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])
    





            


    







