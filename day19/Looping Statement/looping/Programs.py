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
'''
d=[1,2,3,4,5,6,7,1,2,3,4]

num=[]

for i in range(0,len(d)):

    if d[i] not in num:

        num=num+[d[i]]
        

print(num)

'''





#5.wap to replace all the character with "-"
#if the characters occurs more than once in a string

#o/p---->-e--o-ai
'''
s="hellohai"

new_str=""

for i in s:

    if s.count(i)>1:

        new_str= new_str+'-'  #s=s.replace(i,"-")

    else:
        new_str=new_str+i

print(new_str)

'''

#6.wap to print first and last char of each name in the list
'''
a=["Sunil","anil","Suresh","Mahesh","Dinesh"]


for i in a:
    print(i[0],i[-1])
'''


#7.wap to create a new list as square of each number
#of below list
'''
b=[2,4,5,6,7,1]
sqr=[]

for i in b:

    #sqr.append(i**2)

    sqr = sqr+[i**2]

print(sqr)

'''


#8.wap if number is even the print its square else print
#its cube
'''
c=[2,4,5,3,7,9]


for i in c:

    if i%2==0:
        print(i**2)
    else:
        print(i**3)

'''

#9.wap to create a list with square and cube of each numbers

#o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]
'''
d=[2,4,5,1,8,9,10]

l=[]

for i in d:

    l.append((i**2,i**3))

print(l)
'''


#10.wap to create a new list of reversing each name from the list

'''
names=["prince","Rekha","Madhu","Sindhu","denga","manga"]

rev=[]

for i in names:

    if i not in rev:

        rev= rev+ [i[::-1]]

    

print(rev)

'''


#11.wap to create a new list, of individual and collection data type from list
'''
data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]

Id=[]
cd=[]

for i in data:

    if isinstance(i,(int,float,complex,bool)):

        Id += [i]

    else:
        cd += [i]

print(Id)
print(cd)


'''


#12.wap to create a dictionary characters and its count pair
'''
char=["a","M","i","A","M","I","i","H","a","H"]

dic={}



for i in char:

    if i in dic:

        dic[i]=dic[i]+1
    else:
        dic[i]=1

print(dic)

'''

#13.wap to group fruit name and country pair
'''
d={"apple":45,"mango":67,"cherry":90,"berry":23}

p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}

new={}

for i,j in zip(d,p):
    new[i]=(j,p[j])

print(new)

'''

#14.wap to sum of same index element from l1,l2,l3
'''
l1=[10,20,30,40]
l2=[78,44,11,99]
l3=[1,2,3,4]

l4=[]

for i,j,k in zip(l1,l2,l3):

    l4=l4+[i+j+k]  #sum(i)

print(l4)


'''

#15.wap to pair values of both dictionary

'''
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}

new={}

for i,j in zip(d,p):  for i in zip(d.values(),p.values())

    new[d[i]]=(p[j])
    
print(new)

'''





#1. WAP to extract only file names
l= ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',
    'lambda.png', 'map.py', 'python.pdf', 'oops.py']
#output:-['forloop', 'python', 'while', 'functions', 'lambda', 'map', 'oops']


k=[]

for i in l:
    m=i.split(".")

    k.append(m[0])


print(k)




    






    
