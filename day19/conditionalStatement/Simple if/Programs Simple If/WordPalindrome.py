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
