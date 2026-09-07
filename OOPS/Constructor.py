'''
class Data:

    def __init__(self):

        print("First class")

d=Data() #By using onject
Data.__init__(d) #By using classname
'''

'''
class Bhakti:

    def __init__(self):
        print("Afternoon")


    def __init__(self):
        print("Evening")


b=Bhakti() #Constructor Overloading

'''

'''
class Student:

    def __init__(self):

        print("Student class")

    def show(self):
        print("Show class")

s=Student()

s.show()
'''


'''

#calling instance method into the constructor

class Student:

    def __init__(self):

        print("Student class")

        self.show()

    def show(self):
        print("Show class")

s=Student()

'''

'''
class Car:

    def __init__(self):

        #instance variable

        self.name="BMW"
        self.color="Red"
        self.cost="1cr"

        print(f"my car name :{self.name}\n my car color: {self.color}\n car cost is:{self.cost}")


x=Car()

'''


#Ex6: constructor + instance method without parameter


class Car:

    def __init__(self):

        #instance variable

        self.name="BMW"
        self.color="Red"
        self.cost="1cr"

    def show(self):
        print(f"my car name :{self.name}\n my car color: {self.color}\n car cost is:{self.cost}")


x=Car()

        


