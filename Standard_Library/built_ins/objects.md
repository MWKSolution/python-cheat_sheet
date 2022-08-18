# Objects
   1. object()
   2. id()
   3. type()
   4. repr()
   5. hash()
   6. setattr()
   7. delattr()
   8. getattr()
   9. hasattr()
   10. isinstance()
   11. issubclass()
   12. callable()

---

## object()
Return a new featureless object. object is a base for all classes.  
 object does not have a **\_\_dict\_\_**, so you can’t assign arbitrary attributes to an instance of the object class !!!  
```python
class C:
    pass

v = issubclass(C, object)  # v = True
o = object()               # o = <object object at 0x...>
w = dir(C)                 # w = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
z = dir(object)            # z = ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
x = set(w) - set(z)        # x = {'__module__', '__dict__', '__weakref__'}
```
**object()** could be used as a unique sentinel when **None** cannot be used.  
Every **object()** call creates unique object contrary to **None** !!!  
```python
a, b = None, None
s1, s2 = object(), object()
v = a is b   # v = True
w = s1 is b  # w = False
```

---

## id()
Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.  
This is the address of the object in memory.  
Objects with the same value are usually stored at separate memory addresses !!!
Immutable:  
```python
a = 'Hello World'
b = 'Hello World'
c = 'Hello Worl'
d = 'Hello Worl' + 'd'
ida = id(a)   # ida = 40196528
idb = id(b)   # idb = 40196528 = ida
idc = id(c)   # idc = 40217264
idd = id(d)   # idd = 40196528 = ida = idb
v = (a is b)  # v = True
w = (a == b)  # w = True
x = (a is d)  # w = True
y = (a == d)  # w = True
```
Mutable:
```python
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c = [1, 2, 3]
c.append(4)

ida = id(a)   # ida = 40065792
idb = id(b)   # idb = 40065344
idc = id(c)   # idc = 41695168 

v = (a is b)  # v = False
w = (a == b)  # w = True
x = (a is c)  # x = False
y = (a == c)  # y = True
```

---

## type()
### One argument - type(object):  
Return the type of an object. The return value is a type object and generally the same object as returned by **object.\_\_class\_\_**
In Python, everything is an object. Classes are objects as well. As a result, a class must have a type.  
```python
v = type([1, 2, 3])  # v = <class 'list'>
w = type(35)         # w = <class 'int'>

class C:
    pass

c = C()
x = type(c)          # x = <class '__main__.C'>
r = c.__class__      # r = <class '__main__.C'>

y = type(C)          # y = <class 'type'>
z = type(list)       # z = <class 'type'>
t = type(type)       # t = <class 'type'>
```
The **isinstance()** built-in function is recommended for testing the type of an object, because it takes subclasses into account!!!  

### Three arguments - new object  
This is essentially a dynamic form of the class statement.  
```python
class Foo:
    pass

Fuu = type('Fuu', (Foo,), dict(a=100, av=lambda x : x.a))

f = Fuu()          # f = <__main__.Fuu object at 0x...>
v = f.__class__    # v = <class '__main__.Fuu'>
c = Fuu.__class__  # c = <class 'type'>
b = Fuu.__bases__  # b = (<class '__main__.Foo'>,)
n = Fuu.__name__   # n = 'Fuu'
r = Fuu.__dict__   # r = mappingproxy({'a': 100, 'av': <function <lambda> at 0x...>, '__module__': '__main__', '__doc__': None})
q = vars(Fuu)      # q = mappingproxy({'a': 100, 'av': <function <lambda> at 0x...>, '__module__': '__main__', '__doc__': None})

# definition with type is equivalent to:
class Fuu(Foo):
    a = 100
    def av(self):
        return self.a
```

---

## repr()
Return a string containing a printable "official" representation of an object.  
For many objects it returns representation that could be used for objdect creation with **eval()**.  
```python
import datetime
d = datetime.datetime.now()               # d = datetime.datetime(2022, 8, 17, 15, 7, 32, 902063) - from repr :-)
# readable format for date-time object
s = str(d)                                # s = '2022-08-17 15:07:32.902063' - type str
# the official format of date-time object
r = repr(d)                               # r = 'datetime.datetime(2022, 8, 17, 15, 7, 32, 902063)' - type str
dd = eval(r)                              # dd = datetime.datetime(2022, 8, 17, 15, 9, 40, 894384)
t = type(dd)                              # t = <class 'datetime.datetime'>
```
What this function returns for its instances can be overridden by defining a **\_\_repr\_\_()** method.  
```python
class Test:
    pass

t = Test()      # t = <__main__.Test object at 0x...>
ty = type(t)    # ty = <class '__main__.Test'>

class ReprTest:
    def __repr__(self):
        return 'ReprTest()'

c = ReprTest()  # c = ReprTest()
r = repr(c)     # r = 'ReprTest()'
v = eval(r)     # v = ReprTest()
tt = type(v)    # tt = <class '__main__.ReprTest'>
```
str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable.  

---

## hash()
1. A hash function performs hashing by turning any data into a fixed-size sequence of bytes called the hash value or the hash code.  
2. **hash()** return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).  
3. Objects hashed using hash() are irreversible, leading to loss of information.
4. hash() returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects !!!  
5. because the hash function projects a potentially infinite set of values onto a finite space, this can lead to a *hash collision* when two different inputs produce the same hash value.  
```python
v = hash(123)        # v = 123
w = hash('abc')      # w = 5864359080172279384
x = hash((1, 2, 3))  # x = 529344067295497451
z = hash([1, 2, 3])  # TypeError: unhashable type: 'list'
```
Python provides a default implementation for the special method .__hash__() in your classes, which merely uses the object’s identity to derive its hash code:
```python
class C:
    pass

c1 = C()
c2 = C()
v1 = hash(c1)  # v1 = 2506816
v2 = hash(c2)  # v2 = 2509927
```
You can explicitly mark your class as unhashable by setting its **\_\_hash\_\_** attribute equal to **None**:
```python
class H:
    __hash__ = None
    pass

h = H()
v = hash(h)  # TypeError: unhashable type: 'H'
```
Therefore, hash codes must be immutable for the hashing to work as expected.  
!!! hash-equal contract !!!
when you implement .__eq__(), you should always implement a corresponding .__hash__(). The only time you don’t have to implement both methods is when you use a wrapper such as a data class or an immutable named tuple that already does this for you.  
```python
class Person:
    def __init__(self, name, date_of_birth, married):
        self.name = name
        self.date_of_birth = date_of_birth
        self.married = married

    def __hash__(self):
        return hash(self._fields)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return self._fields == other._fields

    @property
    def _fields(self):
        return self.name, self.date_of_birth, self.married
```
!!! stick to Python’s data classes or named tuples whenever you can to guarantee the proper implementation of hashable types. !!!  

```python
@dataclass(unsafe_hash=True)
class Person:
    name: str
```

---

## setattr()
The function assigns the value to the attribute, provided the object allows it.  
Use @property to manage that (setting).
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
Use @property to manage that (deleting).
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
Manage attributes (properties) access with @property.
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

## isinstance()
Return True if the object argument is an instance of the class argument, or of a (direct, indirect, or virtual) subclass thereof.  
```python
class C:
    pass

c = C()
v = isinstance(c, C)                     # v = True
w = isinstance(c, object)                # w = True
x = isinstance(5, int)                   # x = True
y = isinstance(5, object)                # y = True
z = isinstance('abc', (int, str, dict))  # z = True, from 3.10 Union can be used
```

---

## issubclass()
Return True if class is a subclass (direct, indirect, or virtual) of class. A class is considered a subclass of itself.
```python
class C:
    pass

class SC(C):
    pass

v = issubclass(SC, C)                    # v = True
w = issubclass(SC, object)               # w = True
x = issubclass(SC, list)                 # x = False
y = issubclass(SC, (int, list, object))  # y = True
```

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
Use **\_\_call\_\_()** when:
1. Instance has only one method
2. Your arguments need to be functions
3. You want to return functions

---


