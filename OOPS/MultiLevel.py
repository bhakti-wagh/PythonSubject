


#Multi Level Inheritance

class Grandpa:

    def agriland(self):
        print('Land')

class Father(Grandpa):

    def property(self):
        print("Home")


class Child(Father):

    def Bike(self):
        print("Bike")


c=Child()

c.Bike()
c.property()
c.agriland()
