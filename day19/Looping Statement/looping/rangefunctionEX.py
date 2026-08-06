#Range()---> startPoint----endPoint----stepvalue



#To include endindex
'''
for i in range(10): #here startpoint->0 and stepvalue-1
    print(i,end=" ")

'''
#wap to print 15 to 30
'''
for i in range(15,31,1):
    print(i,end=' ')


print()
print()

'''
#wap to print 10 to 20 in between even number
'''
for i in range(10,21,2):
    print(i)

print()
print()'''
#wap to print 10 to 1-->??
'''
for i in range(10,0,-1):
    print(i,end=" ")

print()
print()

for i in range(50,34,-1):
    print(i,end=" ")

print()
print()
'''

#wap to  print position of character in the given string:
'''
s="PYTHON"

for i in range(len(s)):
    print(i,end=" ") # to print character also then---> i,s[i]


print()
print()




s=["Morning","wallmart","Hello","joy","part"]

for i in range(len(s)):
    print(i,s[i])
'''





#wap to print sum of the number(0-10)
'''
sum=0
for i in range(0,11,1):
    sum=sum+i
    print(sum)
     
'''


#character with ascii value

s="hello"


#count uppercase letters

s="PyTHon"

total_character=0

for i in s:
    if i.isupper():
        total_character=total_character+1
print(total_character)
