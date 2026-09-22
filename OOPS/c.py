#Constructor overloading
'''
class Student:

    def __init__(self):

        print("Hello")


    def __init__(self):
        print("World")



s=Student()
'''

'''
#instance method

class Bank:

    def details(self,bname):
        self.bname=bname

        print("Bank class")
        print(f"bank name:{self.bname}")

b=Bank()

b.details("SBI")
'''



class Student:

    def details(self):
        print("student class")


class Employee(Student):

    def Empdetails(self):
        Student.details(self)
        print("Employee class")



class car(Student):
    def Cardetail(self):
        print("car class")


class bike(Employee,car):
    def bikedetail(self):
        Employee.Empdetails(self)
        car.Cardetail(self)
        
        print("bike class")


b=bike()
b.bikedetail()



