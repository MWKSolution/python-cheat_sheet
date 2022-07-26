# Tuple 
1. [Brief]()
2. [Defining tuple]()
3. [Accessing elements]()
4. [Methods on tuples]()
   1. in, not in
   2. \+ operator
   3. len()
   4. index()
   5. count()
5. [Operations on tuples]()
   1. Tuple packing/unpacking
   2. Slicing a tuple.
   3. Reversing
   4. Sorting
   5. Copying
   6. Swapping values with tuple
   7. Counting
   8. Merging
   
---

## Brief 
1. Tuple is immutable
2. Program execution is faster when manipulating a tuple than it is for the equivalent list.
3. Use tuple if data is not to be modified

---

## Defining tuple  
Directly:  
```python
t = (1, 2, 3)  # t = (1, 2, 3)
```
From iterable:
```python
t = tuple([1, 2])  # t = (1, 2)
```
Tuple packing:  
```python
t = 1, 2  # t = (1, 2)
```
Empty tuple:  
```python
t = ()
```
One item tuple (comma is necessary):  
```python
t = 1,    # <class 'tuple'>
t = (1,)  # <class 'tuple'>
t = (1)   # <class 'int'> !!!
``` 
Tuple can have heterogeneous items:  
```python
t = ('Hey', (1, 2), 1, ['you', 'me'])
```

---

## Accessing elements
```python
t = ("hey", "there!", "how", "are", "you?")
v = t[0]           # v = "hey"
v = t[len(t) - 1]  # v = "you?"
v = t[-1]          # v = "you?"
```
**Tuples are immutable**    
**We cannot change tuple contents!!!**
```python
t = (1, 2, 3)
t[0] = 100  # Gives error: TypeError: 'tuple' object does not support item assignment
del t[0]    # Gives error: TypeError: 'tuple' object doesn't support item deletion
```

---

## Methods on tuples

### in, not in
```python
t = (1, 2)
v = 1 in t  # v = True
```
### + operator
Concatenate tuples.  
```python
t1 = (1, 2)
t2 = ("Hey", "there")
t = t1 + t2  # t =  (1, 2, "Hey", "there")
```
### len()
Length of tuple  
```python
t = (5, 8, 8)
l = len(t)  # l = 3
```
### index()
First index of value
```python
t = (5, 8, 8)
v = t.index(8)  # v = 1
```
### count()
Number of occurrences of value.  
```python
t = 5, 8, 8
v = t.count(8)  # v = 2
```

---

## Operations on tuples  

### Tuple packing/unpacking
Tuple packing/unpacking
```python
t = 1, 2  # t = (1, 2)
x, y = t  # x = 1, y = 2
```
### Slicing a tuple.
Slicing
```python
t = ("hey", "there!", "how", "are", "you?")
v= t[2:]        # v =  ("how", "are", "you?")
v = t[:2]       # v =  ("hey", "there!")
v = t[-3:]      # v =  ("how", "are", "you?")
v = t[:-3]      # v =  ("hey", "there!")
v = t[1:4]      # v =  ("there!", "how", "are")
v = t[-1:1:-2]  # v = ('you?', 'how') 
```
Get a (shallow) copy of the tuple by slicing.  
```python
v = t[:]  # v = ("hey", "there!", "how", "are", "you?")
```
Get a reversed (shallow) copy of the tuple by slicing.
```python
v = t[::-1]  # v = ('you?', 'are', 'how', 'there!', 'hey')
```
### Reversing  
Reversed shallow copy  
```python
t = (2, 5, 8, 1, 9, 3, 7)
rt = t[::-1]  # rt = (7, 3, 9, 1, 8, 5, 2)
```
```python
t = (2, 5, 8, 1, 9, 3, 7) 
r = reversed(t)  # r = <reversed object at 0x...>
rt = tuple(r)    # rt = (7, 3, 9, 1, 8, 5, 2)
```
### Sorting
Sorting in reverse order  
```python
t = (2, 5, 8, 1, 9, 3, 7)
r = sorted(t, reverse=True)
rt = tuple(result)  # rt = (9, 8, 7, 5, 3, 2, 1)
```
### Copying
Shallow copy 
```python
import copy
t = ("hey", "there!", "how", "are", "you?")
tc = t[:]          # tc = ("hey", "there!", "how", "are", "you?")
tc = copy.copy(t)  # tc = ("hey", "there!", "how", "are", "you?")
```
Deep copy
```python
import copy
t = ("hey", "there!", "how", "are", "you?")
tc = copy.deepcopy(t)  # tc = ("hey", "there!", "how", "are", "you?")
```
### Swapping values with tuple  
```python
a = 'foo'
b = 'bar'
a, b = b, a  # a ='bar, b = 'foo'
```
### Counting
All elements together
```python
t = (1, 2, 3)
c = len(t)  # c = 3
```
Number of occurrences of value.  
```python
t = 5, 8, 8
v = t.count(8)  # v = 2
```
Counting occurrences of all elements -> use [collections.Counter](../collections/Counter.md) and its methods...
```python
from collections import Counter
t = ('B' ,'B' ,'A' ,'B' ,'C' ,'A' ,'B' ,'B' ,'A' ,'C')
c = Counter(t)  # c = Counter({'B': 5, 'A': 3, 'C': 2})
```
### Merging
```python
t1 = (1, 2)
t2 = ("Hey", "there")
t = t1 + t2  # t =  (1, 2, "Hey", "there")
```
---

