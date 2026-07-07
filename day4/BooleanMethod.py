Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>> #Boolean Method --> here we have to pass only alphabet (uppercase/lowercase)
>>> 
>>> # 1. isalpha() --> here we have to pass only alphabet (uppercase/lowercase)
>>> 
>>> #--> syntax ---> variableName.isalpha()
>>> 
>>> # only lower-> true
>>> #only uppercase->true
>>> #only combination-> true
>>> #number-> false
>>> #special character->false
>>> 
>>> a="GSDJFSDHFJKDSNF"
>>> a.isaplha()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> a.isalpha()
True
>>> 
>>> b="dsjfklsdjf"
>>> b.isalpha()
True
>>> 
>>> 
>>> #2. isalnum() --> combination of aphabet +number
>>> 
#---> syntax --> variablename.isalnum()

#alphabet --> lower, upper, combination

#only number -> True
#only special character -> false
#obly alphabet+number -> true
#alphabet+ number+spl--> false

b="saldfjdslkjfdslj"
b.isalnum()
True

b="skdhfkjsadSDFKJ646548784"
b.isalnum()
True

c="jsdkfjSDDJFLKSJ654654653@##%%^&%^"
c.isalnum()
False


#3. isdigit() --> syntax ---> varaibaleName.isdigit()

# no alphabet , no special character
# isdigit() -> it will accep number that number should be present in quotes

a='123555454'
a.isdigit()
True

b="sjdlkjflks"
b.isdigit()
False


c="34.56"
c.isdigit()
False




# 4. isupper() --> syntax --> vai_name.isupper()

# it will accetp number , special character , character should be in uppercase
# number and special character is optional but character is mandatory


a="KSDJFLKSJDLKFJ45465#%$^#$^"
a.isupper()
True


# 5. islower()  --> syntax ---> var_name.islower()

#it will accept number, special character, character , but it should be in uppercase
#number and special character is optional but characters are mandatory

a="ldjflkjslfj6468761#%#$^#$^"
a.islower()
True

b = "5465422#$%#$^#"
b.islower()
False

c = "$%#$^$@%^!&"
c.islower()
False

d="DSLJFKSLDJ"
d.islower()
False

e = "
SyntaxError: unterminated string literal (detected at line 1)
54
54
e="654651321"
e.islower()
False

f="lsjdfkjk"
f.islower()
True




# istitle() --> syntax --> var_name.istitle()

s="Hi Hello"
s.istitle()
True


t = "Abc Xyz MNO"
t.istitle()
False
t="Abc Xyz MNO"
t.istitle()
False

# 6.istitle()



# 7. isspace() --> syntax --> var_Name.isspace()
#only accept empty space


s=""
s.isspace()
False

d="hi hello"
d.isspace()
False

e=" "
e.isspace()
True


s3="  Hi"
s3.isspace()
False



# 8. 0
# 8. startswith()  --> syntax --> var_Name.startswith('substring',startindex) --> startindex--> optional

w ="Python class done"

w.startswith("Python")
True

w.startswith("ytho")
False

w.startswith("class")
False

w.startswith("class",7)
True
w.startswith("ython",2)
False
w.startswith("ython",1)
True

w.startswith("hon",3)
True

w.startswith("done",13)
True



#9. endswith() --> synatx --> var_Name.endswith('substring',startindex,endindex+1)--> si,endindex -->optional

w = "Python class done"

w.endswith("done")
True

w.endswith("python",0,6)
False

#because p is in lowercase

w.endswith("Python",0,6)
True



e="walmart snapchat,instagram,dataload"
e="walmart snapchat instagram dataload"
e
'walmart snapchat instagram dataload'

e.startswith("snapchat",8)
True

e.startswith("snapchat")
False

e.endswith("snapchat")
False

e.endswith("snapchat",8,16)
True


e.endswith("dataload")
True

e.startswith("dataload",27)
True




# 10. isidentifier() ---> syntax --> "identifier_part".isidentifier()
# 11.  idkeyword() --> keyword.iskeyword("keyword")


# 12. replace() --> synatx --> var_name('oldcharacter','newcharacter',count)-->count-->optional

y="Hello"
y.replace('H','Y')
'Yello'

y.replace('h','Y')
'Hello'

y.replace('l','*',2)
'He**o'
y.replace('l','*',1)
'He*lo'


#what is drawback of replace --> we can't replcae second occurance ,we can replace both occurance or first occurance

y.replace("Hello","python")
'python'

y
'Hello'
