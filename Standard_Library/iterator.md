# Iterator
A process that is repeated more than one time by applying the same logic is called an Iteration.  
1. Iterators are lazy - save memory
2. [iterable](#iterable)  
3. [iterator](#iterator)  
4. [generator](#generator)  

## iterable  
An object capable of returning its members one at a time:
1. Sequence types:  
   + list, str, tuple, ...  
2. Non-sequence types:
   + dict, file objects, ...
   + object (class) with **\_\_iter\_\_()** or **\_\_getitem\_\_()** method  

## iterator 
### iter()
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
*One don't have to use **iter()** when using **for in** to loop over. It does it automatically*
### Custom iterator
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
## Generator
Generator - easy way of making iterator. Instead of class iterator use function with **yield**  
Reading large files  
Simple generator:  
```python
def gen():
    for i in range(10):
        yield i ** 2

for x in gen():
    print(x, end=' ')  # output: 0 1 4 9 16 25 36 49 64 81
```
## Generator expression
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
### iterators are lazy