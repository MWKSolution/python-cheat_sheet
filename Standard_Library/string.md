# String
1. General
   1. Indexing and slicing
   2. String is a sequence
   3. Reversing
   4. Sorting
   5. Operators
2. Escape characters and raw strings
   1. Escape characters
   2. Raw strings
3. Built-in functions
   1. ascii()
   2. chr()
   3. format()
   4. input()
   5. ord()
   6. print()
   7. str()
4. Methods
   1. Case conversion
   2. Search and replace
   3. Classification
   4. Formatting
   5. Conversion
   6. Mappings
5. f-strings
   1. Formatting
   2. expression
   3. conversion
   4. format
6. string module
7. io.StringIO

---

## General
**Strings is immutable!!!**  
### Indexing and slicing:
```python
s = 'abcdefgh'
t = type(s)    # t = <class 'str'>
a = s[1]       # a = 'b'
b = s[-2]      # b = 'g'
c = len(s)     # c = 8
d = s[1:-2:2]  # d = 'bdf'
```
### String is sequence:
```python
l = list('abcdefg')         # l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
m = [i for i in 'abcdefg']  # m = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# see str.split()
```
### Reversing:
```python
s = 'abcdefgh'
r = s[::-1]  
r = ''.join(reversed(s))  # r = 'hgfedcba'
```
### Sorting:
```python
s = 'tbyjdfasertgert'
r = ''.join(sorted(s, reverse=True))  # r = 'ytttsrrjgfeedba'
```

### Operators
```python
# +
a, b = '123', 'abc'
c = a + b   # c = '123abc'  
# see str.join()
# *
a = 'a'
b = a * 10  # b = 'aaaaaaaaaa'
# in
a = ('bc' in 'abcd')   # a = True
```
## Escape characters and raw strings
### Escape characters
Escape sequences:
```
\<newline>  Backslash and newline ignored
\\          Backslash (\)
\'          Single quote (')
\"          Double quote (")
\a          ASCII Bell (BEL)
\b          ASCII Backspace (BS)
\f          ASCII Formfeed (FF)
\n          ASCII Linefeed (LF)
\r          ASCII Carriage Return (CR)
\t          ASCII Horizontal Tab (TAB)
\v          ASCII Vertical Tab (VT)
\ooo        Character with octal value ooo
\xhh        Character with hex value hh
```
Escape sequences only recognized in string literals:
```
\N{name}    Character named name in the Unicode database
\uxxxx      Character with 16-bit hex value xxxx
\Uxxxxxxxx  Character with 32-bit hex value xxxxxxxx
```

[Unicode codes and characters...](https://en.wikipedia.org/wiki/List_of_Unicode_character)


Universal newlines:
```
\n          Line Feed                     Unix
\r          Carriage Return               Macintosh
\r\n        Carriage Return + Line Feed   Windows
\v or \x0b  Line Tabulation
\f or \x0c  Form Feed
\x1c        File Separator
\x1d        Group Separator
\x1e        Record Separator
\x85        Next Line (C1 Control Code)
\u2028      Line Separator
\u2029      Paragraph Separator
```
```python
import string
h = string.whitespace
# h = ' \t\n\r\x0b\x0c'
```

### Raw strings
Raw string treats the backslashes &bsol; as literal characters.  
Unless an ‘r’ or ‘R’ prefix is present, escape sequences in strings are interpreted according to rules given above.    
```python
s = 'abc\tdef\nghi'   # s = 'abc\tdef\nghi'
print(s)
#output:
# abc	def
# ghi
s = r'abc\tdef\nghi'  # s = 'abc\\tdef\\nghi'
print(s)
#output
# abc\tdef\nghi
```
```python
s1 = r'abc\tdef\nghi' 
s2 = 'abc\\tdef\\nghi'
a = s1 == s2  # a = True
b = s1 is s2  # b = True
```
```python
a = len('\n')   # a = 1
b = len(r'\n')  # b = 2
```
A raw string cannot end with an odd number of backslashes !!!  
```python
s = r'\\\'  # SyntaxError: EOL while scanning string literal
```
Used for low level Windows path handling:
```python
path = 'c:\user\task\new'  
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
```
correct:  
```python
path = r'c:\user\task\new'
# or
path = 'c:\\user\\task\\new'
```
Be careful with &bsol; at the end !!!  
Raw strings with repr():
```python
s = 'abc\tdef\nghi' 
v = repr(s)  # v = "'abc\\tdef\\nghi'"
```

See also f-strings for **f'**_string_**'** and bytes for **b'**_string_**'**

---

## Built-in functions

### ascii()
Returns only ascii characters. Escaping others.  
```python
t = """ 
Ńńżź"""
s = ascii(t)  # s = "'\\u0105\\u0104\\u0106\\u0107\\n\\u0143\\u0144\\u017c\\u017a'"
print(s)
# output: '\u0105\u0104\u0106\u0107\n\u0143\u0144\u017c\u017a'
q = ascii('∰')  # q = "'\\u2230'"
w = ascii('a')   # w = "'a'"
```
### chr()
Function returns a string from a Unicode code intege.  
```python
a = chr(65)       # a = 'A'
b = chr(0x104)    # b = 'Ą'
c = chr(0x2230)   # c = '∰'
```
### format()
See f-strings...  
### input()  
reads line from input, converts it into string.  
```python
s = input('>')
#> 46
# s = '46'
```
### ord()
Returns the Unicode code from a given character.  
```python
a = ord('A')  # a = 65
b = ord('Ą')  # b = 260  '0x104'
c = ord('€')  # c = 8364 '0x20ac'
```
### print()  
Print objects to the text stream file, separated by sep and followed by end. All non-keyword arguments are converted to strings.  
```python
print()  # prints 'end' be default \n
print(1, 2, 3, 4)  # 1 2 3 4\n
print(1, 2, 3, 4, sep=',', end='...')  # 1,2,3,4...
```
file keyword:
```python
import sys
print()
# is equivalent
print(file=sys.stdout)
```
```python
with open('text.txt', 'w') as f:
    print('test...', file=f)
# text.txt: test...
```
flush keyword:  
Flushes buffered output.  
### str()  
Returns a string representation of an object. ->  **\_\_str()\_\_**  
```python
a = str()    # a = ''
b = str(12)  # b = '12'
```
For bytes:
```python
s = 'ĄĄĄĄ'
a = s.encode('utf-8')
# !! or !!
a = bytes('ĄĄĄĄ', encoding='utf-8')  # a = b'\xc4\x84\xc4\x84\xc4\x84\xc4\x84'
b = str(a)                           # b = "b'\\xc4\\x84\\xc4\\x84\\xc4\\x84\\xc4\\x84'"
c = str(a, encoding='utf-8')         # c = 'ĄĄĄĄ'
d = str(a, encoding='ascii', errors='ignore')  # d = ''
# !! or !!
e = a.decode('utf-8')                # e = 'ĄĄĄĄ'
```

---

## Methods
### Case conversion
capitalize()  
lower()  
swapcase()  
title()  
upper()  
casefold() - more aggressibe than lower()  
### Search and replace
**count()**  
```python
s = 'ababababababababababa'
v = s.count('ab')          # v = 10 
v = s.count('ab', 10, -2)  # v = 4
```
endswith()  
find()  - return index, if want to check only use 'in'  
index()  - Like find(), but raise ValueError when the substring is not found.  
rfind()  
rindex()  
replace()  
startswith()  
### Classification
isalnum()  
isalfa()  
isdigit()  
isidentifier()  
islower()  
isprintable()  
isspace()  - whitespace
istitle()  
isupper()  
### Formatting
format()  
format_map()  
center()  
**expandtabs()**  
```python
s = '1\t2\t3'
v = s.expandtabs(4)  # v = '1   2   3'
```
ljust()  
lstrip()  
rjust()  
rstrip()  
**strip()**  
```python
s = '   abc   '
v = s.strip()  # v = 'abc'
s = '# .............. abceef #. qwert........#.'
v = s.strip('# .')  # v = 'abceef #. qwert'
```
**zfill()**  
```python
v = '34'.zfill(5)   # v = '00034'
v = '-34'.zfill(5)  # v = '-0034'
```
removeprefix() - 3.9  
removesuffix() - 3.9
### Conversion
**join()**  
Return a string which is the concatenation of the strings in iterable.  
```python
l = ['a', 'b', 'c']
j = '_'
s = j.join(l)  # s = 'a_b_c'
```
**partition()**  
Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.
```python
s = 'asd asd d asda XXX dfgg d dfgd XXX df XXX'
v = s.partition('XXX')  # v = ('asd asd d asda ', 'XXX', ' dfgg d dfgd XXX df XXX')
```
rpartition()  - from right side  
rsplit()   - from right side  
**split()**  
Return a list of the words in the string, using sep as the delimiter string.  
```python
s = 'ab cd ef'
v = s.split()  # v = ['ab', 'cd', 'ef']
s = 'ab<>cd<>ef<>gh'
v = s.split('<>', maxsplit=2)  # v = ['ab', 'cd', 'ef<>gh']
```
**splitlines()**  
Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.  
See list of universal newlines.  
```python
s = 'ab c\n\nde fg\rkl\r\n'
v = s.splitlines()  # v = ['ab c', '', 'de fg', 'kl']
v = s.splitlines(keepend=True)  # v = ['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```
**encode()**  
Return an encoded version of the string as a bytes object. Default encoding is 'utf-8'.  
```python
s = 'ąćźabc'
b = s.encode(encoding='utf-8')  # b = b'\xc4\x85\xc4\x87\xc5\xbaabc'
b = s.encode(encoding='ascii')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)
b = s.encode(encoding='ascii', errors='replace')  # b = b'???abc'
```
Possible *errors* keyword:  
strict, ignore, replace,xmlcharrefreplace, backslashreplace, namereplace  
[Standard encodings](https://docs.python.org/3/library/codecs.html#standard-encodings)

### Mappings
translate()  
maketrans()

---

## f-strings
### Formatting
Other (older) methods of string formatting:
- str.format()
- %-formatting
- string.Template

f-strings are faster !!!,  
Can be multiline and nested.    
Can't be empty, can't contain &bsol;.  

general format:
```python
print(f'{expression!conversion:format}')
```
### expression
variable, object, expression

### conversion
```
!s - str() - default
!r - repr()
!a - ascii()
```
### format
```
:[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]
```
[format specification...](https://docs.python.org/3/library/string.html#formatspec)

---

## string module
Constants:  
```python
import string
a = string.ascii_letters
# a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ; lowercase + uppercase
b = string.ascii_lowercase
# b = 'abcdefghijklmnopqrstuvwxyz'
c = string.ascii_uppercase
# c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = string.digits
# d = '0123456789'
e = string.hexdigits
# e = '0123456789abcdefABCDEF'
f = string.octdigits
# f = '01234567'
g = string.punctuation
# g = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
h = string.whitespace
# h = ' \t\n\r\x0b\x0c'; \x0b - \v - line tabulation; \x0c - \f - form feed
i = string.printable
# i = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# digits + ascii_letters + punctuation + whitespace
```
And...  
- class Formatter - > str.format  
- class Template
- capwords()

---

## io.StringIO

**StringIO**(*initial_value=''*, *newline='\n'*)  
A text stream using an in-memory text buffer.  
Methods:  
'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'getvalue', 'isatty', 'line_buffering', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'  

**getvalue()** - returns entire buffer - string. 

---
