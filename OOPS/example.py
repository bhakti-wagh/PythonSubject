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

'''

'''
class Vehicle:

    def start(self,vname):
        self.vname=vname
        print(f"Vechicle name :{self.vname}")


class Bike(Vehicle):

    def start(self,bname):
        super().start('car')
        self.bname=bname
        print(f"Bike name:{self.bname}")


b=Bike()
b.start('splinder')

'''

'''
class BankAccount:

    def __init__(self,hname,bal):
        self.hname=hname
        self.bal=bal
        self.show()

    def show(self):
        print(f"Holder name :{self.hname}")
        print(f"Balance :{self.bal}")



class SavingAccount(BankAccount):

    def __init__(self,irate):
        super().__init__('bhakit',5000)
        self.irate=irate
        self.show2()


    def show2(self):
        print(f"Interest rate :{self.irate}")

        

class SeniorSavingAccount(SavingAccount):

    def __init__(self,age):

        super().__init__(0.1)
        self.age=age

        if age>=60:
            print("You are eligible for extra interest")
            print(self.bal*self.irate)
        else:
            print("You are not eligible for extra interest")

        print(f"age :{self.age}")
        
s=SeniorSavingAccount(65)
''' 
'''
class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        

    def details(self):
        print(f"Person name:{self.name}")
        print(f"Age :{self.age}")


class Company:

    def __init__(self,cname,sal):
        self.cname=cname
        self.sal=sal
        


    def details(self):
        print(f"Company name:{self.cname}")
        print(f"Salary is :{self.sal}")


class Employee(Person,Company):

    def __init__(self):
        Person.__init__(self,'bhakit',22)
        Company.__init__(self,'qspider',5000)
        self.show()


    def show(self):
        Person.details(self)
        Company.details(self)



e=Employee()
'''



'''
class Company:

    def __init__(self,cname):
        self.cname=cname

        print(f"Company name:{self.cname}")



class Employee(Company):

    def __init__(self,Eid,Ename):
        super().__init__('qspider')
        self.Eid=Eid
        self.Ename=Ename
        self.show()


    def show(self):
        print(f"Employee id :{self.Eid}")
        print(f"Employee name :{self.Ename}")



class Manager(Company):

    def __init__(self,mname,dept):
        self.mname=mname
        self.dept=dept

        print(f"Manager name :{self.mname}")
        print(f"Department :{self.dept}")



e=Employee('E01','sushil')
m=Manager('bhakti','IT')
'''

'''
parent class=Book:-> title, author,isbn,avilable
Method=get_details,mark_unavailble,mark_available

child class=Borrowed Book:-> borrower_name,duedate
Methods=borrow():-> borrowedetails, marks the book as borrowed
Return _book() marks avil, remove borrower details

'''

class Book:

    def __init__(self, title,author,isbn,avail):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.avail=avail
    


    def get_details(self):
        print(f"Book title :{self.title}")
        print(f"Author of book:{self.author}")
        print(f"Isbn :{self.isbn}")
        print(f"Available :{self.avail}")


    def marks_unavailable(self):
        self.avail=False
        print("Marks the book as not available.")


    def marks_available(self):
        self.avail=True
        print("Marks the book as available.")


class BorrwedBook(Book):

    def __init__(self,borrower_name,due_date):
        super().__init__('Albatross', 'sanem', 4654654, False)
        self.borrower_name=borrower_name
        self.due_date=due_date
        self.borrow()


    def borrow(self):

        if self.avail:
             self.marks_unavailable()
             print(f"Borrower name :{self.borrower_name}")
             print(f"due_date:{self.due_date}")

        else:
            print("Book is already borrwoed")


    def return_book(self):
        self.marks_available()
        self.borrower_name 
        self.due_date 
        print("Book returned.")

        

b=BorrwedBook('bhakti','09/sept') 

b.get_details()
print()

b.borrow()
print()








