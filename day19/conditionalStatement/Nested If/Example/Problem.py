
#wap to check whether the middle value in a list is str or not
'''
a=eval(input("Enter the list:"))


if len(a)%2==1:
    if type(a[len(a)//2])==str:
        print("The middle is string",a[len(a)//2])
    else:
        print("The middle value is not string")
else:
    print("The length is even and no middle value")


'''

#wap to check whether the character is vowel or not

'''
char=eval(input("Enter character:"))

if char.isalpha():
    if char in 'AEIOUaeiou':
        print("character is vowel")
    else:
        print("character is consonant")
else:
    print("Character is not string")
'''


#wap to check whether the last value in a list is palindrome or not and start with vowel or not
'''
char=eval(input("Enter list data:"))

if char[-1]==char[-1][::-1]:
    if char[-1][0] in 'AEIOUaeiou':
        print(char[-1],"last ele is palindrome and starts with vowel")
    else:
          print(char[-1],"last ele is palindrome and starts with consonant")
else:
    print("last value/element is not a plindrome ")
    
'''

#wap to check my instagram username and password
'''
u='admin'
p='admin@123'
user=(input("Enter username:")) 
if user==u:
    passw=(input("Enter Password:"))
    if passw==p:
        print("Login successful")
    else:
        print("Password invalid")
else:
    print("username invalid")

'''
#Greatest of four number
'''
num=eval(input("Enter number:"))
a=eval(input("Enter number:"))
b=eval(input("Enter number:"))
c=eval(input("Enter number:"))

if num >= a:
    if num >= b:
        if num >= c:
            print(f"{num} is greater")
        else:
            print(f"{c} is greater")
    else:
        if b >= c:
            print(f"{b} is greater")
        else:
            print(f"{c} is greater")
else:
    if a >= b:
        if a >= c:
            print(f"{a} is greater")
        else:
            print(f"{c} is greater")
    else:
        if b >= c:
            print(f"{b} is greater")
        else:
            print(f"{c} is greater")
'''


ls=eval(input("Enter list data:"))


if type(ls)==list:

    print("1--->pop()")
    print("2--->append()")
    print("3--->clear()")

    choice=eval(input("Enter choice :"))

    if choice==1:
        ls.pop()
        print(ls)
    elif choice==2:
        data=eval(input("Enter data to append:"))
        ls.append(data)
        print(ls)
    elif choice==3:
        ls.clear()
        print(ls)
    else:
        print("Invalid choice")
else:
    print("entered data is not list")
