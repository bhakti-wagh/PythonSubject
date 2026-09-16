
#by using object
class Flower:

    def show(self):
        print("Rose")


class Color:

    def show1(self):
        f=Flower()
        f.show()
        print("Red color")

c=Color()
c.show1()



print()
print()

#by using instance Variable
class Flower:

    def show(self):
        print("Rose")


class Color:

    def show1(self):
        self.x=Flower()
        self.x.show()
        print("Red color")

c=Color()
c.show1()

print()
print()

#by using classname


class Flower:

    def show(self):
        print("Rose")


class Color:

    def show1(self):
       
        Flower.show(self)
        print("Red color")

c=Color()
c.show1()





