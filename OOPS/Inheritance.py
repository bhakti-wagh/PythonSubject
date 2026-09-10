
#Single Level inheritance:


class Dad:
    cash=10000

    def villa(self):
        print("dad's villa")


class Child(Dad):

    def Home(self):
        print("Dad's Gift")

'''
d=Child()

d.villa()
d.Home()
print(d.cash)

'''


print(dir(Dad))




    
