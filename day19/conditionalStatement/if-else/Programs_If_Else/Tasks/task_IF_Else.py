
#wap to check whether a number is positve or negative
# if positive print message or else print negaitve number
'''
num=eval(input("Enterd number:"))

if num>=0:
    print("positive number")

else:
    print("negative number")
'''

#wap to check whethe a no is even or odd. if even
#Print message an even or else print msg odd
'''
num=eval(input("Enter number:"))

if num%2==0:
    print(f"{num} is Even number")

else:
    print(f"{num} is Odd number")
'''

#wap to check whether a given number is greater than 10 or not
#if it is greater than 10 print mesg as greater or else print
#than number with not greater than
'''
num=eval(input("Entered number:"))

if num>=10:
    print("Greater")
else:
    print(f"{num} is not greater than")
'''

#wap to check a given two input numbers are divisible by 3 and 5.
#if it is divisble print("Good Morning"), if it is not divisible print("Good Evening")

'''
num=eval(input("Enter number:"))

if num%3==0 and num%5==0:
    print("Good Morning")

else:
    print("Good Evening")
'''

#Wap to accept two integers and check whether those two values are equal or not
#if equal , multiply to value or else to display quotation value
'''
num1=eval(input("Enter 1st num:"))

num2=eval(input("Enter 2nd num:"))

if num1==num2:
    print(num1*num2)
else:
    print(num1//num2)
'''

#wap to find the largest of two numbers
'''
num1=eval(input("Enter num 1:"))

num2=eval(input("Enter num 2:"))

if num1>num2:
    print(f"{num1} is largest number")
else:
    print(f"{num2} is largest ")
'''

#wap to check whether input num is greater than 10 or not
#If it greater than 10 print messages as greater with number.
#IF it is not a greater than 10 print that number
'''
num=eval(input("Enter number:"))

if num>=10:
    print(f"{num} is greater")
else:
    print(f"{num} is not greater than 10")
'''

#wap to the given num integer if n is greater than 21 , print the
#Absolute difference between n and 21.
#Otherwise print twice the absolute difference
'''
n=eval(input("Enter number:"))

'''

#wap to find smallest of two numbers
'''
num1=eval(input("Enter num 1:"))

num2=eval(input("Enter num 2:"))

if num1<num2:
    print(f"{num1} is smallest number")

else:
    print(f"{num2} is smallest number")

'''


#wap to check whether the given input is divisible by 3 or not if yes
#if yes print the number or else print cube of number
'''
num=eval(input("Enter number:"))

if num%3==0:
    print(num)
else:
    print(num**3)

'''

#wap to check whether the given number is even or odd
#If it is even then make it as an odd number if it
#is an odd number then make it as even number
'''
num=eval(input("Enter number:"))

if num%2==0:
    print(num+1)
else:
    print(num)
'''

#wap to check whether the given input is divisible by 3 and 5 . if yes
#Print the actual number or else print string of that number
'''
num=eval(input("Enter number:"))

if num%3==0 and num%5==0:
    print(num)
else:
    print(str(num))
'''

#wap to check whether the given number lies between 1 and 19.
#if it is true square that number or else false cube that number and display the  number
'''
num=eval(input("Enter number:"))

if num>=1 and num<=19:
    print(num**2)
else:
    print(f"{num} and cube of number is",num**3)
'''

#wap to check whether the student has passed or failed.
#If the student got more than 40 marks print 'pass' along with those marks
#If it is not printed Fail along with marks
'''
marks=eval(input("Enter marks:"))

if marks>=40:
    print(f"{marks} you are pass")
else:
    print(f"{marks} you are Fail")
'''

#WAP to check whether a given value is even and in range of 47 to 58 and not in 0
#or odd. if condition is True, to perform display the ascii character. or else to
#perform floor division with 5 and display it.

'''
a = eval(input("Enter a value: "))

if a % 2 == 0 and 47 <= a <= 58 and a != 0:
    print("ASCII Character:", chr(a))
else:
    print("Floor Division by 5:", a // 5)
'''

#WAP to check whether a given value is less than 125 and in between 47 to 125 or
#not. if condition is True, to perform store the given value as key and value as a
#character into the dict or else to append the value in list and display it.
'''
a = eval(input("Enter a value: "))

d = {}
l = []

if a < 125 and 47 <= a <= 125:
    d[a] = chr(a)
    print("Dictionary:", d)
else:
    l.append(a)
    print("List:", l)
'''

#wap to check whether a given character is in alphabet or not.
#If alphabet, display the alphabet with character or else display
#the not alphanbet with character
'''
a= eval(input("Enter character:"))

if ('A'<=a<='Z') or ('a'<=a<='z'):
    print(f'{a} is an character')
else:
    print(f'{a} is not character')
    '''

#wap to check whether a given character is uppercase or other character.
#If uppercase , display the uppercase with character or
#else display the other character with character.
'''
a=eval(input("Enter character:"))

if 'A'<=a<='Z':
    print(f"{a} is uppercase ")
else:
    print(f"{a} is another character ")
'''

#WAP to check whether a given character is lowercase or other character. if
#lowercase, display the lowercase with character or else display the other
#character with character.
'''
a=eval(input("Enter character:"))

if 'a'<=a<='z':
    print(f"{a} is lowercase ")
else:
    print(f"{a} is another character ")


'''

#wap to check whether a given character is uppercase
#Or other character. if uppercase convert to lowercase
#Or else display ascii number
'''
a=eval(input("Enter character:"))

if 'A'<=a<='Z':
    print(a.lower())
else:
    print(ord(a))
'''


#wap to check whether the given character is in lowercase or uppercase
#If it is in lowercase, convert it into uppercase or
#else it is in uppercase and convert it into lowercase , display the value
'''
a=eval(input("Enter character:"))

if ('a'<=a<='z'):
   print(a.upper())
else:
    print(a.lower(),"ascii value is",ord(a))
'''

#Wap to check whether a given character is vowel or consonant.
#If vowel to print 'VOWEL' along with character ,
#If it is not just print 'CONSONANT'
'''
a=eval(input("Enter character:"))

if a in 'A E I O U a e i o u':
    print(f"{a} is VOWEL")
else:
    print("CONSONANT")
'''


#Wap to check whether a given character is a vowel or consonalt.
#if vowel , to print the next character of given character or else print previous characters
'''
a=eval(input("Enter character:"))

if a in 'AEIOU aeiou':
    print("vowel next character is",chr(ord(a)+1))

else:
    print("Consonant previous character is,",chr(ord(a)-1))
'''

#WAP to check whether the given string of the first character is a special symbol
#or not. If a special symbol, to extract and display the middle character or else to
#reverse the string and display the half of the string.



#WAP to check whether a given string of first character is alphabet or not
#if the alphabet prints, reverse the string or else print the middle character.

s = input("Enter a string: ")

if ('A' <= s[0] <= 'Z') or ('a' <= s[0] <= 'z'):
    print("First character is an alphabet")
    print("Reversed String:", s[::-1])
else:
    mid = len(s) 
    print("First character is not an alphabet")
    print("Middle Character:", s[mid])
