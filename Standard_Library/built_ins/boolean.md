# Boolean
   1. all()
   2. any()
   3. bool()

---
By default, an object is considered true unless its class defines either a **\_\_bool\_\_()** method that returns False or a **\_\_len\_\_()** method that returns zero.  
False values:  
None, False, 0, 0.0, 0j, '', (), [], set(), range(0)  

---

## all()
Return True if bool(x) is True for all values x in the iterable.  
If the iterable is empty, return True.  
```python
v = all([True, True, False])  # v = False
```

---

## any()
Return True if bool(x) is True for any x in the iterable.  
If the iterable is empty, return False.  
```python
v = any([False, True, False])  # v = True
```

---

## bool()
Return a Boolean value
```python
v = bool(1 == 1)  # v = True
v = bool([])      # v = False
```

---
