#1.WAP to return a dictionary with word & its len pair
#from a string

#exp o/p : {hello:5, guys:4, morning:7, how:3, are:3, you:4}
#string = 'hello good morning how are youu'
'''
d={}

for i in string.split():

    d[i]=len(i) #Without using inbuilt method
    #d.update({i:len(i)})#Using inbuilt mehtod
print(d)

''' 

    




#2.WAP to count number of vowels present in given string
'''
s = 'GooD mOrnIng'
count=0

for i in s:

    if i in 'aeiouAEIOU':

        count+=1
print(count)
        
'''


#3.WAP to get below o/p:
s = 'Hi how are you'
#exp o/p : 'iH woh era uoy
'''
#res=''

for i in s.split():

    print(i[::-1],end=" ")
    #res=res+" "+i[::-1]
''' 




#4.WAP to print all the digits in a below list
'''
l = ['hello', '123', 'hai', 'python', '345']

for i in l:

     if i.isdigit():

         print(i)


'''



#6.Find the sum of even numbers from 1 to 20
'''
sum_E=0
for i in range(1,21):

    #print(i)

    if i%2==0:
        
        sum_E=sum_E+i
        
print(sum_E)
        
'''


#7.Count numbers divisible by 3 from 1 to 50
'''
count=0
for i in range(1,51):

    if i%3==0:
        count+=1
print(count)
'''    

#8.Replace negative numbers with 0
'''
numbers = [10, -5, 20, -3, 40]

for i in range(len(numbers)):

    if numbers[i]<0:

        numbers[i]=0

print(numbers)

'''    

#9.Print position of each character
#word = "PYTHON"
'''
1 P
2 Y
3 T
4 H
5 O
6 N
'''

'''
for i in enumerate(word,start=1):
    print(i)


'''  

#10.Count even and odd numbers in a list.
'''
num= [10, 15, 22, 31, 40, 51]

even_count=0
odd_count=0

for i in num:

    if i%2==0:

        even_count+=1

    else:
        odd_count+=1

print(even_count)
print(odd_count)
'''

#11.wap to print repeated char and count the same
'''
s="helloworld"
rep=''

for i in s:

    if s.count(i)>1 and i not in rep:

        print(i,"-->",s.count(i))
        rep=rep+i
        
print(rep)
'''


#12.Grouping flowers and animals separately
'''
items=["lotus-flower","lilly-flower","cat-animal","dog-animal","sunflower-flower"]

flower=[]
animal=[]

for i in items:

    if i.endswith('flower'):
        flower.append(i)
    else:
        animal.append(i)

        
print(flower)
print(animal)

  '''


#13.filter only character except digits
'''
s="Think456 and 123answers it789 guys "

result=""

for i in s:

    if not i.isdigit():
        
        result=result+i
        
print(result)

'''




#14.replace whitespaces with newline char in the below string
'''
s="hello world welcome to python"
for i in s:
    if i==" ":
        s=s.replace(i,"\n")
print(s)
'''

#15.replace all vowels with *
'''
s="hello world welcome to python"

for i in s:

    if i in 'AEIOUaeiou':
        s=s.replace(i,'*')
print(s)

'''


#5.WAP to check whether string is ANAGRAM or not

#anagrams : characters should be same it can different meaning
#tea, eat
#silent, listen
#bored , robed
#cat, act
#keep, peek
#lamp, palm


a="tea"
b="eat"

if sorted(a)==sorted(b):
    print("Its anagram")
else:
    print("Its not anagram")




