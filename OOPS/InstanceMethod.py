'''

# way1
class Flower:

    flower_Name="Rose"

    def type(self):
        print(f"Flower Type is {self.flower_Name}")


f=Flower()

#using self object to access value :

#1. by using classname modification

Flower.flower_Name="Jasmin"

#2. by using object modification

Flower.flower_Name="lily"

 
f.type()


#It affected both classname or object
#o/p: Flower Type is Jasmin

'''

'''
#way2:

class Flower:

    flower_Name="Rose"

    def type(self):
        print(f"Flower Type is {Flower.flower_Name}")


f=Flower()

#using self object to access value :

#1. by using classname modification

#Flower.flower_Name="Mogra" #o/p: Flower Type is Mogra

#1. by using classname modification

f.flower_Name="lily"  #It not affected it show original data
 
f.type()

'''

'''

#way3:

class Flower:

    flower_Name="Rose"

    def type(self):
        print(f"Flower Type is {f.flower_Name}")


f=Flower()

#using self object to access value :

#1. by using classname modification

Flower.flower_Name="Mogra" #o/p: Flower Type is Mogra

#1. by using classname modification

#f.flower_Name="lily"  #It not affected it show original data
 
f.type()


'''

'''

class Employee:
    sal=7000

    def data(self):
        #by using className
        print(f"salary is {Employee.sal}")


e=Employee()

#Modification by className

Employee.sal=8000
#It will affected

e.data() #salary is 8000



class Employee:
    sal=7000

    def data(self):
        #by using className
        #print(f"salary is {Employee.sal}")

        #by using object (recommended part)
        print(f"salary is {self.sal}")


e=Employee()

#Modification by className

Employee.sal=8000
#It will affected

#Modification by object
e.sal=5000 #salary is 5000

e.data() #salary is 8000
'''


'''
class Flower:

    def type(self):
        self.name="Rose"
        self.colour="red"

    def data(self):
        print(f"flower name is {self.name}")
        print(f"Flower colour is{self.colour}")


f= Flower()

f.type()
f.data()
'''


'''
#instance method by using parameter

class Student:

    def info(self,name,age):
        self.name=name
        self.age=age
        self.data()


    def data(self):
        print(self.name)
        print(self.age)

s = Student()

s.info("sanem",23)
'''

'''
class Bank:

    name="SBI"
    branch="pune"
    date="16aug"
    

b=Bank()
#by using className access
print(Bank.name)#SBI
print(Bank.branch)#pune
print()
#by using object access

print(b.date)#16aug

'''



'''
class Bank:

    name="SBI"
    branch="pune"
    date="16aug"
    

b=Bank()
b1=Bank()
print(Bank.__dict__)
'''

'''
class Greeting:
    def say_hello(self,name):
        print(f"Hello ,{name}! welcomt to python")


g1=Greeting()

g1.say_hello("bhakti")
Greeting.say_hello(g1,"Sushil")
'''


'''
class Person:

    def data(self,name,age):
        self.name=name
        self.age=age

        print(f"Person name is:{self.name}")
        print(f"age is :{self.age}")

p=Person()

p.data("bhakti",22)

#o/p
Person name is:bhakti
age is :22
'''


'''
class Dog:

    name="vanki"
    breed="ameri"

    def data(self):
        print(f"Dog name is :{self.name}")
        print(f"Dog breed is:{self.breed}")

d=Dog()

d.data()
#o/p:
Dog name is :vanki
Dog breed is:ameri

'''


'''
class Fan:

    def data(self,brand,price):
        #self.brand=brand
        #self.price=price
        print(f"brand name is:{brand}")
        print(f"price is:{price}")

f=Fan()

f.data("bajaj",25000)
#o/p
brand name is:bajaj
price is:25000

'''

'''
class Employee:

    def info(self,name ,salary):
        self.name=name
        self.salary=salary

        print(f"employee name :{self.name}")
        print(f"before increase salary:{self.salary}")

    def increase(self,salary):
        self.salary+=salary

        print(f"Increase salary by:{self.salary}")


e=Employee()

e.info("bhakti",10000)
e.increase(5000)


#o/p
employee name :bhakti
before increase salary:10000
Increase salary by:15000
'''


'''
class GamePlayer:

    def data(self,name,score):
        self.name=name
        self.score=score

        print(f"player name:{self.name}")
        print(f"score is:{self.score}")


    def incre(self,score):

        self.score+=score

        print(f"Increase score:{self.score}")



g=GamePlayer()

g.data("sushil",100)

g.incre(200)

#o/p:
player name:sushil
score is:100
Increase score:300

'''




#access and modify class variable
'''
class Student:

    name="bhakti"

    def data(self):

        print(self.name)



s=Student()

#s.name="apeksha"

Student.name="apeksha"

s.data()


'''
'''
class Student:

    name="bhakti"

    def data(self):

        print(Student.name)



s=Student()

s.name="apeksha"

#Student.name="apeksha"

s.data()

'''


'''
class Book:

    def data(self):
        self.name="rosee"

        print(self.name)


        #1way

        self.name="catee"
        print(self.name)

b=Book()

b.data()
'''

class Book:

    def data(self):
        self.x="abc"

        print(self.x)

    def info(self,new):

        self.x=new

        print(self.x)


b=Book()


#b.info("ghk")

Book.info("ghk")


    




        
