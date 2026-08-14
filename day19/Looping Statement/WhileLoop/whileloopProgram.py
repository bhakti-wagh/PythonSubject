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
'''
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

'''

'''
num=eval(input("Enter number:"))

dum=num

num_len=len(str(num))

total=0

while num>0:

    last_d= num%10

    total=total+last_d**num_len

    num//=10

if total==dum:

    print(f"{dum} is armstrong ")

else:

    print(f"{dum} is not armstrong")

'''


#disarium number

'''
num=eval(input("Enter number:"))
dum=num

total=0


num_len=len(str(num))


while num>0:

    last_d= num%10

    total=total+last_d**num_len

    
    num_len = num_len - 1

    num//=10

    

if total==dum:
    print("disarium number")

else:
    print("not disarium nuber")
'''
