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

'''
class Car:

    def __init__(self):

        #instance variable

        self.name="BMW"
        self.color="Red"
        self.cost="1cr"

    def show(self):
        print(f"my car name :{self.name}\n my car color: {self.color}\n car cost is:{self.cost}")


x=Car()

x.show()

'''

'''
#Calling one method into another
class Car:

    def __init__(self):

        #instance variable

        self.name="BMW"
        self.color="Red"
        self.cost="1cr"

        self.show()

    def show(self):
        print(f"my car name :{self.name}\n my car color: {self.color}\n car cost is:{self.cost}")


x=Car()

'''

'''
class Room3:

    def __init__(self,total_std,Tg,Tb,sub):

        self.total_std=total_std
        self.Tg=Tg
        self.Tb=Tb
        self.sub=sub

        print(f"Total students in class {self.total_std}\n"
              f"Total girls count {self.Tg}\n"
              f"Total boys count {self.Tb}\n"
              f"Subject is {self.sub}")


r=Room3(45,20,25,"python")
print()
r1=Room3(50,30,20,"sql")
print()
r2=Room3(60,30,30,"web")
'''
'''
class Room3:

    def __init__(self,total_std,Tg,Tb,sub):

        self.total_std=total_std
        self.Tg=Tg
        self.Tb=Tb
        self.sub=sub

        #self.classinfo()

       

    def classinfo(self):
         print(f"Total students in class {self.total_std}\n"
              f"Total girls count {self.Tg}\n"
              f"Total boys count {self.Tb}\n"
              f"Subject is {self.sub}")
        


e=Room3(100,50,50,"manual")
e.classinfo()
r=Room3(45,20,25,"python")
r.classinfo()

'''

'''
class Room3:

    def __init__(self,total_std,Tg,Tb,sub,*args):

        self.total_std=total_std
        self.Tg=Tg
        self.Tb=Tb
        self.sub=sub
        self.args=args

        #self.classinfo()

       

    def classinfo(self):
         print(f"Total students in class {self.total_std}\n"
              f"Total girls count {self.Tg}\n"
              f"Total boys count {self.Tb}\n"
              f"Subject is {self.sub}\n"
              f"Extra information {self.args} ")
        


e=Room3(100,50,50,"manual","*",90)
e.classinfo()
    
 '''
'''
class Room3:

    def __init__(self,total_std,Tg,Tb,sub,**kwargs):

        self.total_std=total_std
        self.Tg=Tg
        self.Tb=Tb
        self.sub=sub
        self.kwargs=kwargs

        #self.classinfo()

       

    def classinfo(self):
         print(f"Total students in class {self.total_std}\n"
              f"Total girls count {self.Tg}\n"
              f"Total boys count {self.Tb}\n"
              f"Subject is {self.sub}"
               f"Extra information {self.kwargs} ")
        


e=Room3(100,50,50,"manual",mockrating="*",marks=90)
e.classinfo()
        
'''



class Bank:

    def __init__(self):

        self.bal=0.0

    def deposite(self,amt):

        print(f"before deposite total amount : {self.bal}")

        self.bal+=amt

        print(f"After deposite total amount : {self.bal}")


    def withdrawl(self,amt):
        self.bal=self.bal-amt

        print(f"After withdrawl total amount is :{self.bal}")

b=Bank()
Bank.bal=1000
print(Bank.bal) #Not affected by the help of class name

b.deposite(200)

b.withdrawl(50)
        
        
        


