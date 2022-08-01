# List
1. Lists are mutable  
2. Lists are ordered  
3. Lists can contain arbitrary objects  
4. Lists can be nested  
5. max lenght of list = sys.maxsize = 2^64 = 9223372036854775807 (for 64-bit platform architecture)  

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
Nested lists
```python
l = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
v = l[0]  # v = 'a'
v = l[1]  # v =  ['bb', ['ccc', 'ddd'], 'ee', 'ff']
v = l[1][0]  # v = 'bb'
v = l[1][1]  # v = ['ccc', 'ddd']
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
## Modifying
Single value
```python
l = ['a', 'b', 'c']
l[1] = 15   # l = ['a', 15, 'c']
l[-1] = 99  # l = ['a', 15, 99]
```
Multiple values
```python
l = ['a', 'b', 'c', 'd', 'e']
l[1:4] = [1, 2]  # l = ['a', 1, 2, 'e']
l[2:2] = ['x', 'y']  # l =  ['a', 1, 2, 'x', 'y', 'e']
```
Remove
```python
l = ['a', 'b', 'c']
del l[0]       # v = ['b', 'c']
l.remove('c')  # v = ['b]
l.pop()        # v = []
l = ['a', 'b', 'c', 'd', 'e']
l[1:4] = []    # l = ['a', 'e']
l = ['a', 'b', 'c', 'd', 'e']
del l[1:4]     # l = ['a', 'e']
```
## Operators and built-in functions and methods  
### in, not in
```python
l = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
v = 'qux' in l       # v = True
v = 'thud' not in l  # v = True
```
### + * operators
```python
l = [1, 2, 3, 4]
ll = l + [5, 6]  # ll = [1, 2, 3, 4, 5, 6]
ll = l *2        # ll = [1, 2, 3, 4, 1, 2, 3, 4]
l += [5, 6]      # l = [1, 2, 3, 4, 5, 6]
```
Be careful:
```python
l = ['foo', 'bar', 'baz', 'qux', 'quux']
l += 'corge'  #  l = ['foo', 'bar', 'baz', 'qux', 'quux', 'c', 'o', 'r', 'g', 'e'], strings are iterable
l += 20
# TypeError: 'int' object is not iterable, should be l += [20]
```
### len()
```python
l = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
v = len(l)  # v = 6
```
### min()
```python
v =min(l)  # v = 'bar'
```
### max()
```python
v =max(l)  # v = 'qux'
```
### append()
Appends element to the list.  
```python
l = []
l.append(42)
l.append(21)  # l = [42, 21]
```
### clear()
Removes all elements from the list.  
```python
l = [1, 2, 3, 4, 5]
l.clear()  # l = []
```
### copy()
Shallow copy of a list.
```python
l = [1, 2, 3]
lc = l.copy  # lc = [1, 2, 3]
```
### count()
Counts the number of occurrences of element in the list.  
```python
l = [1, 2, 42, 2, 1, 42, 42]
v = l.count(42)  # v = 3
v = l.count(2)   # v = 2
```
### extend()
Adds all elements of an iterable iter (e.g. another list) to the list.  
```python
l = [1, 2, 3]
l.extend([4, 5, 6])  # l = [1, 2, 3, 4, 5, 6]
l = [1, 2, 3]
l += [4, 5, 6]       # l = [1, 2, 3, 4, 5, 6] - same result
```
### index()
Returns the position (index) of the first occurrence of value in the list.  
```python
l = ["Alice", 42, "Bob", 99]
v =  l.index("Alice")  # v = 0, start=0, stop = 2^64 (64 bit) = sys.maxszie !!!
l.index(99, 1, 3)      # start=1, stop=3
# ValueError: 99 is not in list
```
### insert()
Inserts element at position (index) in the list.
```python
l = [1, 2, 3, 4]
l.insert(3, 99)      # l = [1, 2, 3, 99, 4]
l.insert(55555, 66)  # index >= len(l) - at the end !, index <= -(len(l) +1) - at the beginning
# l = [1, 2, 3, 99, 4, 66]
```
### pop()
Remove and return element at given position (by default from the end).  
```python
l = [1, 2, 3, 4]
v = l.pop()   # index = -1, v = 4, l = [1, 2, 3]
v = l.pop(1)  # v = 2, l = [1, 3]
v = l.pop(100)
# IndexError: pop index out of range
l=[]
l.pop()
# IndexError: pop from empty list
```
### remove()
Removes the first occurrence of element in the list.
```python
l = [1, 2, 99, 4, 99]
l.remove(99)  # l = [1, 2, 4, 99]
l.remove(66)
# ValueError: list.remove(x): x not in list
```
### reverse()
Reverse list IN PLACE
```python
l = [1, 2, 3, 4]
l.reverse()  # l = [4, 3, 2, 1]
```
### sort()
Stable sort list IN PLACE
```python
l = [88, 12, 42, 11, 2]
l.sort()  # l = [2, 11, 12, 42, 88]
l = ['banana', 'pie', 'Washington', 'book']
l.sort(key=lambda x: x[::-1], reverse=True)  # l = ['Washington', 'book', 'pie', 'banana']
```
## List operations  
### Sorting
### Merging
### Comprehension
### Deep copy
