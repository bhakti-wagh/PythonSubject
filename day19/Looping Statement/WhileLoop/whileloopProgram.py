#Wap to find factor of given number

'''
num=eval(input("Enter number:"))

i=1

out=[]

while i<=num:

    if num%i

    ==0:

        out.append(i)

    i+=1

print(out)

    
'''


#perfect number
'''
num=eval(input("Enter number:"))

i=1

total=0

while i<num:

    if num%i==0:

        total=total+i

    i+=1

if total==num:
    print(f"{num} is perfect number")

else:
    print(f"{num} is not perfect number")


'''

#Prime number
'''
num=eval(input("Enter number:"))

i=1

out=[]

while i<=num:

    if num%i==0:
        out.append(i)
    i+=1

if len(out)==2:
    print("prime number")

else:
    print("not a prime number")

'''



#Armstrong number

num=eval(input("Enter number:"))

i=0
total=0

b=str(num)

power=len(b)

while i<len(b):

    total=total+int(b[i])**power   

    i+=1


if total==num:
    print(f"{num} is armstrong number")

else:
    print(f"{num} is not armstrong number")




 
