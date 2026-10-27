from abc import ABC, abstractmethod

'''
class Test(ABC):

#abstract class and abstract method structure

    @abstractmethod
    def demo(self):
        pass

'''

#case 1:
'''
class Test(ABC):

#abstract class and abstract method if we work both at time it will show error we can't
#create a object of abstract class 

    @abstractmethod
    def demo(self):
        print("demo method")


t=Test()
t.demo()
'''


#case 2
'''
class Test(ABC):

#whenever we not use abstract method then we can create a object of abstract class

    def demo(self):
        print("demo method")

t=Test()
t.demo()
'''


#case 3
'''

class Test:
    #whenever we not use abstract class then we can create a object of class

    @abstractmethod
    def demo(self):
        print("demo method")

t=Test()
t.demo()
'''



#case 4:
'''
class Test:
    #it will work like as concrete method
    
    def demo(self):
        print("demo method")

t=Test()
t.demo()

'''


#CASE 5
'''
class Test:
  
    def __init__(self):
        print("constructor")

t=Test()

'''


#in pareent class only use for hiding purpose
#and we use child class for hiding data but method_name and variable that name should be
#as it is 
'''
class Information(ABC):

    @abstractmethod
    def subjec_name(self,name):

        pass

    @abstractmethod
    def total_score(self,total):
        pass
    



class display(Information):

    def subjec_name(self,name):
        self.name=name

        print(f"Subject name:{self.name}")


    def total_score(self,total):
        self.total=total

        print(f"Total score :{self.total}")


r=display()
r.subjec_name("python")
r.total_score(100)
'''


'''
TypeError: Can't instantiate abstract class display without an implementation for abstract method 'total_score'
class Information(ABC):

    @abstractmethod
    def subjec_name(self,name):

        pass


    @abstractmethod
    def total_score(self,total):
        pass


class display(Information):

    def subjec_name(self,name):
        self.name=name

        print(f"Subject name:{self.name}")


    
r=display()
r.subjec_name("python")

#in paraent class how much we are creating abstract method that much we have to implement
#into child class
#other wise it will show error '''



'''
from abc import ABC, abstractmethod

class Emp(ABC):

    @abstractmethod
    def Role(self,role_name):
        pass


    @abstractmethod
    def sal(self,total_sal):
        pass

    @abstractmethod
    def YOE(self,year):
        pass

    @abstractmethod
    def EID(self,eid):
        pass


class display(Emp):

    def __init__(self,ename,age,loc):
        self.ename=ename
        self.age=age
        self.loc=loc

        print(f"ename is :{self.ename}")
        print(f"Age is :{self.age}")
        print(f"location is:{self.loc}")


    def Role(self,role_name):
        self.role_name =role_name

        print(f"Role name :{self.role_name}")


    
    def sal(self,total_sal):
        self.total_sal =total_sal

        print(f"Total salary :{self.total_sal}")

    
    def YOE(self,year):
        self.year =year

        print(f"year of experience :{self.year}")


    def EID(self,eid):
        self.eid=eid

        print(f"Employee id :{self.eid}")



d=display("Bhakti",22,'pune')

d.Role("Hr")
d.sal(25000)
d.YOE(5)
d.EID("B001")


'''





class SBI(ABC):

    @abstractmethod

    def __init__(self,HN,bal,acc_num):
        pass


    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdrawl(self,amount):
        pass





class ATM(SBI):

    def __init__(self,HN,bal,acc_num):
        self.HN=HN
        self.bal=bal
        self.acc_num=acc_num
        print(f"Holder name :{self.HN}")
        print(f"Balance :{self.bal}")
        print(f"Account number:{self.acc_num}")



    def deposite(self,amount):
            self.amount=amount

            print(f"Before deposite total amount {self.bal}")
            self.bal+=amount

            print(f"after deposite  amount:{self.bal}")
            

    
    def withdrawl(self,amount):
        self.bal-=amount
       
        print(f"Withdrawl amount:{self.bal}")




a=ATM("bhakti",10000,123456789121)

a.deposite(5000)

a.withdrawl(2000)


        
        



    
