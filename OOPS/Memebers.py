#OOPS

# MEMBERS INSIDE THE CLASS

#1. Variable:

class Student: #ClassName--->Student

    name="bhakit" #ClassVariable--> Name,age,total_sub
    age=23
    total_sub=5

s=Student()#object_creation

'''
print(name)
print(age)
print(total_sub)

# we can't access class data outside it will show "NameError"
'''
'''
How to Access class Data/variable outside
-------------------------------------------

Here we have Two ways:
1.By using ClassName
2.By using object

'''

#1. By using ClassName

print(f"Student Name is:{Student.name}")
print(f"Student Age:{Student.age}")
print(f"Student Total Subject:{Student.total_sub}")

'''
o/p: Student Name is:bhakit
Student Age:23
Student Total Subject:5
'''

#2.By using object
print(f"Student Name is:{s.name}")
print(f"Student Age:{s.age}")
print(f"Student Total Subject:{s.total_sub}")

'''
o/p: Student Name is:bhakit
Student Age:23
Student Total Subject:5

'''



#In class :Inside the class whatever the data stored internally in form of : dictionary{key:value}


#If you want to check how the data is stored in internally:

#print(ClassName.__dict__)


print(Student.__dict__)


#docstring:-> description of the clas
#how to print doc or title of class
#:-> print(classname.__doc__)

#If you want to complete information of the class
#:-> help(className)
help(Student)








