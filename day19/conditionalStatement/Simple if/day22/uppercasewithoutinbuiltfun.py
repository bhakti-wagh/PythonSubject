#without using (isupper) to check uppercase:

x='H'

if ord('A')<=ord(x)<=ord('Z'): #  "A"<=x<="Z"
    print("uppercase data")


#without using (islower) to check lowercase:

b='h'

if ord('a')<=ord(b)<=ord('z'):  # "a"<=b<="z"
    print("lowercase data")


#given number is digit or not

c='1234546789'

if c.isdigit():
    print("it's digit")


d='7'
d
if ord('0')<=ord(d)<=ord('9'): # '0'<=d<='9'
    print(ord(d))


#wap to check the given characer is uppercase then convert to lowercase

k="DFJL"

if k.isupper():
    k=k.lower()
print(k)


#wap to check the given character is lowercase then convert to uppercase

d="good morining"

if d.islower():
    d=d.upper()
print(d)


#wap to convert upper to lower(if you want to convert then we use +32 always)
e='H'

if ord('A')<=ord(e)<=ord('Z'):
    print(chr(ord(e)+32))


#wap to convert lower-> upper(-32)

q="m"

if ord('a')<=ord(q)<=ord("z"):
    print(chr(ord(q)-32))
