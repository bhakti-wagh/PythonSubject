#Collection Group

'''
a="Morning"

for i in a:    #for i in 'Morning': 
   # print(i) # it will display in column

    #print(i,end='') #it will display in single line

    # print(i,end='*') # if we want to display in between space,coma
'''
'''

print() #if we want to go for next line then take empty print() function


b=[10,20,30,40]

for k in b:
    print(k,end=" ")

print()

'''

#d={12:90,100:45,50:"abc"}

'''
for i in d:
    print(i,end=' ') #-> here key will display

'''
'''
    if we want to display only values then

    #syntax: varname[key]

    
'''

'''
for i in d:
    print(d[i]) #here d contain group of dict and i -will be start point and hole
                # keys


print()
'''



'''
    if we want to display both key and layer then

    using inbuilt function how to print:key and values(both)

    #syntax: varname.keys()
             varname.values()
             varname.items()

'''
'''

d={12:90,100:45,50:"abc"}

for i in d.keys():
    print(i)


print()

for i in d.values():
    print(i)

print()

for i in d.items():
    print(i)


'''


d=[1,2,3,4,5,6,7,8,9,10]

for i in d:

    if i%2==0:
        print("Even number :",i)


    



