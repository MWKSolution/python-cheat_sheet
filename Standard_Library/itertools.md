# Itertools

1. [Infinite](#infinite)
2. [Terminating](#terminating)
3. [Combinatoric](#combinatoric)
4. [More-Itertools](#more-itertools)

[All itertools - python.org](https://docs.python.org/3/library/itertools.html)

---

## Infinite
Could be used with **next()**
### count()
Infinite counting  
```python
import itertools as it

i = it.count()
j = it.count(10, 2)
k = it.count(2.5, 0.5)

ii = list(zip(range(10), i))  
# ii = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
jj = list(zip(range(10), j))  
# jj = [(0, 10), (1, 12), (2, 14), (3, 16), (4, 18), (5, 20), (6, 22), (7, 24), (8, 26), (9, 28)]
kk = list(zip(range(10), k))  
# kk = [(0, 2.5), (1, 3.0), (2, 3.5), (3, 4.0), (4, 4.5), (5, 5.0), (6, 5.5), (7, 6.0), (8, 6.5), (9, 7.0)]
```
Use with **map()** or **zip()**  
When counting with floating point numbers, better accuracy can sometimes be achieved by substituting multiplicative code such as: (start + step * i for i in count()).  
### cycle()
Make an iterator returning elements from the iterable.  
```python
import itertools as it

i = it.cycle('ABCD')
ii = list(zip(range(10), i))
# ii = [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'A'), (5, 'B'), (6, 'C'), (7, 'D'), (8, 'A'), (9, 'B')]
```
### repeat()
Make an iterator that returns object over and over again. Runs indefinitely unless the times argument is specified.  
```python
import itertools as it

i = it.repeat(10, 3)
q = list(i)  # q = [10, 10, 10]

i = it.repeat('ABC', 2)
r = list(i)  # r = ['ABC', 'ABC']
```
A common use for repeat is to supply a stream of constant values to map or zip.  
```python
l = list(map(pow, range(10), repeat(2)))  # l = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## Terminating
### accumulate()
Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).  
If func is supplied, it should be a function of two arguments.
```python
import itertools as it
import operator as op

i = it.accumulate([1, 2, 3, 4, 5])
q = list(i)  # q = [1, 3, 6, 10, 15]
i = it.accumulate([1, 2, 3, 4, 5], initial=100)
r = list(i)  # r = [100, 101, 103, 106, 110, 115]
i = it.accumulate([1, 2, 3, 4, 5], op.mul, initial=10)
t = list(i)  # t = [10, 10, 20, 60, 240, 1200]
```
### chain()
Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. Used for treating consecutive sequences as a single sequence.  
```python
import itertools as it

i = it.chain('ABC', 'xyz')
q = list(i)  # q = ['A', 'B', 'C', 'x', 'y', 'z']
```
### chain.from_iterable()
Alternate constructor for chain(). Gets chained inputs from a single iterable argument that is evaluated lazily.
```python
import itertools as it

i = it.chain.from_iterable(['ABC', 'xyz'])
q = list(i)  # q = ['A', 'B', 'C', 'x', 'y', 'z']
```
### compress()
Make an iterator that filters elements from data returning only those that have a corresponding element in selectors that evaluates to True. Stops when either the data or selectors iterables has been exhausted.  
```python
import itertools as it

i = it.compress('ABCDEF', [1, 0, 1, 0, 1, 1])
q = list(i)  # q = ['A', 'C', 'E', 'F']
```
### dropwhile()
Make an iterator that drops elements from the iterable as long as the predicate is true, afterwards, returns every element.  
```python
import itertools as it

i = it.dropwhile(lambda x: x >= 0, [5, 3, 1, 0, -1, -2, 3, 5])
q = list(i)  # q = [-1, -2, 3, 5]
```
### filterfalse()
Make an iterator that filters elements from iterable returning only those for which the predicate is False.  
Oposite to buit-in **filter()**  
```python
import itertools as it

i = it.filterfalse(lambda x: x % 2, range(10))
q = list(i)  # q = [0, 2, 4, 6, 8]
```
### groupby()
Make an iterator that returns consecutive keys and groups from the iterable.  
```python
import itertools as it

l = 'AAAABBBCCDAABBB'
i = it.groupby(l)
t = [[k, ''.join(g)] for k, g in i]
# t = [['A', 'AAAA'], ['B', 'BBB'], ['C', 'CC'], ['D', 'D'], ['A', 'AA'], ['B', 'BBB']]
```
```python
import itertools as it
import operator as op

l = [('Animal', 'cat'), ('Animal', 'dog'), ('Bird', 'peacock'), ('Bird', 'pigeon')]
i = it.groupby(l, op.itemgetter(0))
d = {k: list(g) for k, g in i}
# d = {'Animal': [('Animal', 'cat'), ('Animal', 'dog')], 'Bird': [('Bird', 'peacock'), ('Bird', 'pigeon')]}

i = it.groupby(l, key=op.itemgetter(0))
dd = {k: [a[1] for a in g] for k, g in i}
# dd = {'Animal': ['cat', 'dog'], 'Bird': ['peacock', 'pigeon']}
```
### islice()
Like slice but for iterable. Unlike regular slicing, islice() does not support negative values for start, stop, or step.  
```python
import itertools as it

l = 'ABCDEFG'
i = it.islice(l, 2)
t = list(i)  # t = ['A', 'B']

i = it.islice(l, 2, 4)
q = list(i)  # q = ['C', 'D']

i = it.islice(l, 2, None)
w = list(i)  # w = ['C', 'D', 'E', 'F', 'G']

i = it.islice(l, 0, None, 2)
r = list(i)  # r = ['A', 'C', 'E', 'G']
```
### pairwise()
New in 3.10 !!!  
Return successive overlapping pairs taken from the input iterable.
### starmap()
Like **map()** but iterable is a list of tuples.  
```python
import itertools as it

i = it.starmap(pow, [(1, 2), (2, 2), (3, 2)])
q = list(i)  # q = [1, 4, 9]
# vs map
i = map(pow, [1, 2, 3], [2, 2, 2])
w = list(i)  # w = [1, 4, 9]
# or:
i = map(pow, [1, 2, 3], it.repeat(2))
x = list(i)  # x = [1, 4, 9]
```
### takewhile()
Make an iterator that returns elements from the iterable as long as the predicate is true.  
Opposite to **dropwhile()**  
```python
import itertools as it

l = [5, 3, 1, 0, -1, -2, 3, 5]

i = it.takewhile(lambda x: x >= 0, l)
q = list(i)         # q = [5, 3, 1, 0]

i = it.dropwhile(lambda x: x >= 0, [5, 3, 1, 0, -1, -2, 3, 5])
w = list(i)         # q = [-1, -2, 3, 5]

v = ((q + w) == l)  # v = True
```
### tee()
Return n independent iterators from a single iterable.  
```python
import itertools as it

l = [1, 2, 3]
i = it.tee(l, 3)
t = [list(n) for n in i]  # t = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

r = type(i)  # r = <class 'tuple'>
```
### zip_longest()
Like **zip()** but Iteration continues until the longest iterable is exhausted.  
missing values are filled-in with fillvalue (default - None).  
```python
import itertools as it

l1 = [1, 2, 3, 4]
l2 = [1, 2]
i = it.zip_longest(l1, l2)  
q = list(i)  # q = [(1, 1), (2, 2), (3, None), (4, None)]

i = it.zip_longest(l1, l2, fillvalue='xxx')
r = list(i)  # r = [(1, 1), (2, 2), (3, 'xxx'), (4, 'xxx')]
```
---

## Combinatoric
### product()
Cartesian product of input iterables.   
```python
import itertools as it

i = it.product('A')
t = [''.join(e) for e in i]  # t = ['A']

i = it.product('A', repeat=4)  # same as product('A', 'A', 'A', 'A')
u = [''.join(e) for e in i]  # u = ['AAAA']

i = it.product('AB')
r = [''.join(e) for e in i]  # r = ['A', 'B']

i = it.product('AB', repeat=2)  # same as product('AB', 'AB')
q = [''.join(e) for e in i]  # q = ['AA', 'AB', 'BA', 'BB']

i = it.product('AB', 'xy')
v = [''.join(e) for e in i]  # v = ['Ax', 'Ay', 'Bx', 'By']

i = it.product('AB', 'xy', repeat=2)  # same as product(['Ax', 'Ay', 'Bx', 'By']['Ax', 'Ay', 'Bx', 'By']) same as  product('AB', 'xy', 'AB', 'xy')
w = [''.join(e) for e in i]  # w = ['AxAx', 'AxAy', 'AxBx', 'AxBy', 'AyAx', 'AyAy', 'AyBx', 'AyBy', 'BxAx', 'BxAy', 'BxBx', 'BxBy', 'ByAx', 'ByAy', 'ByBx', 'ByBy']

i = it.product(range(2), repeat=3)
m = [''.join([str(s)for s in e]) for e in i]  # m = ['000', '001', '010', '011', '100', '101', '110', '111']
```
### permutations()
Successive r length permutations of elements in the iterable.
```python
import itertools as it

i = it.permutations('ABC')
t = [''.join(e) for e in i]  # t = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

i = it.permutations('ABA')
m = [''.join(e) for e in i]  # m = ['ABA', 'AAB', 'BAA', 'BAA', 'AAB', 'ABA'] !!!

i = it.permutations('ABC', r=2)
z = [''.join(e) for e in i]  # z = ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']

i = it.permutations('ABA', r=2)
q = [''.join(e) for e in i]  # q = ['AB', 'AA', 'BA', 'BA', 'AA', 'AB']  !!!
```
### combinations()
Return r length subsequences of elements from the input iterable.  
```python
import itertools as it

i = it.combinations('ABC', 3)
t = [''.join(e) for e in i]  # t = ['ABC']

i = it.combinations('ABC', 2)
m = [''.join(e) for e in i]  # m = ['AB', 'AC', 'BC']

i = it.combinations('ABC', 1)
z = [''.join(e) for e in i]  # m = ['A', 'B', 'C']
```
### combinations_with_replacement()
Return r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.  
```python
import itertools as it

i = it.combinations_with_replacement('ABC', 3)
t = [''.join(e) for e in i]  # t = ['AAA', 'AAB', 'AAC', 'ABB', 'ABC', 'ACC', 'BBB', 'BBC', 'BCC', 'CCC']

i = it.combinations_with_replacement('ABC', 2)
m = [''.join(e) for e in i]  # m = ['AA', 'AB', 'AC', 'BB', 'BC', 'CC']

i = it.combinations_with_replacement('ABC', 1)
z = [''.join(e) for e in i]  # m = ['A', 'B', 'C']
```

---

## More-Itertools
```
pip install more-itertools
```
For details see:  
[Itertools Recipes - python.org](https://docs.python.org/3/library/itertools.html#itertools-recipes)  
[more-itertools - pypi.org](https://pypi.org/project/more-itertools/)  
[API documentation - readthedocs.io](https://more-itertools.readthedocs.io/en/stable/api.html)  

[itertools as decorators](https://www.bbayles.com/index/decorator_factory)  
[itertools tour](https://martinheinz.dev/blog/16)  
[More itertools](https://www.gidware.com/real-world-more-itertools/)  

---
