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




