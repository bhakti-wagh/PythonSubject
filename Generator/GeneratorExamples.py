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



