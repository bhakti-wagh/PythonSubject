#wap to check the given word is palindrome?
#(checking LHS=RHS "MoM==MOM, DAD==DAD")(Using Slicing)

#1way user input
'''
x = eval(input("enter the data:"))

if x==x[::-1]:
    print(f"{x} is plaindrome word")
'''
#given number is  plaindrome or not {2 ways}
#1way:

q=121

r=str(q) # r='121' convert into string d.t

if r==r[::-1]:
    print(f"{r} is palindrome number")



#2nd way: if you want to print 1st no: var//100, last no: var%10, it will
    #only work for 3digits number

p=121

if (p//100)==(p%10):
    print(f"{p} is palindrome number")




#wap to check the given number is divisible by  2 and 6

num=eval(input("Enter number:"))

if (num%2)==0 and (num%6)==0: #here if 1 condition is true and 2nd condtion false and it will not work 
    print(f"{num} is divisible by 2 and 6")

#use OR

num1 = eval(input("Enter Number:"))

if num1%2==0 or num1%6==0:
    print(f"{num1} is divisible by 2 or 6")
