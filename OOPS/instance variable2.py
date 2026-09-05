'''
class Marks:

    def Subject(self):

        self.math=56
        self.eng=75

        #print(self.math)
        #print(self.eng)


m=Marks()

m.Subject()

m.math=90
m.eng=85

print("after modification:")
print(m.math)
print(m.eng)
'''

'''
class Student:

    def data(self):
        self.name="bhakti"

        print(self.name)


s1=Student()

s1.data()

s1.name="sushil"
print("After modification:")
print(s1.name)
'''


'''
class BankAccount:

    def data(self,bal,name):
        self.bal=bal
        self.name=name

        print(self.bal,self.name)

a1=BankAccount()
a2=BankAccount()


#Before modification
print("before modification")
a1.data(10000,"bhakti")
a2.data(20000,"sushil")


#After modification

a1.bal=15000
a2.bal=25000

print("after modification")
print(a1.bal,a1.name)
print(a2.bal,a2.name)
'''


'''
class Employee:

    def salary(self,sal):
        self.sal=sal

        print(self.sal)

e1=Employee()
e2=Employee()

#before modification
print("before mdoification")
e1.salary(30000)
e2.salary(40000)


#after modification
print("After modification")
e1.sal=35000

print(e1.sal)
print(e2.sal)

'''

'''
class Marks:

    def Subject(self):

        self.math=56
        self.eng=75

        #print(self.math)
        #print(self.eng)


m=Marks()

m.Subject()

m.math=90
m.eng=85

print("after modification:")
print(m.math)
print(m.eng)
        
'''


class Marks:

    def Subject(self):

        self.math=56
        self.eng=75

        #print(self.math)
        #print(self.eng)


m1=Marks()
m2=Marks()

m1.Subject()
m2.Subject()

m1.math=95
print(m1.math)
print(m1.eng)

m2.math=80
m2.eng=90
print(m2.math)
print(m2.eng)


