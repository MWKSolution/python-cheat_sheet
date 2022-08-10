# defaultdict

1. [Brief]()
2. [default_factory]()
   1. int
   2. list
   3. lambda
   4. function
   5. **kwargs
   6. Changing callable
3. [\_\_missing\_\_]()
4. [Passing Arguments to default_factory]()
5. [Usage]()
6. [defaultdict vs dict]()

---

## Brief
1. Subclass of dict.
2. Handles missing keys - never raises a KeyError.
3. Overries **\_\_missing\_\_()** method
4. Adds default_factory 

---

## default_factory
default_factory should be callable or None.  If is None KeyError will be invoked !!!  
Types of values could be different from default factory.
### int
```python
from collections import defaultdict
d = defaultdict(int)
v = d['a'] + 1  # v = 1, for value called int() = 0
```
### list
```python
from collections import defaultdict
d = defaultdict(list)
d['a'].append('A')
# d = defaultdict(<class 'list'>, {'a': ['A']}), list() = []
```
### lambda
```python
from collections import defaultdict
d = defaultdict(lambda: 'missing')
v = d['a']  # v = 'missing
```
### function
```python
from collections import defaultdict

def default_facory():
    return 'missing'

d = defaultdict(default_facory)
v = d['a']  # v = 'missing'
```
### **kwargs
Different defaullts for different keys, if not present run default_factory
```python
from collections import defaultdict
defaults = dict(a='A', b='B')
d = defaultdict(str, **defaults)  # or d = defaultdict(str, defaults); d = defaultdict(str, a='A', b='B'); ... 
# d = defaultdict(<class 'str'>, {'a': 'A', 'b': 'B'})
v = d['a']  # v = 'A'
v = d['b']  # v = 'B'
v = d['c']  # v = ''
```
### Changing callable  
d.default_factory = str  

---

## \_\_missing\_\_
default factory is called from **\_\_missing\_\_** which is not called by **get()**  
default_factory is only called from .__getitem__()  
```python
from collections import defaultdict
d = defaultdict(list)
# Calls d.__getitem__('missing')
v = d['missing']  # v = []
# Don't call dd.__getitem__('another_missing')
v = d.get('another_missing')  # v = None
# d = defaultdict(<class 'list'>, {'missing': []})
```

---

## Passing Arguments to default_factory

---

## Usage
1. Grouping (with list as default_factory)
2. Grouping unique (with set as default_factory)
3. Counting (with int as default_factory)
4. Accumulating (with float as default_factory)
5. Dealing with missing keys
6. Initializing items with constant value

---

## defaultdict vs dict
Same as dict  + **\_\_copy\_\_**, default_factory, **\_\_missing\_\_**  
Missing key dict solutions:
**setdefault()**, **get()**, conditional, handling **KeyError**  
defaultdict faster than dict.setdefault()**  
Creating dict faster than defaultdict  

