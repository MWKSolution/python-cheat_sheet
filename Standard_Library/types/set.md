# Set
1. [Brief]()  
2. [Defining]()
3. [Updating, Modifying]()
   1. add()
   2. remove()
   3. discard()
   4. pop()
   5. clear()
   6. update() |=
   7. intersection_update() &=
   8. difference_update() -=
   9. symmetric_difference_update() ^=
4. [Operators and Methods]()
   1. | union()
   2. & intersection()
   3. \- difference()
   4. \^ symmetric_difference() - *xor*
   5. isdisjoint()
   6. issubset() <=
   7. <
   8. issuperset() >=
   9. \>
5. [frozenset]()
   1. Description
   2. Usage
   
--- 

## Brief
1. Unique elements.
2. Unordered.  
3. Elements must be immutable.  

---

## Defining  
*! Duplicate values only once !*  
From iterable
```python
s = set(['foo', 'foo', 'bar', 'baz', 'foo', 'qux'])  # s = {'qux', 'foo', 'bar', 'baz'}
```
With braces
```python
s = {'q', 'u', 'u', 'x'}  # s = {'x', 'u', 'q'}
```
Warning...
```python
s = {'foo'}     # s = {'foo'}
s = set('foo')  # s = {'o', 'f'}
```
Empty set only with set() !!!
```python
s = {}
t = type(s)  # t = <class 'dict'>
s = set()
t = type(s)  # t = <class 'set'>
```
Sets can have objects of different types which must be immutable !
```python
s = {42, 'foo', (1, 2, 3), 3.14159}  # s = {42, 'foo', 3.14159, (1, 2, 3)}
s = {[1,2], {1:'a', 2:'b'}}
# TypeError: unhashable type: 'list' ... 'dict' 
```

---

## Updating, Modifying
### add()
Add an element to a set.
This has no effect if the element is already present.
```python
s.add(x)
```
### remove()
Remove an element from a set; it must be a member.  
If the element is not a member, raise a KeyError.  
```python
s.remove(x)
```
### discard()
Remove an element from a set if it is a member.  
If the element is not a member, do nothing.  
```python
s.discard(x)
```
### pop()
Removes a random element from a set.  
Raises KeyError if set is empty.  
```python
s.pop()
```
### clear()
Remove all elements from this set.    
```python
s.clear()
```
### update() |=
In-place union.  
### intersection_update() &=
In-place intersection.  
### difference_update() -=
In-place difference.  
### symmetric_difference_update() ^=
In-place symmetric_difference.

---

## Operators and Methods
### | union()
```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
s = a.union(b, c, d)
s = a | b | c | d  # s = {1, 2, 3, 4, 5, 6, 7}
```
### & intersection()
```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
s = a.intersection(b, c, d)
s = a & b & c & d  # s = {4}
```
### - difference()
```python
a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
s = a.difference(b, c)
s = a - b - c  # s = {1, 2, 3}
```
### ^ symmetric_difference() - xor
```python
a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}
s = a ^ b ^ c  # s = {100, 5, 10}
s =  a.symmetric_difference(b, c)
# TypeError: symmetric_difference() takes exactly one argument (2 given)
s = a.symmetric_difference(b)  # s = {1, 50, 5, 10}
```
### isdisjoint()
```python
a = {1, 3, 5}
b = {2, 4, 6}
s = a.isdisjoint(b)  # s = True
```
### issubset() <=
```python
a = {1, 2, 3, 4, 5}
b = {2, 3, 4}
s = b.issubset(a)  # s = True
s = (b <= a)       # s = True
```
### <
```python
a = {1, 2, 3, 4, 5}
b = {2, 3, 4}
s = (b < a)  # s = True
```
### issuperset() >=
```python
a = {1, 2, 3, 4, 5}
b = {2, 3, 4}
s = a.issuperset (b)  # s = True
s = (a >= b)          # s = True
```
### \>
```python
a = {1, 2, 3, 4, 5}
b = {2, 3, 4}
s2 = (a > b)          # s = True
```
---

## frozenset
### Description
frozenset is immutable !!!
Non-modifying operations only, methods that attempt to modify a frozenset fail.  
```python
fs = frozenset(['foo', 'bar', 'baz'])  # fs =  frozenset({'foo', 'baz', 'bar'})
fs.add('qux')
# AttributeError: 'frozenset' object has no attribute 'add'
```
Augmented operators could be used since they don't work IN PLACE !!!  
### Usage
1. Sets of frozensets - elements of ordinary must be immutable
```python
fs1 = frozenset(['foo'])
fs2 = frozenset(['bar'])
fs3 = frozenset(['baz'])
s = {fs1, fs2, fs3}  # s = {frozenset({'bar'}), frozenset({'baz'}), frozenset({'foo'})}
```
2. keys for dicts  
keys in dictionary must be immutable !

---

## Set operations
### Set comprehension
No duplicates!
```python
l = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
s = {i for i in l}  # s = {1, 2, 3, 4, 5, 6, 7}
```
### Sorting
Set is unordered - sorting to list.
```python
s = {4, 1, 3, 2}
l = sorted(s)  # l = [1, 2, 3, 4]
```
### Merging
\+ operator is not supported !!!
Excluding duplicate items !
```python
s1 = {4, 1, 3, 2}
s2 = {5, 6, 3, 1}
ss = s1.union(s2)  # ss = {1, 2, 3, 4, 5, 6}
s1.update(s2)      # s1 = {1, 2, 3, 4, 5, 6}
```
### Copy
Shallow copy  
```python
s = {4, 1, 3, 2}
ss = s.copy()  # ss = {1, 2, 3, 4}
```
### Counting
```python
s = {4, 1, 3, 2}
c = len(s)  # c = 4
```
### Reversing
Set is not reversible !!! - set is unordered !!!!!!
```python
s = {4, 1, 3, 2}
l = reversed(s)
# TypeError: 'set' object is not reversible
```

---