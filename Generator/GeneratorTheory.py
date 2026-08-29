Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Generator:->

#Generator is special type of Function
#In generator we generate the sequence of element one by one instead of all ones

#In generator we save memeory


#Syntax:-->
#           def generator_Name(Parameter):
#                   statment
#                   statment
#                   yield data
#           new_Var=generator_Name(argument)

# print(new_Var):-> it will show generator object address

#If We don't want address we use : 1. Traversing
#                                  2. Looping
#                                  3. next()

#   next():-> it is inbuilt function , it will use call the element at one by one


# yield :->  it is a keyword
#       - instead of function we use yield keyword in generator
# :-> we can use multiple keyword at time
#   but it will pause the execution or hold the execution

# if we want to print in single line use: yield data1,data2 ..... / o/p: tuple form()





#Difference between Return And Yield Keyword:

#       Return                   |                       Yield
>>> #- here we can't use multiple         - here we can use mulitple keyword
>>> #   Keyword
>>> #   Ex : return A [correct]           -Ex: yield A
>>> #   Ex : return B [Blankspace]        -Ex: yield B
>>> 
>>> #- Mulitple operation by using        - Mulitple operation by using
>>> #   return keyword                          yield keyword
>>> #Ex: return A,B                       -EX: yield A,B
>>> # o/p: tuple form()                   - o/p: tuple form()
>>> 
>>> #return terminate the compile         - pose the execution /Hold the execution
>>> 
>>> 
>>> 
>>> # how to check memory in bits
>>> #   import sys
>>> #   new_var=sys.getsizeof(object)
>>> 
>>> 
>>> #if i want to stop the exection in middle then use
>>> #   varnmae.close()
>>> #It will stop the iteration
>>> #If i called again next() it will show stopIteration Error
>>> 
>>> 
>>> #Suppose In Generator Whenever we are storing a data into container and we use
