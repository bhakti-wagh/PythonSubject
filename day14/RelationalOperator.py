Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

# Relational Operator
# It is used to compare between given 2 or more operands
#there are 6 types in Relational operators

#1.Relational equals to (==)
#2.Relational not equals to (!=)
#3.Relational greater than(>)
#4.Relational lesser than(<)
#5.Relational greater than or equals to (>=)
#6.Relational lesser than or equals to (<=)


#1.Relational equals to (==):->
#it will compare between 2 operands and gives the result as True only if both the operands
# are same.

#Syntax:->  operand1==operand2
#Realtional equals to operator is also knwon as comparision operator.

#Examples:

10==10
True

12.3==12
False

'abc'=='abc'
True

#2.Relational not equals to (!=):->
# It is used to compare between 2 operandsa and gives the result as True only if both the operands are different (not same)
#syntax:->  Operand1 != Operand2

23!=20
True

45.0!=45
False

'abc'!='ABC'
True

#3.Relational greater than(>):->
#It will give result as true only if operand1 is greater than operand2
#Syntax:->  op1>op2
#Complex and dict are not supported for realtional '>' than operator.
#whenever a string value has to be compared with realtion '>' operator, then it will        Compare based on ASCII Values
#to find ASCII Value we want ord()
#ord():-> it is a inbuilt function used to give the ASCII value for a Particular char
#Syntax:-> ord('char')

50>20
True

'abc'>'ABC'
True

[10,20,30]>[30,20,10]
False

{45,50}>{7,10}
False
#set output will be unpredictable

True>False
True

45.9>78.0
False

#4.Relational lesser than(<):->
##It will give result as true only if operand1 is lesser than operand2
#Syntax:->  op1<op2
#whenever a string value has to be compared with realtion '>' operator, then it will        Compare based on ASCII Values
#Complex and dict are not supported for realtional '<' than operator.

89<20
False

10<5
False

5<10
True

'abc'<'ABC'
False

'bhakti'<'sushil'
True

[10,20,30]<[30,20,10]
True


{45,50}<{7,10}
False

2j+8<8j<2
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    2j+8<8j<2
TypeError: '<' not supported between instances of 'complex' and 'complex'

{1:20}<{3:30}
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    {1:20}<{3:30}
TypeError: '<' not supported between instances of 'dict' and 'dict'



#5.Relational greater than or equals to (>=):->
##It will give result as true only if operand1 is greater than or equal to operand2
#Syntax:->  op1>=op2
#Complex and dict are not supported for realtional '>=' than operator.
#whenever a string value has to be compared with realtion '>=' operator, then it will        Compare based on ASCII Values


45>=45
True

10.5>=10.6
False

4j+9>=6j+66
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    4j+9>=6j+66
TypeError: '>=' not supported between instances of 'complex' and 'complex'

True>=False
True

'mina'>='mona'
False

[45,90,60]>=[45,90,59]
True

(45,90,6)>=(45,90,59)
False

{90,60}>={50,30}
False



#6.Relational lesser than or equals to (<=):->
##It will give result as true only if operand1 is lesser than or equal to operand2

#Syntax:->  op1<=op2
#Complex and dict are not supported for realtional '<=' than operator.
#whenever a string value has to be compared with realtion '<=' operator, then it will        Compare based on ASCII Values
>>> 
>>> True<=False
False
>>> 'mina'<='mona'
True
>>> 
>>> [45,90,60]<=[45,90,59]
False
>>> 
>>> (45,90,6)<=(45,90,59)
True
>>> {90,60}<={50,30}
False
>>> 
>>> 4j+9<=6j+66
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    4j+9<=6j+66
TypeError: '<=' not supported between instances of 'complex' and 'complex'
>>> 
>>> 45<=45
True
>>> 
>>> 10.5<=10.6
True
