#Programs


#wap to print a-z character
'''
for i in
range(97,123):
    print(chr(i),end=" ")

print()
'''


#Wap to print A-Z character
'''
for i in range(65,91):
    print(chr(i),end=" ")
'''

#If you want to print a-z and A-Z character then use below logic
'''
for i in range(97,123):
    print(chr(i),chr(i-32),end=" ")
'''

#wap to get the give o/p
'''
s="hi hello good morning"

for i in reversed(s):
    print(i,end=" ")
print()
print()
    
for i in s[::-1]:
    print(i,end=" ")

print()
print()

for i in range(-1,-len(s)-1,-1):    
    print(s[i],end=" ")

print()
print()

res=""

for i in s.split():
    res=i[::-1]+" "+res

print(res)


'''


#wap to create dictionary with letter and its words starting with that letter pasir
'''
s="hi hello good morning welcome to python session"


d={}

for i in s.split():

    if i[0] not in d:

        d[i[0]]=[i]
    else:
        d[i[0]] += [i]

print(d)


'''

#wap to create dictionary with letter and its indexing position 
'''
s="hello python"

d={}

for i in range(len(s)):
    
    if s[i] not in  d:

        d[s[i]]=[i]
    else:
        d[s[i]]+=[i]

print(d)
'''



#wap to sum of numbers
'''
s="Sony12India567pvt21ltd"

total=0

for i in s:

    if i.isdigit():

        total +=int(i)

print(total)


'''


#3.Print all the missing numbers from 1-10 in the below list
'''
l = [1, 2, 3, 4, 6, 7, 10]

num=[]

for i in range(1,11):

    if i not in l:
        num.append(i)
        
print(num)
        
'''


#4.WAP to remove duplicates from the list without using inbuilt function

d=[1,2,3,4,5,6,7,1,2,3,4]

num=[]

for i in range(0,len(d)):

    if d[i] not in num:

        num=num+[d[i]]
        


print(num)



    
