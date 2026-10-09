'''
from itertools import zip_longest
a=[10,20,30]
b=[40,50,60]

print([a[i]+b[i] for i in range(len(a))])

print([sum(i) for i in zip(a,b)])

print([sum(i) for i in zip_longest(a,b)])

'''


'''
a=("Hi","Hello","Bye")

print([(i,a[i])for i in range(len(a))])

'''

'''
x=['Nandu' , 'Indu','Bindu','chandu','shindu']
print([i[::-1] for i in x  if len(i)%2==0])

print([i[::-1] if len(i)%2==0 else i for i in x])
'''

'''
inp=[10,'hai',4j+9,True ,{'a':20,'b':10}]

print([len(inp[i]) if isinstance(inp[i], (int, float, complex, bool)) == False else 1 for i in range(len(inp))])

a="Python is very easy"

print([(i,len(i)) for i in a.split()])
'''

a='abcde abc abcd abcdef'
print([(i,len(i)) if len(i)%2==0 else (i,i) for i in a.split()])
