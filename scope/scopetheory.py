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

# 3. global variable we can do modification outside without using any keyword
#   but if we done any modification inside the function without keyword it will show
#   unboundedLocal error

# How to do modification for global variable inside----?

# 1. By using global keyword:->  global :-> it is keyword that use do modification

# Example:->
'''
a=100 #Global variable

def display():
    global a
    b=10 #local variable
    print(f"the given variable is local variable {b}")

    a=a+400
    print(f"The local variabel is global varaible {a}")

display()

print("Modification for global variable (outside)")

a=a+100

print(a)


o/p

the given variable is local variable 10
The local variabel is global varaible 500
Modification for global variable (outside)
600
'''





# > NonLocal Variable

#any varaible present between two function that type of variable call as a NonLocal variable 
