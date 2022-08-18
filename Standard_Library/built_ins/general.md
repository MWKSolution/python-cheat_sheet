# General functions
   1. len()
   2. max(), min()
   3. slice()

---

## len()
Return the length (the number of items) of an object.  
```python
v = len('abcd')     # v = 4
l = [1, 2, 3]       
w = len(l)          # w = 3
z = len(range(10))  # z = 10
q = l[-1]           # q = 3
# more pythonic than:
r = l[len(l)-1]     # r = 3
```
Can't use len on iterators and generators !!!! and some types...
```python
n = len(reversed(l))  # TypeError: object of type 'list_reverseiterator' has no len()
m = len(10)           # TypeError: object of type 'int' has no len()
```
With custom objects **\_\_len\_\_** must be defined.  
```python
class L:
    def __len__(self):
        return 10

l = L()
v = len(l)  # v = 10
```

---

## max(), min()
Return the largest/smallest item in an iterable or the largest of two or more arguments.  
!!! You can’t call min() or max() with an iterable of noncomparable types as an argument !!! - TypeError  
```python
l = [3, 5, 9, 1, -5]
v = max(l)                    # v = 9
w = min(3, 5, 9, 1, -5)       # w = -5
x = max("abcdefghijklmnopqrstuvwxyz")  # x = 'z'
y = min(["Hello", "Pythonista", "and", "welcome", "world"])  # y = 'Hello'
r = min(1, 'a', 3, 'c')       # TypeError: '<' not supported between instances of 'str' and 'int'
z = max([])                   # ValueError: max() arg is an empty sequence
q = max([], default='empty')  # q = 'empty'   
```
can be used with comprehensions and generators
```python
lower = 0
numbers = [42, -78, 200, -230, 25, 142]
v = [max(number, lower) for number in numbers]  # v = [42, 0, 200, 0, 25, 142]
```
With key keyword:
```python
prices = {"banana"   : 1.20,
          "pineapple": 0.89,
          "apple"    : 1.57,
          "grape"    : 2.45}

v = min(prices.items(), key=lambda item: item[1])  # v = ('pineapple', 0.89)

w = max(["20", "3", "35", "7"], key=int)           # w = "35"
```
You can also make instances of your custom classes compatible with **min()** and **max()**.   
To achieve this, you need to provide your own implementations of **\_\_lt\_\_()**, **\_\_le\_\_()**, **\_\_gt\_\_()**, or **\_\_ge\_\_()** and **\_\_eq\_\_()**.
To make it easier use **functools.total_ordering**
```python
from functools import total_ordering

@total_ordering
class StrangeNumber:
    def __init__(self, number):
        self.number = number
    def __repr__(self):
        return f'{type(self).__name__}({self.number})'
    def __lt__(self, other):
        return self.strange(self.number) < self.strange(other.number)
    def __eq__(self, other):
        return self.strange(self.number) == self.strange(other.number)
    @classmethod
    def strange(cls, n):
        return float("".join(reversed(str(n))))

x = StrangeNumber(12345.56)    # x = StrangeNumber(12345.56)
y = StrangeNumber(13.3333333)  # y = StrangeNumber(13.3333333)
z = (x >= y)                   # z = False
k = max(x, y)                  # k = StrangeNumber(13.3333333)
```

---

## slice()
Return a slice object representing the set of indices specified by range(start, stop, step).  
Slice objects are also generated when extended indexing syntax is used:  
```python
s = 'abcdefgh'
x = slice(2, 5, 2)
v = (s[x] == s[2:5:2])  # v = True 
y = s[x]                # y = 'ce'
```