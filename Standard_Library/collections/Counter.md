## Counter  
Subclass of dictionary.  
### Initializing Counter
```python
from collections import Counter
# With sequence of items 
c = Counter(['B','B','A','B','C','A','B','B','A','C'])
# with dictionary
c = Counter({'A':3, 'B':5, 'C':2})
# with keyword arguments
c = Counter(A=3, B=5, C=2)
# Empty Counter
c = Counter()
```
### Updating Counter
```python
from collections import Counter
c = Counter()
c.update([1, 2, 3, 1, 2, 1, 1, 2])  # c = Counter({1: 4, 2: 3, 3: 1})
c.update([1, 2, 4])                 # c = Counter({1: 5, 2: 4, 3: 1, 4: 1})
# updating with another counter
c.update(Counter([1, 1, 1]))
```
Counter can have negative or zero counts:
```python
from collections import Counter
c = Counter(a=-2, b=-3)
c.update(a=2, b=2)  # c = Counter({'a': 0, 'b': -1})
```
Subtracting
```python
from collections import Counter
c = Counter(A=3, B=5, C=2)
c.subtract(A=3, B=10)  # c = Counter({'C': 2, 'A': 0, 'B': -5})
```
### Missing key
Returning 0 (zero)
```python
from collections import Counter
c = Counter("mississippi")
v = c["a"]  # v = 0
```
### most_common()
Frequency(counts) of elements.  
Returns list of tuples: (object, count)
```python
from collections import Counter
c = Counter(banana=15, tomato=4, apple=39, orange=30)
# The most common object
l = c.most_common(1)  # l = [('apple', 39)]
# The two most common objects
l = c.most_common(2)  # l = [('apple', 39), ('orange', 30)]
# All objects sorted by count
l  = c.most_common()  # l = [('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)], same as .most_common(None)
c.most_common(20)     # l = [('apple', 39), ('orange', 30), ('banana', 15), ('tomato', 4)]
```
least-common elements
```python
from collections import Counter
c = Counter(banana=15, tomato=4, apple=39, orange=30)
# All objects in reverse order
l = c.most_common()[::-1]    # l = [('tomato', 4), ('banana', 15), ('orange', 30), ('apple', 39)]
# The two least-common objects
l = c.most_common()[:-3:-1]  # l = [('tomato', 4), ('banana', 15)]
```
### +, -, &, | operators on Counter
```python
from collections import Counter
c1 = Counter(apple=4, orange=9, banana=4)
c2 = Counter(apple=10, orange=8, banana=6)
# sum
c = c1 + c2  # c = Counter({'orange': 17, 'apple': 14, 'banana': 10})
# subtract - not counting negative values
c = c2 - c1  # c = Counter({'apple': 6, 'banana': 2})
# lower values
c = c1 & c2  # c = Counter({'orange': 8, 'apple': 4, 'banana': 4})
# higher values
c = c1 | c2  # c = Counter({'apple': 10, 'orange': 9, 'banana': 6})
```
### +, - unary operators
```python
from collections import Counter
c = Counter(a=2, b=-4, c=0)
# only positive counts
v = +c  # v = Counter({'a': 2})
# only negative counts
v = -c  # v = Counter({'b': 4})
```
### elements()
Returns an iterator (!!!) over elements, repeating each of them as many times as its count.  
Zero or negative counts are ignored.  
Order after elements() could be different from the original list. 
```python
from collections import Counter
c = Counter('mississipi')  # c = Counter({'i': 4, 's': 4, 'm': 1, 'p': 1})
l = ''.join(c.elements())  # l = 'miiiissssp'
```
### Methods inherited from dict
**copy()**, **clear()**, **get()**, **items()**, **keys()**, **pop()**, **popitem()**, **setdefault()**, **values()**  
**fromkeys** - not provided to prevent ambiguities:
```python
from collections import Counter
c = Counter.fromkeys("mississippi", 2)
# NotImplementedError: Counter.fromkeys() is undefined.  Use Counter(iterable) instead.
```