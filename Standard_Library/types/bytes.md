# Binary

bytes is a immutable sequence of small integers in the range 0 to 255.   
bytesarray is mutable sequence of small integers in the range 0 to 255.

## Defining bytes
```python
a = b'dfsdfsdfs'  # a = b'dfsdfsdfs'
t = type(a)       # t = <class 'bytes'>
b = a[1]          # b = 102 -> it a sequense of smallint !
c = chr(b)        # c = 'f'

d = bytes('abcdżźć', encoding='utf-8')
# or
d = ('abcdżźć').encode('utf-8')  # definning using str method !!!
# d = b'abcd\xc5\xbc\xc5\xba\xc4\x87'
g = bytes('abcdżźć', encoding='ascii', errors='namereplace')
# g = b'abcd\\N{LATIN SMALL LETTER Z WITH DOT ABOVE}\\N{LATIN SMALL LETTER Z WITH ACUTE}\\N{LATIN SMALL LETTER C WITH ACUTE}'

e = bytes(10)
# e = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
l = [97, 98, 99]
f = bytes(l)  # f = b'abc',   only from integers!
```
Possible errors keyword:
strict, ignore, replace,xmlcharrefreplace, backslashreplace, namereplace
## Defining bytesarray

## operations, operators (bytes, bytesarray)
Like for strings  
bytesarray is mutable !!!

## Methods (bytes, bytesarray)
### fromhex(), hex()
fromhex() is a classmethod!!!
```python
b = bytes.fromhex('aa684682c1f2')  
# b = b'\xaahF\x82\xc1\xf2' , \x.. notation only for non ascii 
c = b.hex()        # c = 'aa684682c1f2'
d = b.hex('|')     # d = 'aa|68|46|82|c1|f2'
e = b.hex('.', 2)  # e = 'aa68.4682.c1f2'
```

### decode()
```python

```

Like for strings, but there is subset of string methods.  
### Case conversion
capitalize(), lower(), swapcase(), title(), upper()  
### Search and replace
count(), endswith(), find(), index(), rfind(), rindex(), replace(), startswith()  
### Classification
isalnum(), isalfa(), isdigit(), islower(), isspace(), isupper()  
### Formatting
center(), expandtabs(), ljust(), lstrip(), rjust(), rstrip(), strip(), zfill(), removeprefix() - 3.9, removesuffix() - 3.9  
### Conversion
join(), partition(), rpartition(), rsplit(), split(), splitlines()  
!!! there is na ~~encode()~~ !!! - ther is **decode()** !!!

### Mappings
translate()
maketrans()


## memoryview
memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying. The memoryview() function allows direct read and write access to an object’s byte-oriented data without needing to copy it first. That can yield large performance gains when operating on large objects since it doesn’t create a copy when slicing.  
By using buffer protocol we can work on large data like we want to work on binary data of an image. Buffer protocol, can create another object access to modify the large data without copying it. This makes the program use less memory and increases the execution speed.  

---
