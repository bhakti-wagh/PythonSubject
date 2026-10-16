#1-->WAP TO FIND SQUARE OF ALL THE VALUES PRESENT
#BETWEEN THE RANGE(1 TO 5).

'''
def sqr(num):

    return num*num

a=[1,2,3,4,5]
res=map(sqr,a)

print(list(res))
'''
#o/p: [1, 4, 9, 16, 25]
'''
res1=map(sqr,range(1,6))
print(list(res1))
'''


#2-->WAP TO FIND LENGTH OF EACH AND EVERY WORD PRESENT
#INSIDE THE GIVEN STRING.
'''
def findlen(word):

    return len(word)

a=['abc','defg','apple','adffhk']

res=map(findlen,a)
print(list(res))
'''
#o/p:[3, 4, 5, 6]



#3-->WAP TO GET THE FOLLOWING O/P:
#I/P='GOOD MORNING'
#O/P={'GOOD':4,'MORNING':7}
'''
def fun(word):
   

    return (word,len(word))

s='GOOD MORNING'
res=dict(map(fun,s.split()))
print(res)
    
'''

#4-->WAP TO FIND FACTORIAL OF ALL THE
#NUMBERS PRESENT INSIDE THE GIVEN
#HOMOGENOUS LIST COLLECTION.

'''
def fact(num):

    fact=1

    for i in range(1,num+1):
        fact=fact*i

    return fact   
        
a=[4,2]

res=map(fact,a)
print(list(res))

#o/p:[24, 2]

'''
#5-->WAP TO GET THE FOLLOWING O/P
#I/P='PYTHON IS EASY'
#O/P={'PYTHON':'python', 'IS':'is', 'EASY':'easy'}

'''
def lower(word):

    return (word,word.lower())


w='PYTHON IS EASY'

res=map(lower,w.split())

print(dict(res))

'''

#6-->wap to return if the key is individual returns its value else return its type
#d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}

'''
d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}

def fun(w):

    if isinstance(w,(int,float,bool)):
        return d[w]

    else:
        return type(w)


res=map(fun,d)
print(list(res))
'''

#o/p:['ten', <class 'str'>, <class 'tuple'>, 'decimal']


#7-->wap to create a list of 1st characters from each name
'''
names=["manu","lohit","jivago","wank","yaseen"]

def fun(w):

    return w[0]

res=map(fun,names)
print(list(res))
'''
#o/p:['m', 'l', 'j', 'w', 'y']


#8-->wap to return list of name and length pair

names1=["laptop","mouse","board","house","week"]

def fun(n):

    return (n,len(n))


res=map(fun,names1)
print(list(res))

#o/p:[('laptop', 6), ('mouse', 5), ('board', 5), ('house', 5), ('week', 4)]


#9-->wap to print sum of indices from both list
'''
l1=[2,3,4,5,6]
l2=[3,4,5,8,9]


def fun(x,y):
    return x+y

res=map(fun,l1,l2)
print(list(res))
'''
#o/p:[5, 7, 9, 13, 15]


#10-->wap to make a pair of names and age

names=["a","b","c","d"]
age=[20,35,21,56]

def pair(n,a):

    return(n,a)

res=map(pair,names,age)
print(dict(res))

#o/p:{'a': 20, 'b': 35, 'c': 21, 'd': 56}




    


