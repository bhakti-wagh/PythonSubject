#wap to check the given data type is a string

#1st way
x="morning"

if type(x)==str:
    print("String data type")

#2nd way
if isinstance(x,str):
    print(f"string data type {x}")


#wap to check the given data type is sequence data type

#1way
a=eval(input("Enter the data type:"))

if type(a) in (str,list,tuple):
    print(f"{a} is sequence data type")

#2nd way

z=eval(input("Enter the data type:"))

if isinstance(z,(str,list,tuple)): #isinstance(value,(data1,data2...))
    print("Sequence data type")
