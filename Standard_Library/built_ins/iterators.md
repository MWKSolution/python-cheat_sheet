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
## reversed()
...   
## sorted()
...  

---


