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


Uiversal newlines:
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
Raw string treats the backslashes (\) as literal characters.  
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
path = 'c:\user\task\new'  # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
```
correct:  
```python
path = r'c:\user\task\new'
# or
path = 'c:\\user\\task\\new'
```
Be careful with '\' at the end !!!
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
t = """ąĄĆć
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
casefold()  
### Search and replace
count()  
endswith()  
find()  
index()  
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
isspace()  
istitle()  
isupper()  
### Formatting
center()  
expandtabs()  
ljust()  
lstrip()  
rjust()  
rstrip()  
strip()  
zfill()  
### Conversion
join()  
partition()  
rpartition()  
rsplit()  
split()  
splitlines()  

translate()  
maketrans()  
format_map()  
encode()  ---- !!!!!!!!!!

---

## f-strings
### Formatting
Other (older) methods of string formatting:
- str.format()
- %-formatting
- string.Template

f-strings are faster !!!,  
can be multiline, nested  
can't be empty, can't contain '\'

general format:
```python
print(f'{expression!conversion:format}')
```
### expression
variable, object, expression

###conversion
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
class Formatter - > str.format  
class Template

capwords()

---