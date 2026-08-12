#Armstrong number

#Wap to check given number is armstrong or not

a=153

total=0

b=str(a) #--> 153---> '153'

print(b) #-->'153'

power=len(b)

print(power)  #-->3

for i in b:

    total=total+int(i)**power

if total==a:
    print("armstrong number")

else:
    print("Not armstrong number")
