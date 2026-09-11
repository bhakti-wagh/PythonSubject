


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




'''
class Dad:

    def money(self):
        print("1cr")

class child1(Dad):

    def money(self):
        #super().money()
        Dad.money(self)
        print("50Lak")

class child2(child1):

    def money(self):
        #super().money()
        child1.money(self)
        print("25Lak")


c=child2()

c.money()
'''




'''


class  Flower:

    def __init__(self):

        print("Flower class")


class Color(Flower):

    def __init__(self):

        #super().__init__()
        #Flower.__init__(self)

        print("Color class")


class Type(Color):

    def __init__(self):
         
         #super().__init__()
         Color.__init__(self)
         Flower.__init__(self)

         print("Type Class")


t=Type()

print(dir(Type))


'''






'''
class Institute:

    def Information(self,In,Stack,Fee):

        self.In=In
        self.Stack=Stack
        self.Fee=Fee

        print(f"Institute name is :{self.In}")
        print(f"Student course name is :{self.Stack}")
        print(f"Total Fee is :{self.Fee}")



class Student(Institute):

    def Subject_Info(self,Sn,Tc,Dur):
        self.Sn=Sn
        self.Tc=Tc
        self.Dur=Dur

        print(f"subject name is {self.Sn}")
        print(f"Total class {self.Tc}")
        print(f"Duration of class {self.Dur}")

class Result(Student):

    def Final_Stage(self,Tm,Grade):
        self.Tm=Tm
        self.Grade=Grade

        print(f"Total marks {self.Tm}")
        print(f"Grade is :{self.Grade}")


r=Result()

r.Final_Stage(85,'A')
r.Subject_Info("Python",3,'4month')
r.Information("qspider","Python Stack",45000)


'''

class Employee:

    def __init__(self,ComName,TotalMemeber,HighestPack):
        self.ComName=ComName
        self.TotalMemeber=TotalMemeber
        self.HighestPack=HighestPack
        self.data()


    def data(self):
        print(f"Company name  {self.ComName}")
        print(f"Total memeber {self.TotalMemeber}")
        print(f"Highest Package {self.HighestPack}")


class Staremp(Employee):

    def __init__(self,sal,yoe,rol):
        self.sal=sal
        self.yoe=yoe
        self.rol=rol
        self.Info()

    def Info(self):
        super().__init__('testyantra',100,'10lack')
        print(f"Salary is : {self.sal}")
        print(f"year of Experience {self.yoe}")
        print(f"Role of emp :{self.rol}")



class Rules(Staremp):

    def __init__(self,intime,outime,rolename):
        self.intime=intime
        self.outime=outime
        self.rolename=rolename
        self.check()


    def check(self):

        super().__init__(45000,2,'data Analysis')
        print(f"In time  :{self.intime}")
        print(f"Out time :{self.outime}")
        print(f"role name is :{self.rolename}")



r=Rules('11am','6pm','sde')


