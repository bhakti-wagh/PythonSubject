Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import codecs

codecs.lookup("utf-8")
<codecs.CodecInfo object for encoding utf-8 at 0x2a6feea5730>

codecs.lookup("cp1252")
<codecs.CodecInfo object for encoding cp1252 at 0x2a6feea58b0>


import encodings
import pkgutil

for codec in sorted(m.name for m in pkgutil.iter_modules(encodings._path_)): print(codec)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for codec in sorted(m.name for m in pkgutil.iter_modules(encodings._path_)): print(codec)
AttributeError: module 'encodings' has no attribute '_path_'. Did you mean: '__path__'?



>>> import encodings
... import pkgutil
... 
... for codec in sorted(m.name for m in pkgutil.iter_modules(encodings.__path__)):
...     print(codec)
...     
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import encodings
>>> import pkgutil
>>> 
>>> for codec in sorted(m.name for m in pkgutil.iter_modules(encodings.__path__)):
...     print(codec)
...     c
... 
...     
aliases
Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    c
NameError: name 'c' is not defined

>>> 


texts = [
    "A",
    "é",
    "€",
    "न",
    "😊"
]

for text in texts:
    print(f"\nCharacter: {text}")
    print("UTF-8 :", len(text.encode("utf-8")), text.encode("utf-8"))
    print("UTF-16:", len(text.encode("utf-16")), text.encode("utf-16"))
    print("UTF-32:", len(text.encode("utf-32")), text.encode("utf-32"))

    

Character: A
UTF-8 : 1 b'A'
UTF-16: 4 b'\xff\xfeA\x00'
UTF-32: 8 b'\xff\xfe\x00\x00A\x00\x00\x00'

Character: é
UTF-8 : 2 b'\xc3\xa9'
UTF-16: 4 b'\xff\xfe\xe9\x00'
UTF-32: 8 b'\xff\xfe\x00\x00\xe9\x00\x00\x00'

Character: €
UTF-8 : 3 b'\xe2\x82\xac'
UTF-16: 4 b'\xff\xfe\xac '
UTF-32: 8 b'\xff\xfe\x00\x00\xac \x00\x00'

Character: न
UTF-8 : 3 b'\xe0\xa4\xa8'
UTF-16: 4 b'\xff\xfe(\t'
UTF-32: 8 b'\xff\xfe\x00\x00(\t\x00\x00'

Character: 😊
UTF-8 : 4 b'\xf0\x9f\x98\x8a'
UTF-16: 6 b'\xff\xfe=\xd8\n\xde'
UTF-32: 8 b'\xff\xfe\x00\x00\n\xf6\x01\x00'
Character: 😊
SyntaxError: invalid character '😊' (U+1F60A)



print(ord('A'))
65

print(ord('é'))
233

print(ord('€'))
8364

print(ord('न'))
2344

print(ord('😊'))
128522


print(char(233))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(char(233))
NameError: name 'char' is not defined. Did you mean: 'chr'?
print(chr(233))
é

print(chr(8798))
≞

print(chr(2344))
न

print(chr(128522))
😊
print(chr(128526))
😎
print(chr(128556))
😬

print(chr(2335))
ट
print(chr(2320))
ऐ
print(chr(2310))
आ
print(chr(2301))
ࣽ
print(chr(2305))
ँ
print(chr(2304))
ऀ
print(chr(2308))
ऄ
print(chr(2307))
ः
