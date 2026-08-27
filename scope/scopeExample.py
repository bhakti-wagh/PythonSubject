'''
def spam():
    a=100
    a+=50
    return a

x=spam()
print(x)


def spam1():
    b="python"
    print(b)

spam1()
'''



a=100 #Global variable

def display():
    global a
    b=10 #local variable
    print(f"the given variable is local variable {b}")

    a=a+400
    print(f"The local variabel is global varaible {a}")

display()

print("Modification for global variable (outside)")

a=a+100

print(a)

'''
the given variable is local variable 10
The local variabel is global varaible 500
Modification for global variable (outside)
600

