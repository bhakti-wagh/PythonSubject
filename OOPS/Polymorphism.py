
'''
print(1+2)
print("1"+"2")
'''

'''

print(len("Bhakti"))

x=["bhakti",2]

print(len(x))

'''
#There is 4 ways to implement polymorphism

#1. Duck Typing:
'''
class Duck:

    def Swim(self):
        print("I am duck and i can swim")

    def Speak(self):
        print("Quack quack")

class Dog:

    def Swim(self):
        print("I am Dog and i can swim")

    def Speak(self):
        print("Bow Bow")



def display(duck):

    duck.Swim()
    duck.Speak()
    print("Information displayed")


d=Duck()
g=Dog()
display(g)
  '''



#2.Operator Overloading:


print(1-2)
print("1"2)
