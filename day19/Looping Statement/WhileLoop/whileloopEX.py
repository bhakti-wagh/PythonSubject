
# wap to print "Idli vada" for 5 times
'''
i=0

while i<5:
    print("Idli vada")

    i+=1
'''
'''
Idli vada
Idli vada
Idli vada
Idli vada
Idli vada


'''


# wap to print no from 1 to 10
'''
i=1

while i<11:
    print(i,end=" ")

    i+=1
'''
#1 2 3 4 5 6 7 8 9 10


#wap to print even no from 1 to 10
'''
i=2

while i<=10:

    if i%2==0:
        print(i,end=" ")

    i+=2
 '''

#2 4 6 8 10




#wap to print addition n natural number
'''
n=eval(input("Enter the number:"))

i=1

add=0

while i<=n:

    add=add+i
    i+=1

print(add)
'''
# sum = 55


#wap to print multiplication n natural number
'''
n=eval(input("Enter the number:"))

i=1

multi=1

while i<=n:

    multi=multi*i
    i+=1

print(f"Mulitplication of {n} natural number is:",multi)

'''


#wap to fetch lower case char from string
'''
st=eval(input("Enter the string:"))

out=''

i=0

while i<len(st):

    if st[i].islower():
        out=out+st[i]
    i+=1

print(out)

'''
#Enter the string:'HelLo'
#elo


#fetch all the lowercase,uppercase,digit , specialcharacter
'''
s=eval(input("Enter the string:"))

low=''
upp=''
digit=''
spe=''

i=0

while i<len(s):

    if s[i].islower():
        low=low+s[i]

    elif s[i].isupper():
        upp=upp+s[i]

     elif s[i].isdigit():
        digit=digit+s[i]

    else:
        spe=spe+s[i]
    i+=1

print(low)
print(upp)
print(digit)
print(spe)
'''

'''
Enter the string:'hE45#%'
h
E
45
#%
'''


#wap to addition of int numbers in given form list

'''
a=[10,4j+9,'bhakti','sdkf',45,90,'sb']

add=0

i=0
while i<len(a):

    if isinstance(a[i],int):

        add=add+a[i]

    i+=1

print(add)

#145
'''

#wap to fecth the string value from list only if len>3

l=['abc',45,'zsya','you','cat','apple']

#l=eval(input("Enter the list:"))

i=0
 

while i<len(l):

    if isinstance(l[i],str) and len(l)>=3:
        print(l[i])
    i+=1





#wap to do addition of ascii value of the special char in string
'''
l="H@Hei!!"

i=0
add=0
while i<len(l):

    if not l[i].isalpha():
        add=add+ord(l[i])
    i+=1

print(add)
'''
        
