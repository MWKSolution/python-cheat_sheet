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
### remove()
### discard()
### pop()
### clear()
### update() |=
### intersection_update() &=
### difference_update() -=
### symmetric_difference_update() ^=

---

## Operators and Methods
### | union()
### & intersection()
### - difference()
### ^ symmetric_difference() - xor
### isdisjoint()
### issubset() <=
### <
### issuperset() >=
### \>

---

## frozenset
frozenset is immutable !!!
Non-modifying operations only, methods that attempt to modify a frozenset fail.  
```python
fs = frozenset(['foo', 'bar', 'baz'])  # fs =  frozenset({'foo', 'baz', 'bar'})
fs.add('qux')
# AttributeError: 'frozenset' object has no attribute 'add'
```
Augmented operators could be used since they don't work IN PLACE !!!  
Usage:
1. Sets of frozensets - elements of ordinary must be immutable
```python
fs1 = frozenset(['foo'])
fs2 = frozenset(['bar'])
fs3 = frozenset(['baz'])
s = {fs1, fs2, fs3}  # s = {frozenset({'bar'}), frozenset({'baz'}), frozenset({'foo'})}
```
2. keys for dicts  

---