#Examples of 8 arguments


#1. positional arguments
'''
def demo(a,b):
    print(a,b)

demo()#->TypeError
demo(1)#->TypeError
demo(1,2)#->1,2

'''

#2.keyword arguments

'''
def demo(a,b):
    print(a,b)


#demo()#-> TypeError
#demo(1)#->TypeError
#demo(a=1,2)#-> positonal argument follow keyword argument

demo(1,b=2) # 1,2

 '''


#3. only positional arguments
'''
def demo(a,b,/,x,d):
    print(a,b,x,d)

#demo(1,2,3,4) # 1 2 3 4
#demo(1,2,c=3,4)#positonal argument follows keyword arg
#demo(a=1,2,3,4)#positonal argument follows keyword arg
demo(1,2,3,d=4)
'''


#4. only keyword arguments

def demo(a,b,*,c):
    print(a,b,c)

demo(1,2,c=3) #1 2 3
000
