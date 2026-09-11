


#Multi Level Inheritance


'''
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
'''






class Dad:

    def money(self):
        print("1cr")

class child1(Dad):

    def money(self):
        super().money()
        print("50Lak")

class child2(child1):

    def money(self):
        super().money()
        print("25Lak")


c=child2()

c.money()
