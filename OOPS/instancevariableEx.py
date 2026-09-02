'''
class Animal:

    name="dog"
    colur="black"

    def data(self):
        #Using className
        #print(f"Name of animal is:{Animal.name}")

        #Using object
        print(f"Name of animal is:{self.name}")


a=Animal()

#modify with classname to class Variable

Animal.name="cat"


#Modify with object to class Variable

#a.name="elep" #:-> it will show first one not modify
#If we pass object in access part then it will modify 

a.data()
'''

'''

class Book:

    def info(self):
        self.name="Albatross"
        self.auth="sanem"

        #we not use print() :

    def data(self):
        print(f"Book name :{self.name}")
        print(f"Author name:{self.auth}")



b=Book()

b.info()
b.data()
'''



'''
#without parameter
class Bank:

    def Total_Balance(self):
        self.amount=500

        print(f"Total balance is :{self.amount}")

    def Deposite(self):
        self.bal=500

        self.amount+=self.bal
        print(f"After the deposite total amount is:{self.amount}")


    def withdrawl(self):
        self.bal=200

        self.amount-=self.bal
        print(f"After withdral:{self.amount}")


b=Bank()

b.Total_Balance()
b.Deposite()
b.withdrawl()
'''

'''
#with parameter and without paramter
class Bank:

    def Total_Balance(self):
        self.amount=500

        print(f"Total balance is :{self.amount}")

    def Deposite(self,bal):
        

        self.amount+=self.bal
        print(f"After the deposite total amount is:{self.amount}")


    def withdrawl(self,bal):
        

        self.amount-=self.bal
        print(f"After withdral:{self.amount}")


b=Bank()

b.Total_Balance()
b.Deposite(500)
b.withdrawl(200)
'''



class Flipkart:

    productName="laptop"
    cost=25000
    TotalProduct=3
    Add="pune"


    def Product_data(self):
        print(f"product name is:{self.productName}")
        print(f"Total cost is :{self.cost}")
        print(f"Total product is:{self.TotalProduct}")


    def Address(self):
        print(f"Current Address is :{self.Add}")


    def Modification_data(self,new_cost,TP):
        self.cost=new_cost
        self.TotalProduct=TP

        print(f"Updated cost price is:{self.cost}")
        print(f"Updated total product is :{self.TotalProduct}")
        


f=Flipkart()

f.Product_data()
f.Address()

f.Modification_data(50000,20)

print(f.productName)
print(f.cost)
print(f.TotalProduct)
print(f.Add)
        
    
    
    




