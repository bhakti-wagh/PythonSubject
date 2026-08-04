

#wap to check whether the given number is even and greater than 5
'''
num=eval(input("Enter number:"))

if num%2==0:

    print(f"the given number {num} is even")

    if num>=5:
        print(f" the given number {num} is Greater than 5")
    else:
        print("Not greater than 5")

else:
    print("Not even number")
'''


#2.wap to check the number is odd and check if
#the number is divisible by 7

'''
num=eval(input("Enter number:"))

if num%2==1:
    print(f"the given number is {num} is odd")

    if num%7==0:
        print(f"the given number is {num} divisible by 7")

    else:
        print(f"The given number is {num} not divisible by 7")

else:
    print(f"The given number is {num} is even")
'''


#4.wap to validate facebook username and password
#condition is:---> username-->"python"  and
#password="python masters"

'''
user ="python"
pas_w="python masters"


username=eval(input("Enter username:"))


if username==user:
    print("Valid username")

    password=eval(input("Enter password:"))

    if password==pas_w:
        print("valid password")
        print("Login succesfully")
    else:
        print("Invalid password")

else:
    print("Invalud username")

'''


#5.wap to Book ticket in Book my show
#condition:---> first it should ask theaters name then it
#should display the movie available
#then it has to display ticket price and in the end ticket
#should be booked
'''
Theater=['PVR','INOX','CINIPOLE']

user=eval(input("Enter Theater name:"))

if user in Theater:
    print(f"User is selected the {user} Theater name")

    Movies=['spiderman','Doremon','Sinchan','RIO 2']

    user1=eval(input("Enter Movie name:"))

    if user1 in Movies:
        print(f"Here{user} is selected the Theater and {user1} is selected The Moive")

        Tp=[1000,2000,3000,4000]
        amount=eval(input("Enter the amount"))

        if amount==Tp[0]:
            print(f'Here user is {user} selected the Theater name and {user1} is selected the Movie and Total Ticket price is {amount}')

        elif amount==Tp[1]:
            print(f'Here user is {user} selected the Theater name and {user1} is selected the Movie and Total Ticket price is {amount}')

        elif amount==Tp[2]:
            print(f'Here user is {user} selected the Theater name and {user1} is selected the Movie and Total Ticket price is {amount}')

        elif amount==Tp[3]:
            print(f'Here user is {user} selected the Theater name and {user1} is selected the Movie and Total Ticket price is {amount}')

        else:
            print("Ticket price is too low")

    else:
        print("Wrong movie selected")

else:
    print("Wrong Theater selected")
        
            
'''
    

    

#data type should be string 1.upper() 2.lower() 3.swapcase()
#4.capitalize()

'''
data=eval(input("Enter the data:"))

if isinstance(data,str):
    print("yes we are passing string data type")

    print("1.upper()")
    print("2.lower()")
    print("3.swapcase()")
    print("4.capitalize()")
    

    option=eval(input("Enter option:"))

    if option==1:
        print(data.upper())
       

    elif option==2:
        print(data.lower())
       
        
    elif option==3:
        print(data.swapcase())
        

    elif option==4:
        print(data.capitalize())
        
    else:
        print("invalid option")

else:
    print("Invalid data type")
    
'''

#wap to find middle element is even or odd [3,4,6,7,9,1,5]

#li=eval(input("Enter list data:"))
'''
a = [3, 4, 6, 7, 9, 1, 5]

if len(a) > 0:

    mid = len(a) // 2
    middle = a[mid]

    if middle % 2 == 0:
        print(f"Middle element {middle} is Even")
    else:
        print(f"Middle element {middle} is Odd")

else:
    print("List is Empty")
'''
#wap to purchase a phone from the shopping app
#apps=["Flipcart","Amazon"]
#categories=["Electronics","Mobile","Fashion","furnitures"]

'''
apps=["Flipcart","Amazon"]

user=eval(input("Enter apps:"))

if user in apps:

    print(f"you choose {user}app")

    categories=["Electronics","Mobile","Fashion","furnitures"]

    user1=eval(input("Enter categories:"))

    if user1 in categories:

        print(f"you choose {user} app and {user1} categories")

        

        


'''
    



#wap to give 10% off only who is purchasing in credit card and min 3 product should purchase
#and product price should be more than 500

'''

payment=["credit card","Phone Pay","Cash on delivery"]


mode=eval(input("Enter mode of Payment:"))

if mode in payment:

    print(f"You choose {mode}")

    totalproduct=eval(input("Enter Total Proudct:"))

    if totalproduct>=3:
        p1=eval(input("Enter p1 amount:"))
        p2=eval(input("Enter p2 amount:"))
        p3=eval(input("Enter p3 amount:"))

        if p1>500 and p2>500 and p3>500:

            
            if mode==payment[0]:
                
                total = p1 + p2 + p3
                discount = total * 10 / 100
                final_amount = total - discount

                print("Congratulations! You got 10% Discount.")
                print("Total Product:",totalproduct)
                print("Total Amount:", total)
                print("Discount:", discount)
                print("Final Amount:", final_amount)
                

              
            else:
                 print("Discount is available only for Credit Card payment.")



        else:
            print("product price is not greater than 500")

    else:
        print("Total product is not 3")

else:
    print("Invalid payment mode")

'''
