Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#Bitwise Operator:->

19 & 13
1
bin(19)
'0b10011'
bin(1)
'0b1'

24 & 17
16

54 & 32
32

47 &37
37

24 &19
16

16 &8
0


#It will convert the given integer number into binary digits and perform Bit by bit         operation.
#Integer is the only data type which supports bitwise operator.

#There are 6 types of Bitwise Operator
#1.Bitwise and(&)
#2.Bitwise or(|)
#3.Bitwise xor(^)
#4.Bitwise not(~)
#5.Bitwise left shift(<<)
#6.Bitwise right shift(>>)

#1.Bitwise and(&):->
#It will convert given integer number into binary digits and perform bit by bit andoperand
#Truth Table:>
#  0-0:->0
#  0-1:->0
#  1-0:->0
#  1-1:->1


45 & 63
45

#Above examples are bitwise and


#2.Bitwise or(|):->
#It will convert the given integer number into binary digit  and perform bit by bit 'or'    operation.
#Truth Table:>
#  0-0:->0
#  0-1:->1
#  1-0:->1
#  1-1:->1

30 | 25
31

42 | 33
43

#3.Bitwise xor(^):->
#If both the operands are same then o/p will be zero
#Truth Table:>
#  0-0:->0
#  0-1:->1
#  1-0:->1
#  1-1:->0

21^20
1

38^33
7

29|19
31

44|22
62

53|39
55

14^7
9

39^30
57

24^17
9


#4.Bitwise not(~):->
#It will invert the result[+->- , - -> +]
#Syntax:- ~op1
#Formula:->   -(op1+1)

~20
-21

~-
SyntaxError: invalid syntax
~-31
30


~89
-90

~63
-64

~-64
63
~100
-101

~-101
100


~44
-45

#5.Bitwise left shift(<<):->

17<<3
136
bin(136)
'0b10001000'
>>> 
>>> #syntax :-> op1<<n -> n must be integer
>>> #It will shift the osition of binary digits towards left hand side
>>> 
>>> 18<<3
144
>>> bin(18)
'0b10010'
>>> bin(3)
'0b11'
>>> 
>>> 
>>> #5.Bitwise right shift(>>):->
>>> 17>>3
2
>>> 
>>> #Syntax:-> op1>>n -> n must be integer
>>> #It will shift the position of binary digits towards right hand side
>>> 
>>> 75>>3
9
>>> 
>>> 79>>2
19
>>> 
