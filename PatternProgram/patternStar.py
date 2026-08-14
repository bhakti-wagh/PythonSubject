
#Pattern Programs

'''
n=5

for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

'''
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

'''

'''
for i in range(5):
    for j in range(i+1):

        print("*",end=" ")
    print()

'''

#o/p

'''
* 
* * 
* * * 
* * * * 
* * * * *
'''


for i in range(5,0,-1):
    for j in range(i,0,-1):

        print("*",end=" ")
    print()






