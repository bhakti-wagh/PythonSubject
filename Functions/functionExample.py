# Function:->


#wap to print odd number:

'''
def odd(a):
    if a%2==1:
        print(f"Odd number {a}")
    else :
        print(f"even number")

odd(11)
'''

'''

def even_odd():
    num=int(input("Enter the number:"))

    if num%2==0:
        print(f"{num} is even number")

    else:
        print(f"{num} is odd number")

even_odd()
'''


#wap to check the given number is palindrome
'''
s="level"

if s==s[::-1]:
    print("palilndrome")
else:
    print("not a palilndrome")
'''
'''
def palindrome():
     x=eval(input("Enter the string:"))

     if x==x[::-1]:
         print("its pal")
     else:
         print("not a pal")
palindrome()

'''








'''

s=[1,2,3,4,5,6,10]


for i in s:

    if i%2==0:
        print(i)
'''
'''
def even_Data(s):

    for i in s:
        if i%2==0:
            print(i,end=" ")

even_Data([1,2,3,4,5,6,10])
'''


'''
d=["Hi","walmart","xyz","good","onoff"]

for i in d:

    if len(i)%2==0:
        print(i,end=" ")
    else:
        print(i[::-1])
'''


'''
def even_len(d):
    for i in d:

        if len(i)%2==0:
            print(i,end=" ")
        else:
            print(i[::-1])

even_len(["Hi","walmart","xyz","good","onoff"])
    
'''

'''
s="Hello"

d={}

for i in s:

    d[i]=ord(i)

print(d)



def check(s):
    d={}

    for i in s:
        d[i]=ord(i)
        
    print(d)

check("Hello")

 '''


'''
d=[1,45,78,True,False,999]


def check(d):

    for i in d:

        if isinstance(i,bool):  #type(i)==bool
            print(i)

check([1,45,78,True,False,999])
'''



'''

#normal 
e=[90,True,3.5,9+4j,"abc",[1,2,3],{67,90}]

s_v=[]

c_v=[]

for i in e:

        if isinstance(i,(int,bool,float,complex,bool)):
            s_v.append(i)
            
        else:
            c_v.append(i)
print(s_v)
print(c_v)

print()
print()



#function
def demo(e):

    single=[]

    collection=[]

    for i in e:

        if isinstance(i,(int,bool,float,complex,bool)):
            single.append(i)
            
        else:
            collection.append(i)

    print(single)
    print(collection)

demo([90,True,3.5,9+4j,"abc",[1,2,3],{67,90}])
'''



