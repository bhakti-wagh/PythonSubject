
s="Hello"

'''
print(enumerate(s))#here normal way we get address of variable

#<enumerate object at 0x0000025E6A8E6AC0>
'''

# using object of typecasting
'''
print(list(enumerate(s)))#[(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
print(tuple(enumerate(s)))#((0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'))
print(set(enumerate(s)))#{(3, 'l'), (4, 'o'), (0, 'H'), (1, 'e'), (2, 'l')}
print(dict(enumerate(s)))#{0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

'''

#using looping

'''
for i in enumerate(s):
    print(i)
'''
'''
    o/p:
            (0, 'H')
            (1, 'e')
            (2, 'l')
            (3, 'l')
            (4, 'o')
'''


#if you want to print only position and value then take 2 variable
'''
 if i useing 2 variable then --> 1varaibale--> positon
                             --> 2variable-->  value
 output should be in unpacked
'''


for i,j in enumerate(s):
    print(i)#here only postion display

'''
    o/p:    0
            1
            2
            3
            4

'''

for i,j in enumerate(s):
    print(i,j)#here display both position and value ,,i-->position, j--> value

'''
    o/p:   0 H
           1 e
           2 l
           3 l
           4 o
'''

#wap to print postion and character both

k=[10,20,30,40,50]

for i in enumerate(k):
    print(i)


'''
        o/p:
            (0, 10)
            (1, 20)
            (2, 30)
            (3, 40)
            (4, 50)
'''

