# Function:->


#wap to print odd number:

'''
def odd(a):
    if a%2==1:
        print(f"Odd number {a}")
    else :
        print(f"even number")

odd(11)
'''

'''

def even_odd():
    num=int(input("Enter the number:"))

    if num%2==0:
        print(f"{num} is even number")

    else:
        print(f"{num} is odd number")

even_odd()
'''


#wap to check the given number is palindrome
'''
s="level"

if s==s[::-1]:
    print("palilndrome")
else:
    print("not a palilndrome")
'''
'''
def palindrome():
     x=eval(input("Enter the string:"))

     if x==x[::-1]:
         print("its pal")
     else:
         print("not a pal")
palindrome()

'''
'''

s=[1,2,3,4,5,6,10]


for i in s:

    if i%2==0:
        print(i)
'''

def even_Data(s):

    for i in s:
        if i%2==0:
            print(i,end=" ")

even_Data([1,2,3,4,5,6,10])




        
