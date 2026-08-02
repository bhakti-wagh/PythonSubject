#WAP to check if a given number is one digit or two digit or three digit or more than 3 digit. If one digit display the one digit,
#if two digit display the two digit value and so on.
'''
num=eval(input("Enter Number:"))

if num<=9:
    print("One Digit")
elif num<=99:
    print("Two Digit")

elif num<=999:
    print("Three Digit")

else:
    print("Invalid number")
'''

#WAP to accept any number from 1-5 and display that number is word form
'''
num=eval(input("Enter Number:"))

if num==1:
    print("One")
elif num=''=2:
    print("Two")
elif num==3:
    print("Three")
elif num==4:
    print("Four")
elif num==5:
    print("Five")

else:
    print("Invalid")
'''

#wap  to check given Password length is lessthan 6 print week and length is in between 6 to 8
#medium else password length is 9 to 12 strong above print verystrong

'''
password=eval(input("Enter password:"))

if len(password)<=6:
    print("Week")
elif 6<=len(password)<=8:
    print("Medium")
elif 9<=len(password)<=12:
    print("strong")
else:
    print("Very Strong")
    
'''

#Create a Login System:
#Correct username and password → Login Successful
#Correct username, wrong password → Incorrect Password
#Wrong username → User Not Found
'''
user=eval(input("Enter username:"))
passw=eval(input("Enter Password:"))

if user=='Admin' and passw=='12345':
    print("Login Successfully")
elif user=='Admin' or passw!='12345':
    print("Incorrect Password")
else:
    print("User not found")
'''


#WAP to build a simple menu-driven food ordering system. Accept a menu number from the user
#and display the corresponding food item along with its price.
#If the entered menu number is invalid, print "Invalid Menu". 
'''
menuNo=eval(input("Enter Menu No:"))

if menuNo==1:
    print("Poha %d " %(25))
elif menuNo==2:
    print("Idli Sambar %d"%(50))
elif menuNo==3:
    print("Sandwich %d"%(40))
elif menuNo==4:
    print("Vadapav %d"%(20))
elif menuNo==5:
    print("Fried Rice %d"%(80))
else:
    print("Invalid Menu")
'''

#WAP to check the teacher's mood based on the percentage of assignments submitted by the class.
#Conditions:If 100% of the assignments are submitted, print "Teacher is Very Happy "          .Else if the percentage is between 75% and 99%, print "Teacher is Happy     ".Else if the percentage is between 50% and 74%, print "Teacher is Angry   ".
#Otherwise (below 50%), print "Surprise Test Tomorrow!  "
'''
assigno=eval(input("Enter assignment no:"))

if assigno==100:
    print("Teacher is very Happy")
elif assigno<=50:
    print("Surprise test Tomorrow!")
else:
    print("not happy")'''


#WAP to suggest a weekend plan based on the user's money and mobile battery percentage.

#Money ≥ ₹1000 and Battery ≥ 80% → Go on a Trip 🏖️
#Money ≥ ₹500 and Battery ≥ 50% → Watch a Movie 🍿
#Money ≥ ₹200 and Battery ≥ 20% → Go to a Café ☕
#Otherwise → Stay Home and Study Python 🐍

money=eval(input("Enter Money:"))
battery=eval(input("Enter Mobile battery:"))

if money>=1000 and battery>=80:
    print("Go on a Trip 🏖")
elif money>=500 and battery>=50:
    print("Watch a Movie 🍿")
elif money>=200 and battery>=20:
    print("Go to a Café ☕")
else:
    print("Stay Home and Study Python 🐍")

