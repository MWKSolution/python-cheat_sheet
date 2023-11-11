# Iterator

1. [Brief](#brief)
2. [Iterable](#iterable-)
   1. Definition
   2. Custom iterable (\_\_iter__)
3. [Iterator](#iterator-)  
   1. iter(), next()
   2. iter() with sentinel
   3. Custom iterator (\_\_iter\_\_, \_\_next\_\_)
4. [Generator](#generator)  
   1. yield
   2. Generator expression  
5. [Iterators are lazy](#iterators-are-lazy-)  

---

## Brief
A process that is repeated more than one time by applying the same logic is called an Iteration.  

---

## iterable  
### Definition
An object capable of returning its members one at a time:
1. Sequence types:  (have **\_\_getitem\_\_()** and **\_\_len\_\_()** methods)
   + list, str, tuple, ...  
2. Non-sequence types:
   + dict, file objects, ...
   + object (class) with **\_\_iter\_\_()**   method 
   + generators
### Custom iterable
Object must have **\_\_iter\_\_** method
```python
class Foo(object):
    def __iter__(self):
        return (x for x in range(4))

it = iter(Foo())       # it = <generator object Foo.__iter__.<locals>.<genexpr> at 0x...>
l = list(Foo())        # l = [0, 1, 2, 3]
for i in Foo():
    print(i, end=' ')  # output: 0 1 2 3
```

---

## iterator 
### iter(), next()
Iterable passed to **iter()** function returns **iterator** 
```python
i = iter([1, 2, 3])
v = next(i)  # v = 1
v = next(i)  # v = 2
v = next(i)  # v = 3
v = next(i)  # StopIteration exception
```
One can use **for in** to loop over iterator
```python
i = iter([1, 2, 3])
for x in i:
    print(x, end=' ')  # output: 1 2 3 
```
*One don't have to use **iter()** on iterable when using **for in** to loop over. It does it automatically !!!*  
```python
i = [1, 2, 3]
for x in i:
    print(x, end=' ')  # output: 1 2 3 
```
### iter() with sentinel
Something like ***while True*** with ***break***
```python
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
```
### Custom iterator: \_\_iter\_\_(), \_\_next\_\_()
Can have **\_\_init\_\_** like other casses but must have methods:
1. **\_\_iter\_\_** - has to return self + some initialisation if **\_\_init\_\_** is omitted
2. **\_\_next\_\_** - return next item in the sequence
```python
class Count:
    """By default, counts from 0 to 10"""
    def __init__(self, start=0, stop=10):
        self.num = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.stop:
            num = self.num
            self.num += 1
            return num
        else:
            raise StopIteration
```
Usage:
```python
c = Count()
for i in c:
    print(i, end=' ')  # output: 0 1 2 3 4 5 6 7 8 9 10
```

---

## Generator
### yield 
Generator - easy way of making iterator. Instead of class iterator use function with **yield**   
Simple generator:  
```python
def gen():
    for i in range(10):
        yield i ** 2

for x in gen():
    print(x, end=' ')  # output: 0 1 4 9 16 25 36 49 64 81
```
### Generator expression
Similar to list, dict, set comprehensions but returns **generator** !!! and takes less memory but takes more time !
```python
import sys
g = (i ** 2 for i in range(10000))  # type(g) = <class 'generator'>
s = sys.getsizeof(g)                # s = 112
```
```python
import sys
l = [i ** 2 for i in range(10000)]  # type(l) = <class 'list'>
s = sys.getsizeof(l)                # s = 87616
```

---

## iterators are lazy  
Iterators providing one value at a time - it saves memory. But not time.
Good for large amount of data, reading large files or infinitely long iterables.  
