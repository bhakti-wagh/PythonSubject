
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
