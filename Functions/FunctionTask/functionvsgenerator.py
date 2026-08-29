
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

def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c

d=check(10,20)
print(d)  #o/p:<generator object check at 0x0000028A9E9E0BA0>


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





