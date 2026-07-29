#wap to check given number is even then print quotient and reminder else make power of num
'''
num=eval(input("enter number:"))

if num%2==0:
    print("q-->",num/2)
    print("R-->",num%2)
    

else:
    print("power--->",num**2)
'''

#wap to check the given dic length is even print as it is else add one
#key and value pair make it as even
s={1:2,4:5,8:9}

if len(s)%2==0:
    print(s)

else:
    s.update({50:10}) # var_name[key]=value
    print(s)


#wap to check given no is odd print as it is else convert to negative
num=eval(input("enter number:"))

if num%2!=0:
    print(num)

else:
    print(-(num))
