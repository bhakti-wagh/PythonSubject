#Wap to find factor of given number

num=eval(input("Enter number:"))

i=1

out=[]

while i<=num:

    if num%2==0:

        out.append(i)

    i+=1

print(out)

    
