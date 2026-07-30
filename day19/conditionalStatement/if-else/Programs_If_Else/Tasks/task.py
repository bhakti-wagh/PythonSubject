#Ravi would like to buy a new cello or red pen. The cost of the pen should be 10.
#If the pen is available in the shop, he will buy the pen. If it is not there he will
#come out of the shop.


#WAP to perform addition and subtraction operation by using list collection if the
#first and middle data items number are even performing addition operation, or
#else performing subtraction.
a=[10,20,30,47,50,60,70]

low=0
high=len(a)-1

first_element=a[low]

print("first_element")

mid_ele=(low+high)//2

print("mid_ele")#3

print(a[mid_ele])#collection[mid]-> varName[posi]

if first_element%2==0 and a[mid_ele]%2==0:
    print(first_element+a[mid_ele])
else:
    print(first_element-a[mid_ele])
