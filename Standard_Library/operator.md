# Operator
1. Brief
2. Operators as functions
3. Item lookups
   1. attrgetter()
   2. itemgetter()
   3. methodcaller()


---

## Brief
Module operator exports Python operators as functions.  
Module also defines tools for generalized attribute and item lookups.  

---

## Operators as functions
[Full list of mapping operators to functions...](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)  
Some interesting operators:
```python
import operator as op 
op.setitem(obj, k, v)  ->  obj[k] = v
op.delitem(obj, k)     ->  del obj[k]
op.getitem(obj, k)     ->  obj[k]
# all above with slices
seq[i:j] = values      ->  setitem(seq, slice(i, j), values)
del seq[i:j]           ->  delitem(seq, slice(i, j))
seq[i:j]               ->  getitem(seq, slice(i, j))

op.truth(obj)          ->  obj
op.index(a)            ->  int(a)
```
Only in **operator**:
```python
import operator as op
l = [1, 1, 1]
v = op.countOf(l, 1)  # v = 3
w = op.indexOf(l, 1)  # w = 0
```
```python
import operator as op
import sys

l = [1, 1, 1]  
z = op.length_hint(l)  # z = 3 - got from len()

class C:
    def __init__(self):
        self.x = 1
        self.y = 2
    def __length_hint__(self):
        return sys.getsizeof(self)

c = C()
q = len(c)             # TypeError: object of type 'C' has no len()
r = op.length_hint(c)  # r = 48
# used for memory allocation or for completion time estimate
```
Operator as functions useful when something need to return or pass function, not operator:
```python
import operator as op

t1 = (1, 2, 3)
t2 = (4, 5, 6)

def combiner(a, b, fun):
    r = [fun(i, j) for (i, j) in zip(a, b)]
    return r

v = combiner(t1, t2, op.add)  # v = [5, 7, 9]

# or in sort
g = sorted(t1, key=op.neg)    # g = [3, 2, 1]
```

---

## Item lookups

### attrgetter()
After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
```python
from collections import namedtuple
import operator as op

Data = namedtuple('Data', 'x y z')
d1 = Data(1, 6, 8)  # d1 = Data(x=1, y=6, z=8)
d2 = Data(3, 3, 7)
d3 = Data(4, 9, 2)

v = max((d1, d1, d3), key=op.attrgetter('z'))  # v = Data(x=1, y=6, z=8)
# key is calling to d1.z, d2.z and d3.z
# equivalent to:
w = max((d1, d1, d3), key=lambda x: x.z)  # w = Data(x=1, y=6, z=8)
# !!! attrgetter is faster than lambda !!!
```
!!! attrgetter is faster than lambda !!!
### itemgetter()
After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
```python
import operator as op

d1 = (1, 6, 8)  # d1 = (1, 6, 8)
d2 = (3, 3, 7)
d3 = (4, 9, 2)

v = max((d1, d1, d3), key=op.itemgetter(2))  # v = (1, 6, 8)
w = max((d1, d1, d3), key=lambda x: x[2])    # w = (1, 6, 8)
# !!! itemgetter is faster than lambda !!!
```
!!! itemgetter is faster than lambda !!!
```python
import operator as op
v = op.itemgetter(1)('ABCDEFG')               # v = 'B'
w = op.itemgetter(1, 3, 5)('ABCDEFG')         # w = ('B', 'D', 'F')
z = op.itemgetter(slice(2, None))('ABCDEFG')  # z = 'CDEFG'
# works on dict -> uses __getitem__
t = op.itemgetter('rank')(dict(rank='captain', name='dotterbart'))  # t = 'captain'
```

### methodcaller()
After f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).  
```python
import operator as op

l = ['aaaa', 'bb', 'ccccccc', 'd', 'eee']
v = [op.methodcaller('upper')(i) for i in l if op.methodcaller('startswith', 'b')(i)]
# v = ['BB']
w = [i.upper() for i in l if i.startswith('b')]
# w = ['BB']
```