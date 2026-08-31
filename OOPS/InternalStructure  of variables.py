'''
#1st example:
class Job:

    empName="John"
    sal=50000
    dept="HR"

j=Job()
j1=Job()

#1st point:
Job.dept="Database"
print(Job.dept) #Database
print(j.dept) #Database
print(j1.dept)#Database

#2nd point;

j1.sal=2000
print(Job.sal)#50000
print(j.sal)#50000
print(j1.sal)#2000

#3rd point:
Job.sal='10K'
print(Job.sal)#10k
print(j.sal)#10k
print(j1.sal)#2000 #because in here previous modification will not effected

#but j1 have another parameter so we can modifiy
Job.empName="Alice"
print(Job.empName) #Alice
print(j.empName) #Alice
print(j1.empName)#Alice

'''







