# Iterators
   1. enumerate()
   2. filter()
   3. map()
   4. iter()
   5. next()
   6. range()
   7. zip()
   8. reversed()
   9. sorted()

---

## enumerate()
Return an enumerate object.  
**! Use rather enumerate than range !**  
```python
t = ('a', 'b', 'c')
e = enumerate(t)  # e = <enumerate object at 0x...>
r = tuple(e)      # r = ((0, 'a'), (1, 'b'), (2, 'c'))
```
```python
t = ('a', 'b', 'c')
e = enumerate(t, start=10)  # or: enumerate(t, 10)
r = tuple(e)      # r = ((10, 'a'), (11, 'b'), (12, 'c'))
```

---

## filter()
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.  
**!!! Use list comprehensions instead !!!**  
```python
t = (7, -3, 11, 0, -2)
f = lambda x: True if x >= 0 else False
i = filter(f, t)  # i = <filter object at 0x...>
r = tuple(i)      # r = (7, 11, 0)
```
Inverse: **itertools.filterfalse()** 

---

## map()
Return an iterator that applies function to every item of iterable, yielding the results.   
**!!! Use list comprehensions instead !!!**
```python
t = (1, 2, 3, 4, 5)
f = lambda x: x**2
i = map(f, t)  # i = <map object at 0x...>
r = tuple(i)   # r = (1, 4, 9, 16, 25)
```
For iterable of tuples: **itertools.starmap()** 

---

## iter()
[See iterator](../iterator.md)
## next()
[See iterator](../iterator.md)  

---

## range()
Rather than being a function, range is actually an immutable sequence type.  
**! Use rather enumerate than range !**  
```python
r = range(10)  # r = range(0, 10)
t = tuple(r)   # t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```
```python
r = range(10, 20, 2)  # r = range(10, 20, 2)
t = tuple(r)          # t = (10, 12, 14, 16, 18)
```
```python
r = range(10, -6, 2)
t = tuple(r)  # t = (10, 8, 6, 4, 2, 0, -2, -4)
```
```python
r = reversed(range(5))  # r = <range_iterator object at 0x...>
t = tuple(r)            # t = (4, 3, 2, 1, 0)
```
```python
r = range(0)
t = tuple(r)  # t = ()
```
---

## zip()
Iterate over several iterables in parallel, producing tuples with an item from each one.  
The iterator stops when the shortest input iterable is exhausted.  
```python
n = [1, 2, 3]
l = ['a', 'b', 'c']
z = zip(n, l)  # z = <zip object at 0x...>
r = list(z)    # r = [(1, 'a'), (2, 'b'), (3, 'c')]
```
No arguments
```python
z = zip()    # empty iterator
r = list(z)  # r = []
```
One argument
```python
l = ['a', 'b', 'c']
z = zip(l)
r = list(z)  # r = [('a',), ('b',), ('c',)]
```
Unequal length
```python
z = zip(range(5), range(100))
r = list(z)  # r = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
```
!!! From Pyton 3.10 there is argument: *strict=True* to raise error if iterables unequal. !!!    
For zip on longest iterable: **itertools.zip_longest()**

Looping over multiple iterables
```python
l = ['a', 'b', 'c']
n = [0, 1, 2]
for i, j in zip(l, n):
    print(i, j, end=' ; ')
# Output: a 0 ; b 1 ; c 2 ;
```
Unzipping
```python
l = ['a', 'b', 'c']
n = [0, 1, 2]
z = zip(l, n)
ll, nn = zip(*z)  # ll = l , nn = n
```
Iterating over two dictionaries at once  
```python
d1 = {'a': 0, 'b': 1, 'c': 2}
d2 = {'x': 10, 'y': 11, 'z': 12}
for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
    print(k1, '->', v1, ' : ', k2, '->', v2)
# Output:
# a -> 0  :  x -> 10
# b -> 1  :  y -> 11
# c -> 2  :  z -> 12
```
Build dictionary  
```python
l = ['a', 'b', 'c']
n = [0, 1, 2]
z = zip(l, n)
d = dict(z)  # d = {'a': 0, 'b': 1, 'c': 2}
```

---

## reversed()
### dict
Reversing keys order
```python
d = {'a': 10, 'b': 20, 'c': 30}
r = reversed(d.items())  # r = <dict_reverseitemiterator object at ...>, reversed returns iterator !!!!
v = dict(r)                    # v = {'c': 30, 'b': 20, 'a': 10}
```
### list
in-place
```python
l = [1, 2, 3, 4]
l.reverse()  # l = [4, 3, 2, 1]
```
out-of-place
```python
l = [1, 2, 3, 4]
lr = list(reversed(l))  # lr = [4, 3, 2, 1], reversed() returns iterator !!!!
```
### tuple
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
### set
Set is not reversible !!! - set is unordered !!!!!!
```python
s = {4, 1, 3, 2}
l = reversed(s)
# TypeError: 'set' object is not reversible
```

---

## sorted()
### dict
General sorting using built-in sorted()
```python
d = {6:'George', 2:'John', 1:'Potter', 9:'Micheal', 7:'Robert', 8:'Gayle'} 
v = sorted(d)           # v = [1, 2, 6, 7, 8, 9]
v = sorted(d.keys())    # v = [1, 2, 6, 7, 8, 9]
v = sorted(d.items())   # v = [(1, 'Potter'), (2, 'John'), (6, 'George'), (7, 'Robert'), (8, 'Gayle'), (9, 'Micheal')]
v = sorted(d.values())  # v = ['Gayle', 'George', 'John', 'Micheal', 'Potter', 'Robert']
```
Sorting by value in reverse order  
```python
d = {6:'George', 2:'John', 1:'Potter', 9:'Micheal', 7:'Robert', 8:'Gayle'}  
lst = sorted(d.items(), key=lambda x: x[1], reverse=True)
# lst = [(7, 'Robert'), (1, 'Potter'), (9, 'Micheal'), (2, 'John'), (6, 'George'), (8, 'Gayle')]
dct = dict(lst)
# dct = {7: 'Robert', 1: 'Potter', 9: 'Micheal', 2: 'John', 6: 'George', 8: 'Gayle'}
```
### list
Lists With Non-Comparable Data Types Can’t Be sorted !!!  
In-place
```python
l = [5, 2, 3, 1, 4]
l.sort()  # l = [1, 2, 3, 4, 5]
```
Out-of-place
```python
l = [5, 2, 3, 1, 4]
ls = sorted(l)  # ls = [1, 2, 3, 4, 5]
```
With parameters (sort and sorted)
```python
l = ['aaaa', 'bb', 'ccccccc', 'd', 'eee']
l.sort(key=len, reverse=True)  # l = ['ccccccc', 'aaaa', 'eee', 'bb', 'd']
```
### tuple
Sorting in reverse order  
```python
t = (2, 5, 8, 1, 9, 3, 7)
r = sorted(t, reverse=True)
rt = tuple(result)  # rt = (9, 8, 7, 5, 3, 2, 1)
```
### set
Set is unordered - sorting to list.
```python
s = {4, 1, 3, 2}
l = sorted(s)  # l = [1, 2, 3, 4]
```

---


