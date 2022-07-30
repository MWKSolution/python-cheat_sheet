# List
1. Lists are mutable  
2. Lists are ordered
3. Lists can contain arbitrary objects

## Defining list
```python
 a = ['foo', 'bar', 'baz', 'qux']
```

## Referring/Accessing
By index
```python
#      0      1      2      3      4       5
l = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
#     -6     -5     -4     -3     -2      -1
v = l[0]
v = l[-6]  # v = 'foo'
v = l[5] 
v = l[-1]  # v = 'corge'
```
Slicing  
```python
l = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
v = l[-5:-2]  
v = a[1:4]               # v = ['bar', 'baz', 'qux']
v = a[-5:-2] == a[1:4]   # v = True
v = a[:4] + a[4:] == a   # v = True
v = a[1:6:2]             # v = ['bar', 'qux', 'corge']
v = a[::-1]              # v = ['corge', 'quux', 'qux', 'baz', 'bar', 'foo']
v = a[:]                 # v = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
v = a[:] is a            # v = False, it's a copy!
```