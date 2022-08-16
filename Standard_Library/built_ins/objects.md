# Objects
   1. callable()
   2. setattr()
   3. delattr()
   4. getattr()
   5. hasattr()
   6. dir()
   7. hash()
   8. id()
   9. isinstance()
   10. issubclass()
   11. object
   12. repr()
   13. vars()
   14. type()

---

## callable()
Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. 
```python
x = 5
i = callable(x)  # i = False
v = x()
# TypeError: 'int' object is not callable
def x():
    return 5
v = x()          # v = 5 - callable
j = callable(x)  # j = True
```
Classes are callable (calling a class returns a new instance).
Instances are callable if their class has a **\_\_call\_\_()** method.
```python
class C:
    def __call__(self):
        return 5

c = C()          # C = <class '__main__.C'>, c = <__main__.C object at 0x...>
v = c()          # v =5

i = callable(C)  # i = True
j = callable(c)  # j = True
```

---

## setattr()
The function assigns the value to the attribute, provided the object allows it.  
```python
class C:
    pass

o = C()             # o.__dict__ = {}

setattr(o, 'a', 5)  # o.__dict__ = {'a': 5}
v = o.a             # v = 5
# equivalent to:
o.a = 5
```

---

## delattr()
The function deletes the named attribute, provided the object allows it.  
```python
class C:
    pass

o = C()
o.a = 5           # o.__dict__ = {'a': 5}

delattr(o, 'a')   # o.__dict__ = {}
# is equivalent to:
del o.a
# now: AttributeError: a

```

---

## getattr()
Return the value of the named attribute of object. name must be a string.  
If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.  
```python
class C:
    pass

o = C()
o.a = 5                         # o.__dict__ = {'a': 5}
v = getattr(o, 'a')             # v = 5
# equivalent to:
v = o.a                         # v = 5
v = getattr(o, 'b', 'default')  # v = 'default'
v = getattr(o, 'c')             # AttributeError: 'C' object has no attribute 'c'

```
For private attributes (name mangling !!!):  
```python
class C:
    __a = 5

o = C()

v = getattr(o, '_C__a')  # v = 5
v = getattr(o, '__a')    # AttributeError: 'C' object has no attribute '__a'
```

---

## hasattr()
True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)  
```python
class C:
    pass

o = C()
o.a = 5              # o.__dict__ = {'a': 5}
v = hasattr(o, 'a')  # v = True  
v = hasattr(o, 'b')  # v = False
```
```python
v =  hasattr(str, '__len__')  # v = True
```

---


