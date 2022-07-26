# Dictionary  
1. Dictionary is mutable
2. Python dictionaries were unordered before version 3.6.
3. In Python versions less than 3.6, (for example) popitem() would return an arbitrary (random) key-value pair !!!

## Defining a Dictionary  
Directly:
```
MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'}
```
From mapping (key, value) pairs:
```
MLB_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')])
```
From **kwargs
```
MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners')
```
From iterable
```
d = dict(iterable) 
```
Incrementally from empty dict:  
```
person = {}
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
```
Keys types could be any immutable type  
```
foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
```
## Referring  
```
v = MLB_team_1['Minnesota']  # v='Twins'
v = MLB_team_2['Colorado']   # v='Rockies'
```
## Referring non-existing key  
```
v = MLB_team['Toronto']  # KeyError: 'Toronto'
``` 
Referring by index is irrelevant, 'index' is treated as key !!!!  
```
v = MLB_team[1]  # KeyError: 1
d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}  # this is valid dictionary definition !!!
```
## Update entry  
```
MLB_team['Kansas City'] = 'Royals'
```
## Delete entry
```
del MLB_team['Seattle']
```
## Restrictions on dictionaries
1. A given key can appear in a dictionary only once  
2. A dictionary key must be of a type that is immutable:  

```
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}  # a tuple is ok
d = {[1, 1]: 'a', [1, 2]: 'b', [2, 1]: 'c', [2, 2]: 'd'}  # a list is not:
# TypeError: unhashable type: 'list'
```
## Restrictions on values
NONE  
## Operators and built-in functions and methods  
### in, not in  
```
b = 'Milwaukee' in MLB_team    # key is in dict: True
b = 'Toronto' not in MLB_team  # key is not in dict: True
```
### len()
```
l = len(MLB_team)  # l = 5
```
### clear()  
Clears a dictionary.  
```
d = {'a': 10, 'b': 20, 'c': 30}
d.clear()  # d = {}
```
### get()  
Returns the value for a key if it exists in the dictionary.  
```
d = {'a': 10, 'b': 20, 'c': 30}
v = d.get('b')      # v = 20
v = d.get('z')      # if key is not found, v = None
v = d.get('z', -1)  # with default value if key is not found, v = -1
```
### items()  
Returns a list of key-value pairs (tuples) in a dictionary.  
```
d = {'a': 10, 'b': 20, 'c': 30}
i = d.items()  # i = [('a', 10), ('b', 20), ('c', 30)]
```
### keys()  
Returns a list of keys in a dictionary.  
```
d = {'a': 10, 'b': 20, 'c': 30}
k = d.keys()  # k = ['a', 'b', 'c']
```
### values()  
Returns a list of values in a dictionary.  
```
d = {'a': 10, 'b': 20, 'c': 30}
v = d.values()  # v = [10, 20, 30]
```
### pop()  
Removes a key from a dictionary, if it is present, and returns its value.  
```
d = {'a': 10, 'b': 20, 'c': 30}
v = d.pop('b')      # v = 20, d = {'a': 10, 'c': 30}
v = d.pop('z')      # key is not present, KeyError: 'z'
v = d.pop('z', -1)  # key is not present, with default value  v = -1, d = {'a': 10, 'b': 20, 'c': 30}
```
### popitem()  
Removes the last added key-value pair from a dictionary.  
```
d = {'a': 10, 'b': 20, 'c': 30}
v = d.popitem()  # v = ('c', 30), d = {'a': 10, 'b': 20}
v = d.popitem()  # v = ('b', 20), d = {'a': 10}
v = d.popitem()  # d = {} !
v = d.popitem()  # KeyError: 'popitem(): dictionary is empty'
```
### update()  
Merges a dictionary with another dictionary or with an iterable of key-value pairs.  
```
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)  # d1 = {'a': 10, 'b': 200, 'c': 30, 'd': 400}  key 'b' is present in both dicts
```
'+' operator cannot be used on dictionaries !!!   
```
d = d1 + d2
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
```
### copy()  
Shallow copy of a dict.  
```
dc = d.copy()  # Creates new dictionary.
```
### setdefault()  
Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.  
```
d = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
v = d.setdefault('C')  # v = 'Geeks'
```
```
d = { 'A': 'Geeks', 'B': 'For'}
v = d.setdefault('C')           # v = None, d = {'A': 'Geeks', 'B': 'For', 'C': None}
v = d.setdefault('D', 'Geeks')  # v = 'Geeks', d = {'A': 'Geeks', 'B': 'For', 'C': None, 'D': 'Geeks'}
```
### fromkeys()  
It creates a new dictionary from the given iterable with the specific value  
```
seq = {'a', 'b', 'c', 'd', 'e'}
v = dict.fromkeys(seq)       # v = {'d': None, 'a': None, 'b': None, 'c': None, 'e': None} 
v = dict.fromkeys(seq, 1)    # v = {'d': 1, 'a': 1, 'b': 1, 'c': 1, 'e': 1}
lis = [2, 3]
v = dict.fromkeys(seq, lis)  # v = {'d': [2, 3], 'e': [2, 3], 'c': [2, 3], 'a': [2, 3], 'b': [2, 3]} 
lis.append(4)                # v = {'d': [2, 3, 4], 'e': [2, 3, 4], 'c': [2, 3, 4], 'a': [2, 3, 4], 'b': [2, 3, 4]}
```
# Dictionary operations

## Sorting Dictionary  
General sorting using built-in sorted()
```
d = {6:'George', 2:'John', 1:'Potter', 9:'Micheal', 7:'Robert', 8:'Gayle'}  
v = sorted(d.keys())    # v = [1, 2, 6, 7, 8, 9]
v = sorted(d.items())   # v = [(1, 'Potter'), (2, 'John'), (6, 'George'), (7, 'Robert'), (8, 'Gayle'), (9, 'Micheal')]
v = sorted(d.values())  # v = ['Gayle', 'George', 'John', 'Micheal', 'Potter', 'Robert']
```
Sorting by value in reverse order  
```
d = {6:'George', 2:'John', 1:'Potter', 9:'Micheal', 7:'Robert', 8:'Gayle'}  
lst = sorted(d.items(), key=lambda x: x[1], reverse=True)
# lst = [(7, 'Robert'), (1, 'Potter'), (9, 'Micheal'), (2, 'John'), (6, 'George'), (8, 'Gayle')]
dct = dict(lst)
# dct = {7: 'Robert', 1: 'Potter', 9: 'Micheal', 2: 'John', 6: 'George', 8: 'Gayle'}
```
## Deep copy
```
import copy
d = {6:'George', 2:'John', 1:'Potter', 9:'Micheal', 7:'Robert', 8:'Gayle'}
new = copy.deepcopy(d)
```


