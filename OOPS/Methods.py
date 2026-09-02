
#Methods:

# def: A function inside the class we can call it as Methods

# 3 types of methods:
# 1. instance Method
# 2. Class Method
# 3. Static Method


#What is the meaning of Instance Method?
#-> A method it will accept only first parameter of the object address
# -> then we call it as instance Method
#-> by default it take [Self]  special parameter



#Syntax:->    class ClassName:
#
#                   def Method_name(self):
#                           stmt
#           object=ClassName()


# : self is always pointing to a object
# : it is a special parameter

#> if we want to access instance method it is mandatory to create a object

# To fetch  instance Method outside we have [2] ways:
#  1. by using className
#  2. by using object



#1. by using className:  expecility we have to use object
#       syntax :    ClassName.method(object)


#2. by using object:  internally it take a object
#       syntax:    object.method() :-> internally :-> object.method(object)




#> Instance Variable :-> it will work only for instance Method and constructor



#How to access and modify the class Variable into instance method

# 1. Access                             Modify
# - by className                    :-> using ClassName :->Modify
# - by className                    :-> using object :-> not Modify

# 2. Access                              Modify
# - by object/self                  :-> using ClassName :-> Modify
#                                   :-> using object    :-> Modify



'''
class Animal:

    name="dog"
    colur="black"

    def data(self):
        #Using className
        #print(f"Name of animal is:{Animal.name}")

        #Using object
        print(f"Name of animal is:{self.name}")


a=Animal()

#modify with classname to class Variable

Animal.name="cat"


#Modify with object to class Variable

#a.name="elep" #:-> it will show first one not modify
#If we pass object in access part then it will modify 

a.data()
''''



#How to access one method into another instance method:->

# by two ways :
# 1. using object:   object/self.methodName()
# 2. using classname:  classname.methodName(object/self)











