

class Flower:

    def show(self):
        print("Rose Flower")


class Animal(Flower):

    def show1(self):
        print("Dog Animal")


class Vehicle(Flower):

    def show2(self):
        print("Car vehicle")


class Vegitables(Animal,Vehicle):

    def show3(self):
        super().show1()
        super().show2()
        print("Bhindi vegitables")



v=Vegitables()
v.show3()
print(Vegitables.__mro__)

