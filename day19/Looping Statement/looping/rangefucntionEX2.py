##practice Questions

#1. Print each character of a string
'''
a="Tree Notes"

for i in range(len(a)):
    print(a[i],end=" ")


'''
#2.Print vowels only
'''
s = "education"

for i in range(len(s)):

    if s[i] in 'aeiouAEIOU':
        print(s[i],end=" ")
'''


#3.Count uppercase letters
'''
s = "PyTHon"

for i in range(len(s)):

    if s[i].isupper():
        print(s[i],i)

'''

#4.Print digits from string

'''
s = "ab12cd34"

for i in range(len(s)):

    if s[i].isdigit():
        print(s[i],i)

'''

#5.Sum of list elements
'''

x=[25,70,90,100]

total=0

for i in range(len(x)):

    total=total+x[i]
    
print("sum of total is:",total)

'''


#6.Print even numbers from list
'''
e=[23,45,66,78,90]

for i in range(len(e)):

    if e[i]%2==0:
        print(e[i])

'''

#7.Print negative numbers
'''
l = [4,-2,7,-9,3]

for i in range(len(l)):

    if l[i]<0:
        print(l[i])

'''

#8.Count odd numbers
'''
l = [1,2,3,4,5,6,7]

for i in range(len(l)):

    if l[i]%2!=0:
        print(l[i])
'''


#9.Print odd numbers 1 to 20
'''
for i in range(1,21,1):

    if i%2!=0:
        print(i)
'''

#10.wap Sum from 1 to 50
'''
total=0

for i in range(1,51,1):

    total=total+i

print("sum of 1 to 50:",total)
'''


#11.wap Print numbers divisible by 5 (1 to 51)
'''
for i in range(1,52,1):

    if i%3==0:
        print(i)
'''
#12.Reverse 10 to 1
'''
for i in range(10,0,-1):

    print(i,end=" ")
'''

#13.Squares from 1 to 10
'''
for i in range(1,11,1):

    print(i**2)

'''

#14.Print ASCII values of characters
'''
s='ABC'

for i in range(len(s)):

    print(ord(s[i]))
'''

#15.wap to Count consonants
'''
s = "education"
count=0

for i in range(len(s)):

    if s[i] not in 'aeiouAEIOU':
        count=count+1
        print(s[i])

print("total count of consonants:",count)

'''


#16.Print numbers greater than 50
'''
l = [23,67,12,89,54]

for i in range(len(l)):

    if l[i]>50:
        print(l[i])
'''

#17.Count positive numbers
'''
l = [-1,4,-3,7,9]

count=0

for i in range(len(l)):

    if l[i]>0:
        count=count+1
        print(l[i],end=" ")
print()
print("count of Positive no:",count)
'''

#18.wap to Separate even/odd
'''
e=[1,2,3,4,5,6,7,8]

even=[]
odd=[]

for i in range(len(e)):

    if e[i]%2==0:
        even.append(e[i])
    else:
        odd.append(e[i])

print("Even no:",even)
print("odd no:",odd)
'''

#19.Sum of even numbers
'''
e=[1,2,3,4,5,6,7,8]

sum=0

for i in range(len(e)):

    if e[i]%2==0:
        sum=sum+e[i]
        print(e[i],end=" ")
print()
print("sum of even no:",sum)

'''


#20.wap to print the number form 1 -20 segregate even and odd number into list
'''
even=[]
odd=[]

for i in range(1,21,1):

    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
'''
#21.wap to extract vowels and digits in a string
'''
s="hello123"

for i in range(len(s)):

    if s[i] in 'AEIOUaeiou' or s[i].isdigit():

        print(s[i])

'''
#22.wap to capitalize only the first letter of every word in the given list
'''
l=["vaidegi","rahul","shivam","kapil","patil"]

for i in range(len(l)):

    if l[i].isalpha():

        print(l[i].capitalize(),end=" ")
'''

#23.wap to extract only individual data types form the list
'''
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

for i in range(len(l)):

    if isinstance(l[i],(int,complex,bool,float)):
        print(l[i],"----> ",type(l[i]) )
'''

#24.wap to extract only individual data types from the list and sum all the individual data types

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

sum=0

for i in range(len(l)):

    if isinstance(l[i],(int ,complex,bool,float)):

        sum=sum+l[i]

        print(l[i])

print("Sum of individual D.T:",sum)



#25.wap to print the count of alphabets and numbers and space in the given string
'''
s="india got the independence in the year 1947"

alpha=0
num=0
space=0

for i in range(len(s)):

    if s[i].isalpha():

        alpha=alpha+1

    elif s[i].isdigit():
        num=num+1

    elif s[i].isspace():
        space=space+1

print("Total alphabets:",alpha)
print("Total numbers:",num)
print("Total space:",space)

        
'''



