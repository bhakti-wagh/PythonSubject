                               #Scope

# The place of the variable

# Types of Scope:

# 1. Local variable
# 2. Global Variable
# 3. NonLocal variable



# > Local Variable :

# 1. Any variable present inside the function then we can call it as a local variable
# 2. Local variable we can't access outside directly if we access it will show --NameError--

# 3. How to Access local variable outside  By the help of return  Keyword


# Example:-->

 #   def spam():
 #      name="python"---> local variable
 #      print(name) --> correct
 #  spam()----o/p "python"

 #  print(name) ---> NameError



# Example:-->

#       def spam():
#           name="Python"
#           return name
#       new_variable=spam()
#       print(new_variable)----->o/p "Python"



#Examples:

'''
def spam():
    a=100
    a+=50
    return a

x=spam()
print(x)


def spam1():
    b="python"
    print(b)

spam1()



'''


# > Global variable:

# 1.Any variable is present outside the fucntion then we can call it as a global variable.
# 2.Golbal variable we can access any where into the function means we can access inside the
#    function or outside the function it will work






