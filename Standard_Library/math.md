  
# Math and Numbers
1. Types
   1. bool
   2. int
   3. float
   4. complex
2. Operators
3. Built-in functions  
4. Other types
   1. decimal.Decimal
   2. fractions.Fraction
5. math
   1. Constants
   2. Number-theoretic and representation functions
   3. Power and logarithmic functions
   4. Trigonometric functions
   5. Angular conversion
   6. Hyperbolic functions
   7. Special functions
6. cmath

---

## Types

Root of numeric types : numbers.Number  

**object** -> int, float, comlex, decimal.Decimal, *numbers.Number*  
**int** -> bool  
***numbers.Number*** -> *numbers.Complex*, *numbers.Real*, *numbers.Rational*  
***numbers.Rational*** -> fractions.Fraction, *numbers.Integral*

### bool
```python
x, y = True, False
z = type(x)  # z = <class 'bool'>
```
Objects considered false:  
- constants defined to be false: None and False.
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '', (), [], {}, set(), range(0)

### int

There is no limit for int numbers!  
```python
x, y, z, t, m = 100, 1_000_000, 0b10101010, 0xFF, 0o234
q = type(x)  # q = <class 'int'>
```
Methods:   
**bit_lenght()**, **bit_count()**,  
**to_bytes()**, **from_bytes()**(classmethod!)   
**as_integer_ratio()**  

### float
It’s suitable in science, engineering, and computer graphics, where execution speed is more important than precision.  
!!! representation error !!!  
Stick to float or int if possible!  
Limit and overflow:  
```python
import sys
f = sys.float_info
# f = sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, 
# min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53,
# epsilon=2.220446049250313e-16, radix=2, rounds=1)
m = sys.float_info.max
# m = 1.7976931348623157e+308
x = 1.1e400    # x = inf
x = 11.1**400  # OverflowError: (34, 'Result too large')
```
```python
x, y, z, t, m = 1.1, 1_000.555_123, 1.3e6
q = type(x)  # q = <class 'float'>
m = float('inf')          # m = inf; 'INF', 'Infinity', ...
k = float('NAN')          # k = nan; 'NaN', 'nan', ...
# inf also with '-' (minus)
```
Methods:  
**as_integer_ratio()**
```python
v = (-2.0).is_integer()  # v = True
```
```python
v = (1234.5678).hex()  # v = '0x1.34a456d5cfaadp+10'
```
```python
# classmethod !
v = float.fromhex('0xf.aap10')  # v = 16040.0
# !!!!
w = float.hex(16040.0)          # w = '0x1.f540000000000p+13'

```
### complex
```python
a = 1+2j   
q = type(a)  # q = <class 'complex'>
```
```python
a = 1+2j
v = a.real         # v = 1.0
w = a.imag         # w = 2.0
z = a.conjugate()  # z = (1-2j)
```
**abs()** for complex gives magnitude (modulus - vector length) !!!
```python
w = abs(5-3j)    # w = 5.830951894845301
```

---

## Operators

[Operators...](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)

!!! @ - new operator in 3.5 - matmul(a,b) - not implemented for builtins - object has to have defined:  **\_\_matmul\_\_(), \_\_rmatmul\_\_(), and \_\_imatmul\_\_()**. numpy has it.    

---

## Built-in functions  

1. **abs(x)** - Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing **\_\_abs\_\_()**. It is magnitude for complex numbers !!!
```python
v = abs(-12.14)  # v = 12.34
w = abs(5-3j)    # w = 5.830951894845301
```
2. **divmod(a, b)** - for integers, floats: (a // b, a % b),  no complex.  
```python
v = divmod(5, 2)      # v = (2, 1)
w = divmod(5.5, 2.1)  # w = (2.0, 1.2999999999999998)
```
3. **pow(base, exp[,mod])** - base**exp operator, with mod: pow(base, exp) % mod - but more efficiently. Depemding on argument it returns integer or float or complex...
```python
v = pow(3, 4)
w = 3**4           # v = w = 81
z = pow(3, 4, 10)  # z = 10
```
4. **round(number[,ndigits])** - Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.  
```python
v = round(2.1234567)     # v = 2
w = round(2.1234567, 2)  # w = 2.12
x = round(2.1234567, 6)  # x = 2.123457
```


5. **bin(x)** - Convert an *integer* number to a binary *string* prefixed with “0b”.  
```python
v = bin(55)    # v = '0b110111'
w = bin(0xff)  # w = '0b11111111'
```
6. **hex(x)** - Convert an *integer* number to a lowercase hexadecimal *string* prefixed with “0x”
```python
v = hex(55)        # v = '0x37'
w = hex(0b110111)  # w = '0x37'
```
7. **oct(x)** - Convert an *integer* number to an octal *string* prefixed with “0o”. 
```python
v = oct(55)  # v = '0o67'
```

8. **int([x])**,  **int(x, base=10)** - Return an integer object constructed from a number or string x, or return 0 if no arguments are given. For object **\_\_index\_\_()** or **\_\_int\_\_()** must be defined.  
```python
a = int()  # a = 0
v = int(5)
w = int(5.5)
x = int('5')
y = int('0b101', base=2)
z = int('101', 2)
m = int(0b101)
n = int('    5\n\t')
# v = w = x = y = z = m = n = 5

int(101, base=2)  # TypeError: int() can't convert non-string with explicit base
int('five')       # ValueError: invalid literal for int() with base 10: 'five'
int('inf')        # ValueError: invalid literal for int() with base 10: 'inf'

class C:
    def __index__(self):
        return 1
c = C()
q = int(c)  # q = 1
```
9. **float([x])** - Return a floating point number constructed from a *number* or *string* x. For object **\_\_float\_\_()** must be defined.  
```python
q = float()               # q = 0
v = float(5)              # v = 5.0
w = float(5.5)
x = float('5.5')
n = float('    5.5\n\t')  # n = w = x = 5.5
m = float('inf')          # m = inf
k = float('NAN')          # k = nan
q = float('xxx')          # ValueError: could not convert string to float: 'xxx'

class C:
    def __float__(self):
        return 1.1
c = C()
r = float(c)  # r = 1.1
```

10. **complex([real[, imag]])** - Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number. For object **\_\_complex\_\_()** must be defined.  
```python
q = complex()            # q = 0j
w = complex(5.5)         # w = (5.5+0j)
e = complex(5.5, 3.3)    # e = (5.5+3.3j)
r = complex('5.5')       # r = (5.5+0j)
t = complex('5.5+3.3j')  # t = (5.5+3.3j)
```
11. **sum(iterable,/,start=0)** - Sums start and the items of an iterable from left to right and returns the total.
```python
x = sum(range(10), start=100)  # x = 145
```

---

## Other types

### decimal.Decimal
**For financial calculations !!!** - eliminate the binary representation error  
decimal.Decimal data type is a hybrid of decimal floating-point and fixed-point representations.  
It can represent numbers with arbitrary yet finite precision.  
Emulated in software rather than hardware, making this data type much less efficient in terms of time and space than float.  

```python
from decimal import Decimal
x = Decimal('0.1')           # x = Decimal('0.1')
y = Decimal.from_float(0.1)  # y = Decimal('0.1000000000000000055511151231257827021181583404541015625')
z = (x == y)                 # z = False
```
```python
import decimal
x = decimal.getcontext()
# x = Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, 
# capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
```

### fractions.Fraction
Infinite precision bounded only be available memory.  
Fractions are implemented in pure Python and are much slower than floating-point numbers that can run directly on your hardware. In most cases that require a lot of calculations, performance is more important than precision.
Floats and Fractions could be 
```python
from fractions import Fraction
x = Fraction(0.75)
y = Fraction(6/8)
q = Fraction(3, 4)
r = Fraction('3/4')
# = x = y = q = r = Fraction(3, 4) 
z = x.denominator  # z = 4
t = x.numerator    # t = 3
g = str(x)         # g = '3/4'
print(x)
# output: 3/4
```
Methods:
**as_integer_ratio()**  
**from_float()**, **from_decimal()** - *classmethods*  
**\_\_floor\_\_(), \_\_ceil\_\_(), \_\_round\_\_()** - from math module
```python
from fractions import Fraction
x = Fraction('3.1415926535897932').limit_denominator(1000)
# x = Fraction(355, 113)
```

---

## math
!!! Not for complex numbers !!!  
Use for floats over built-in functions !  
### Constants
```python
import math
math.pi
math.tau
x = (2*math.pi == math.tau)  # x = True
math.e
math.inf
y = float('inf') == math.inf  # y = True
math.nan
z = (float('nan') == math.nan)  # z = False !!!!
# use isnan() !!!!!!!
t = math.isnan(float('nan'))  # t = True
```
### Number-theoretic and representation functions
**ceil()**  
comb()  
copysign()  
fabs()  
factorial()  
**floor()**  
fmod()  
frexp()  
**fsum()** - more acurate than sum !  
**gcd()** - greatest common divisor  
**isclose()**  
**isfinite()**  
**isinf()**  
**isnan()**  
isqr() - least common muliple - 3.9!  
ldexp()  
modf()  
nextafter() - 3.9  
perm()  
prod()  
reminder()  
**trunc()**  
ulp() - 3.9  
### Power and logarithmic functions
**exp()**  
expm1()  
**log()**  
log1p()  
**log2()**  
**log10()**  
**pow()**  - !!! faster than built-in ** or pow() but doesn't work with complex !
**sqrt()**    
### Trigonometric functions
acos()  
asin()  
atan()  
atan2()  
cos()  
dist() -  Euclidean distance between two points p and q, each given as a sequence.  
hypot() - Euclidean norm  
sin()  
tan()
### Angular conversion
**degrees()**  
**radians()**  
### Hyperbolic functions
acosh()  
asinh()  
atanh()  
cosh()  
sinh()  
tanh()  
### Special functions
erf()  
erfc()  
gamma()  
lgamma()  

[All functions documentation...](https://docs.python.org/3/library/math.html)

---

## cmath
Define **\_\_complex\_\_()** for making complex number out of object.  
### Constants
```python
import cmath
cmath.pi
cmath.e
cmath.tau
cmath.inf
cmath.nan
#
x = cmath.nanj               # x = nanj
y = complex(0.0, cmath.nan)  # y = nanj
z = cmath.isnan(y)           # z = True
m = cmath.infj               # m = infj
t = complex(0.0, cmath.inf)  # t = infj
u = (m == t)                 # u = True

```
### Conversions to and from polar coordinates
```python
import math
import cmath
z = 3+2j
x = cmath.polar(z)
modulus = x[0]                   # modulus = 3.6...
phase = x[1]                     # phase = 0.588...
phase_deg = math.degrees(phase)  # phase_deg = 33.69... 
phase = cmath.phase(z)           # phase = 0.588...
modulus = abs(z)                 # modulus = 3.6...
y = cmath.rect(modulus, phase)   # y = (3+1.9999999999999996j)
``` 
```python
import cmath

a = 3 + 2j
g = complex(3, 2)
radius, angle = cmath.polar(a)
t = radius * (cmath.cos(angle) + 1j*cmath.sin(angle))
e = radius * cmath.exp(1j*angle)
# a = g = t = e; (3+1.9999999999999996j) ! 
```
Use isclose for cmp !!!  
### Power and logarithmic functions
exp()  
log()  
log10()  
sqrt()  
### Trigonometric functions
acos()  
asin()  
atan()  
cos()  
sin()  
tan()  
### Hyperbolic functions
acosh()  
asinh()  
atanh()  
cosh()  
sinh()  
tanh()  
### Classification functions
isfinite()  
isinf()  
isnan()  
isclose()

---
