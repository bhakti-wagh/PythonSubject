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





