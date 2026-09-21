'''
class School:

    def __init__(self,name,mobile,age,sname):

        self.name=name
        self.mobile=mobile
        self.age=age
        self.sname=sname
        self.display()


    def display(self):
        print(f"Name :{self.name}")
        print(f"Mobile:{self.mobile}")
        print(f"Age:{self.age}")
        print(f"School name:{self.sname}")



class Twelth(School):

    def __init__(self,clgname,Tmarks):

        super().__init__('Bhakti',789456123,22,'ABC School')    

        self.clgname=clgname
        self.Tmarks=Tmarks
        self.show()


    def show(self):
        print(f"college name :{self.clgname}")
        print(f"Twelth marks:{self.Tmarks}")



class Degree(Twelth):

    def __init__(self,DegName,course,grade):

        super().__init__('pvpclg',75)
        self.DegName=DegName
        self.course=course
        self.grade=grade
        self.show2()

    def show2(self):
        print(f"Degree clg name:{self.DegName}")
        print(f"course :{self.course}")
        print(f"Grade :{self.grade}")


d=Degree('BVDU','BCA','o grade')

'''


'''
class Bank
def__init__(self,c_name,bal,deposite)

if bal<5000:
    not eligible for current account
elif bal*01

'''



class Bank:
    def __init__(self,c_name,bal,deposite):
        self.c_name=c_name
        self.bal=bal
        self.deposite=deposite
        self.show()

        if bal>5000:
            print("Not eligible for current account")

        else:
            print(bal*0.1)


    def show(self):
        print(f"Customer name :{self.c_name}")
        print(f"balance is :{self.bal}")
        print(f"deposite is :{self.deposite}")


class Details(Bank):

    def __init__(self):

        super().__init__('Bhakti',2000,500)


d=Details()





        
