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
'''

'''

class Book:

    def info(self):
        self.name="Albatross"
        self.auth="sanem"

        #we not use print() :

    def data(self):
        print(f"Book name :{self.name}")
        print(f"Author name:{self.auth}")



b=Book()

b.info()
b.data()
''



    
    




