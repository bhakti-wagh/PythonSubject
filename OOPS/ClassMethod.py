
#Class Method:->

#Class Method only working for Class Data

#In class method object creation not required/ not mandadatory

#In class method by default it will take it as a 'cls'parameter

#cls:-> specail parameter , it will pointing to main class

#DEF:-> Any method decorated with  '@classmethod', then we call it as
#       class Method

#* :-> class method only working for class data

#Syntax:->
#           class classname:

#                   @classmethod
#                   def method_name(cls):
#                       stmt
#           object=classname():-> not required


#   Access Through object
#       object.method_name()

#  Access Through classname
#       classname.method_name()


# while you miss @classmethod it will act as an 'instance Method'


'''
class wish:

    @classmethod
    def greet(cls):

        print(cls)


w=wish()

print(w)#<__main__.wish object at 0x0000017D7A97AE40>

w.greet()#<class '__main__.wish'>


wish.greet()#<class '__main__.wish'>
'''




#Access class variable into the class method:
#   2 ways:-> 1. using cls
#             2. using classname

#Both will be work

'''

#EX:

#Using cls
class Car:
    name="BMW"

    @classmethod
    def data(cls):
        print(cls.name)


Car.data()#BMW



#using classname
class Flower:
    name="Rose"

    @classmethod
    def data(cls):
        print(Flower.name)

Flower.data()#Rose
'''




#Modification class variable inside  class method

#2 ways: 1. using cls
#        2. using classname

# both will be work
'''

class Bank:

    branch="pune"

    @classmethod

    def data(cls):
        #print(cls.branch)

        #Modification inside by cls
        cls.branch="Beed"
        #print(cls.branch) #working

        #Modifcation inside by classname
        Bank.branch="kothrud"
        #print(Bank.branch)#Working

b=Bank()

b.data()
'''





#Modification class variable outside of class
#   1. only classname
# by the help of object it will won't work


'''
class Flower:

    name="Rose"

    @classmethod
    def data(cls):
        print(cls.name)

f=Flower()

#f.data()#Rose

#Modify with object

#f.name="lily"


#Modify with classname

Flower.name="lily"
f.data()#lily

'''





