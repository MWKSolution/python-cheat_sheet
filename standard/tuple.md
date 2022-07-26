# Tuple  
1. Tuple is immutable
2. Program execution is faster when manipulating a tuple than it is for the equivalent list.
3. Use tuple if data is not to be modified

## Defining tuple  
Directly:  
```
t = (1, 2, 3)  # t = (1, 2, 3)
```
From iterable:
```
t = tuple([1, 2])  # t = (1, 2)
```
Tuple packing:  
```
t = 1, 2  # t = (1, 2)
```
Empty tuple:  
```
t = ()
```
One item tuple (comma is necessary):  
```
t = 1,    # <class 'tuple'>
t = (1,)  # <class 'tuple'>
t = (1)   # <class 'int'> !!!
``` 
Tuple can have heterogeneous items:  
```
t = ('Hey', (1, 2), 1, ['you', 'me'])
```
## Accessing elements
```
t = ("hey", "there!", "how", "are", "you?")
v = t[0]           # v = "hey"
v = t[len(t) - 1]  # v = "you?"
v = t[-1]          # v = "you?"
```
# Tuples are immutable  
We cannot change tuple contents!!!
```
t = (1, 2, 3)
t[0] = 100  # Gives error: TypeError: 'tuple' object does not support item assignment
del t[0]    # Gives error: TypeError: 'tuple' object doesn't support item deletion
```
## Methods on tuples

### in, not in
```
t = (1, 2)
v = 1 in t  # v = True
```
### + operator
Concatenate tuples.  
```
t1 = (1, 2)
t2 = ("Hey", "there")
t = t1 + t2  # t =  (1, 2, "Hey", "there")
```
### len()
Length of tuple  
```
t = (5, 8, 8)
l = len(t)  # l = 3
```
### index()
First index of value
```
t = (5, 8, 8)
v = t.index(8)  # v = 1
```
### count()
Number of occurrences of value.  
```
t = 5, 8, 8
v = t.count(8)  # v = 2
```
# Operations on tuples  

## Tuple packing/unpacking
Tuple packing/unpacking
```
t = 1, 2  # t = (1, 2)
x, y = t  # x = 1, y = 2
```
## Slicing a tuple.
Slicing
```
t = ("hey", "there!", "how", "are", "you?")
v= t[2:]        # v =  ("how", "are", "you?")
v = t[:2]       # v =  ("hey", "there!")
v = t[-3:]      # v =  ("how", "are", "you?")
v = t[:-3]      # v =  ("hey", "there!")
v = t[1:4]      # v =  ("there!", "how", "are")
v = t[-1:1:-2]  # v = ('you?', 'how') 
```
Get a (shallow) copy of the tuple by slicing.  
```
v = t[:]  # v = ("hey", "there!", "how", "are", "you?")
```
Get a reversed (shallow) copy of the tuple by slicing.
```
v = t[::-1]  # v = ('you?', 'are', 'how', 'there!', 'hey')
```
## Reversing  
Reversed shallow copy  
```
t = (2, 5, 8, 1, 9, 3, 7)
rt = t[::-1]  # rt = (7, 3, 9, 1, 8, 5, 2)
```
## Sorting
Sorting in reverse order  
```
t = (2, 5, 8, 1, 9, 3, 7)
r = sorted(t, reverse=True)
rt = tuple(result)  # rt = (9, 8, 7, 5, 3, 2, 1)
```
## Copying
Shallow copy 
```
import copy
t = ("hey", "there!", "how", "are", "you?")
tc = t[:]          # tc = ("hey", "there!", "how", "are", "you?")
tc = copy.copy(t)  # tc = ("hey", "there!", "how", "are", "you?")
```
Deep copy
```
import copy
t = ("hey", "there!", "how", "are", "you?")
tc = copy.deepcopy(t)  # tc = ("hey", "there!", "how", "are", "you?")
```
## Swapping values with tuple  
```
a = 'foo'
b = 'bar'
a, b = b, a  # a ='bar, b = 'foo'
```
