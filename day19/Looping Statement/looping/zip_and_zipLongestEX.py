
x=(10,20,30)
y=[1,2,3]

#Using traversing

print(list(zip(x,y)))  #[(10, 1), (20, 2), (30, 3)]

#using zip_longest Traversing
from itertools import zip_longest
print(list(zip_longest(x,y))) #[(10, 1), (20, 2), (30, 3)]


#using for loop zip
for i in zip(x,y):
    print(i)

'''
(10, 1)
(20, 2)
(30, 3)
'''

#using for loop zip_longest

for i in zip_longest(x,y):
    print(i)

'''
(10, 1)
(20, 2)
(30, 3)
'''

