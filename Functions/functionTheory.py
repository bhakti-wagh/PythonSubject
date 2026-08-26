#Function:->

#why we want to use Function:->
#if you want to avoid code repetation , same code again i want to reuse
#code in systamatic order
#repetation



#Defination:->   Set of code / Block of code It will execute When we calling the function
#              without calling function  if we execute it will show blank space


#Function totaly depends on syntax

#Types of Function:-
#                       1.Predefined function/inbuilt function(alerady it define in system)
#                       2. UserDefined Function(customaize function)




# USERDEFINE FUNCTION:-> SYNTAX :-> 2 

#  1.without using return keyword
#  2.with using return keyword



#1. without using return keyword:->

#   Syntax:->
#               def function_name(parameter):   ------function declaration
#                       statement
#                       statement ----------Block of code / set of code

#               function_name(argument)-------function call


#:->  def ---- keyword
#:-> in the place of function_name:-> name of the program (any name)
#:-> (parameter):-> it is part of optional
#:-> meaning of parameter:-> means  it is nothing but variable name

#:-> meaning of argument:-> it is optional
#                           It is nothing but variable value

#Parameter is always pointing to argument

#what is difference between function declaration and function calling



#LHS==RHS


#types of argument while calling the functions
#1. Positional argument
#2.  Keyword argument
#3. only positional argument
#4. only keyword argruments
#5. variable positional arguements(*args)
#6. vaiabale keyword arguments(**kwargs)
#7. combination of only positional arguement and only keyword argument
#8. combination of *args and **kwargs


# Position arguments :-> how much we are passing parameter that much we have to pass argument
#any one parameter is miss match it will show Type Error (without using == symbol)


#Kwyword aruments-> in keyword argument we have to pass varname=value


# what is difference between only positional argument and only keyword arguments??
#-> in positional argument 

#3. only positional argument:-> (/)

# Before the forward slash(/) we can pass only positional argument but  after the slash we can
#pass both either(positional or keyword argument)


'''
def demo(a,b,/,c):
    print(a,b,c)

demo(10,20,c=30)#10 20 30

'''


#4. only keyword argument:-> (*)

# Before the (*) we can pass both either (positional or keyword argument) but after the (*)
# we can pass keyword argument

'''
def demo(a,b,*,c):
    print(a,b,c)

demo(10,20,c=30)#10 20 30

'''







