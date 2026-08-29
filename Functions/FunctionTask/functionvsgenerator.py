'''
#using return keyword
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    return a
    return b
    return c

d=check(10,20)
print(d)  #o/p:30


print()


#Using generator with yield keyword
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c

d=check(10,20)
print(d)  #o/p:<generator object check at 0x0000028A9E9E0BA0>
#If we use print() : it will show object address




#1st typecasting
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c

d=check(10,20)
#typecasting use
print(list(d)) #o/p: [30, -10, 200]

print()


#2.using looping
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c

d=check(10,20)
#using loop

for i in d:
    print(i)  # 30 ,-10,200

print()




#Using next() :-> it will call one by one output
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c

d=check(10,20)
print(next(d))#30
print(next(d))#-10
print(next(d))#200
print(next(d))#StopIteration



'''


'''

#If i want at time output using geneartor with yield keyword
#o/p : in tuple form
def check(x,y):
    yield x+y,x-y,x*y

d=check(10,20)
print(next(d)) #(30, -10, 200)

'''
'''

x=[1,2,3,4,5,6]

#i want to make all number square and add into list

def square(x):
    

    for i in x:
        print(i**2)

        
square([1,2,3,4,5,6])#All o/p get at time


def square(x):

    for i in x:
        yield i**2

y=square([1,2,3,4,5,6])

print(next(y)) #1
print(next(y))  #4
print(next(y))  #9
print(next(y))  #16

y.close()

print(next(y))#StopIteration

'''


'''
#using return 
def square(x):
    l=[]

    for i in x:
        l.append(i**2)
    return l

y=square([1,2,3,4,5,6])

print(y) #[1, 4, 9, 16, 25, 36]




#using yeild
def square(x):
    l=[]

    for i in x:
        l.append(i**2)
    yield l

y=square([1,2,3,4,5,6])

print(next(y))#[1, 4, 9, 16, 25, 36]

#whenver we are storing the data into container that time output will be at time

'''


#using function

x=["walmart","vestra","vstar","blind","thankyou","promax","panthor"]

#total 7
# print odd length

def odd(x):

    for i in x:
        if len(i)%2!=0:
            print(i)


odd(["walmart","vestra","vstar","blind","thankyou","promax","panthor"])


#by return keyword

def odd(x):

    y=[]

    for i in x:
        if len(i)%2!=0:
            y.append(i)
    return y


z=odd(["walmart","vestra","vstar","blind","thankyou","promax","panthor"])

print(z)


#by using generator typecasting

def odd(x):

    for i in x:
        if len(i)%2!=0:
            yield i

z=odd(["walmart","vestra","vstar","blind","thankyou","promax","panthor"])

print(list(z))



#by using next()

def odd(x):

    for i in x:
        if len(i)%2!=0:
            yield i

z=odd(["walmart","vestra","vstar","blind","thankyou","promax","panthor"])

print(next(z))
print(next(z))
print(next(z))
print(next(z))


#by looping

def odd(x):

    for i in x:
        if len(i)%2!=0:
            yield i

z=odd(["walmart","vestra","vstar","blind","thankyou","promax","panthor"])

for i in z:
    print(i)








    

            








