#Reversed()

a="Python"

#normal way

#print(reversed(a))  #<reversed object at 0x000001AACA6EC070>


#Using Typecasting
'''
print(list(reversed(a)))#['n', 'o', 'h', 't', 'y', 'P']
print(tuple(reversed(a)))#('n', 'o', 'h', 't', 'y', 'P')
print(set(reversed(a)))#{'P', 'h', 'y', 'n', 't', 'o'}
print(dict(reversed(a)))#valueError :-> because of value part
'''
#using Looping
'''
for i in reversed(a):
    print(i,end=" ")#n o h t y P 

'''


#for reverse the string using slicing
'''
for i in a[::-1]:
    print(i,end=" ")#n o h t y P 
'''

#using range fucntion
'''
for i in range(-1,-len(a)-1,-1):
    print(a[i],end=" ")  #n o h t y P 
'''


#without using inbuilt function

#take one empty string

'''
res=""

for i in a:
    res=i+res
print(res)
'''





d=[1,2,3,4,5]
'''
for i in reversed(d):
    print(i,end=" ")#5 4 3 2 1
print()
print()
'''

'''
for i in range(-1,-len(d)-1,-1):
    print(d[i],end=" ")#5 4 3 2 1
print()
print()
'''
'''
for i in d[::-1]:
    print(i,end=" ")#5 4 3 2 1
print()
print()

'''

res=[]

for i in d:
    res=[i]+res
print(res)#[5, 4, 3, 2, 1]
