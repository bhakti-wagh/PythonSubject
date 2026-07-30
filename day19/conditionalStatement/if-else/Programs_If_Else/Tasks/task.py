#Ravi would like to buy a new cello or red pen. The cost of the pen should be 10.
#If the pen is available in the shop, he will buy the pen. If it is not there he will
#come out of the shop.


#WAP to perform addition and subtraction operation by using list collection if the
#first and middle data items number are even performing addition operation, or
#else performing subtraction.
'''
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

'''

#wap to check whether the first item of these
#two list is either integer or not
#if it is an integer, concatenate these two list
#or else print memeory address of these two lists
'''
a=[10,20,30,40]
b=[5.5,6,7,8,9]

if isinstance(a[0],int) and isinstance(b[0],int):
    print(a[0]+b[0])
else:
    print("first list id:",id(a))
    print("second list id:",id(b))

    '''
#WAP to check whether the given string of the first character is a special symbol
#or not. If a special symbol, to extract and display the middle character or else to
#reverse the string and display the half of the string.
'''
a=eval(input("enter data:"))

mid=(len(a)-1)//2

if not a[0].isalnum():
    print(mid,a[mid])
else:
    rev=a[::-1]
    print(rev[0:mid+1:1])

'''

#WAP whether a given string, if string length is more than 2, then it displays a new
#string with the first and last characters switched, otherwise the display the 3
#copies of given string.

a="Py"

if len(a)>2:
    print(a[-1]+a[1:-1:1]+a[0])

else:
    print(a*3)
 
