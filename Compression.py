'''
from itertools import zip_longest
a=[10,20,30]
b=[40,50,60]

print([a[i]+b[i] for i in range(len(a))])

print([sum(i) for i in zip(a,b)])

print([sum(i) for i in zip_longest(a,b)])

'''



a=("Hi","Hello","Bye")

print([(i,a[i])for i in range(len(a))])


