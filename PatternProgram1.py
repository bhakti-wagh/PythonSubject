#Star pattern

for i in range(4):
    for j in range(4):
        print("*",end=" ")

    print()



#Right-angled Triangle

n=4
for i in range(n):
    for j in range(i+1):
        
        print("*",end=" ")
        
    print()


print()


#inverted right triangle
n=4
for i in range(n,0,-1):
    for j in range(i):
        
        print("*",end=" ")
        
    print()


print()

#increasing number triangle

n=4
for i in range(1,5,1):
    for j in range(1,i+1):
        
        print(j,end=" ")
        
    print()


print()


#repeated number triangle

for i in range(1,5,1):
    for j in range(i):
        print(i,end=" ")
    print()


print()


#Alphabet triangle

for i in range(1,5,1):
    for j in range(1,i+1):
        
        print(chr(64+j),end=" ")
        
    print()


print()

print()

#Inverted number triangle

n=4
for i in range(n,0,-1):
    for j in range(1,i+1):
        
        print(j,end=" ")
        
    print()


print()
