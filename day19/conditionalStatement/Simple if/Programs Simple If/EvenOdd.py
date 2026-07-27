#wap to check give number is even (with %):
'''
a=4
if a%2==0:
    print(f"The given num {a} is even")
    

'''

#(Without %)

a=10

#(here get int Q. then it will multiply with 2 and then it will check it will equal to variable)

if(a//2)*2==a: 
    print(f"The given num {a} is even")


#Wap to check the given number is even (without using % and // symbol)-->?
#Using Bitwise (and/&):-> Truth Table / if -> 0 then even / if->1 then odd / we have to take
# bin(1)->1 because(constant binary num)


b=20

if (b&1)==0:
    print(f"Then given num {b} is even")

c=23
if(c&1)==0:
    print(f"Then given num {b} is even")#It will show blank space






#Wap to check given number is odd (with 3 types )

c=23
if 23%2==1:
    print(f"The give num {c} is odd")

d=7
if d%2!=0:
    print(F"The given num{d}is odd")

d1=13
if(d1&1)==1:
    print(F"The given num {d1}is odd")


#Wap to check given word is even length

a="Python"

if len(a)%2==0:
    print(f"The given word is {a} is even length")


#wap to check give number is even and then convert into complex data type

x=100

if x%2==0:
    print(complex(x))
    print(float(x))

#Wap to check given number is even and store into list (Without inbuilt function)

x=200

k=list()

if x%2==0:
    k=k+[x]
    print(k)


#Wap to check given number is even and store into list (with append function)

h=20
k=[]

if h%2==0:
    k.append(h)
    print(k)

s=30
k=s

type(k)

