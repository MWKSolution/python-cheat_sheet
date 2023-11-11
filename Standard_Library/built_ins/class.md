# Class
1. [@staticmethod, @classmethod](#staticmethod-classmethod)
   1. [@staticmethod](#staticmethod)
   2. [@classmethod](#classmethod)
   3. [instance method](#instance-method)
2. [@property](#property)
   1. [Defining](#defining)
   2. [Restricting access](#restricting-access)
   3. [Usage](#usage)
3. [super()](#super)
   1. [Basic use](#basic-use)
   2. [Multiple inheritance](#multiple-inheritance)
   3. [Mixin](#mixin-)
4. [\_\_new\_\_()](#new)

---

## @staticmethod, @classmethod
### @staticmethod
Transform a method into a static method.  
A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()).  
It is not required to create an instance of the class to call a static method !!!
I used for some utility functions that do not act on instance or class attributes.
```python
class C:
    @staticmethod
    def method(x):
        return x + 5
# without instance  
v = C.method(5)  # v = 10
# with instance
c = C()
w = c.method(1)  # w = 6
```
staticmethod as regular function:
```python
def func(x):
    return x + 5

class C:
    method = staticmethod(func)
    
v = C.method(5)  # v = 10
```
### @classmethod
Transform a method into a class method.  
A class method can be called either on the class (such as C.f()) or on an instance (such as C().f()).  
Used for factory design pattern methods - returns class object.  
```python
class C:
    cattr = 'class_atrr'
    @classmethod
    def method(cls, x):
        cls.cattr += '_a'
        return cls.cattr + x

# without instance
m = C.cattr        # m = 'class_atrr'
v = C.method('?')  # v = 'class_atrr_a?'
w = C.cattr        # w = 'class_atrr_a'
# with instance
c = C()
y = c.method('#')  # y = 'class_atrr_a_a#'
z = c.cattr        # z = 'class_atrr_a_a'
t = C.cattr        # t = 'class_atrr_a_a'
```
Factory design pattern
```python
from datetime import date
  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)  # !!! -> returns cls()  !!!
  
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
  
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)  # factory
v = person1.age         # v = 21
w = person2.age         # w = 25
x = Person.isAdult(22)  # x = True
```
As regular function
```python
def func(obj, x):
    return repr(obj) + x

class C:
    method = classmethod(func)

v = C.method('xxx')  # v = "<class '__main__.C'>xxx"
```

### instance method
```python
class C:
    cp = 'class_attr'
    def __init__(self, a):
        self.ia = a
    # instance method
    def im(self, b):
        self.ia += b
        return self.cp + self.ia

c = C('!!')     
n = C.im('?')    # TypeError: im() missing 1 required positional argument: 'b'
o = C.im(c, '?') # BUT!!!: o = 'class_attr!!?'
w = c.cp         # w = 'class_attr'
r = C.cp         # r = 'class_attr'
x = c.ia         # x = '!!?'
z = C.ia         # AttributeError: type object 'C' has no attribute 'ia'
t = c.im('??')   # t = 'class_attr!!???'
m = c.ia         # m = '!!???'
```
Instance methods can access class by using: self.__class__  
```python
class C:
    # instance method
    def im(self):
        return self.__class__.__name__

c = C()
v = c.im()  # v = 'C'
```

---

## @property
### Defining
To hide internal attributes make them properties.  
Unless you need something more than bare attribute access, don’t write properties. They’re a waste of CPU time, and more importantly, they’re a waste of your time.  
```python
class C:
    def __init__(self):
        self._x = 'prop'

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
```
With decorators:
```python
class C:
    def __init__(self):
        self._x = 'prop'

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

v = C.x      # v = <property object at 0x...>
q = C.x.__doc__  # q = "I'm the 'x' property."
c = C()
w = c.x      # getter
x = c._x     # use __x for mangling !
c.x = 'xxx'  # setter
del c.x      # deleter
r = c.x      # AttributeError: 'C' object has no attribute '_x'
```
With lambda (read only property)
```python
class C:
    def __init__(self):
        self._x = 'prop'

    x = property(lambda self: self._x)

c = C()
v = c.x  # v = 'prop'
```

### Restricting access
(read, write and even delete only properties)
When you omit property methods you get access level you want. (see property with lambda)   

### Usage
1. validating inputs
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None
```
2. Computed attributes with cache
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = None

    @property
    def diameter(self):
        if self._diameter is None:
            self._diameter = self.radius * 2
        return self._diameter
```
or use  **functools.cached_property()**  
This kind of implementation is suitable for those computations in which the input values don’t mutate.  
If you want to create a cached property that doesn’t allow modification  
@ property and @functools.cache() 

3. logging access, managing deletion
4. Creating Backward-Compatible Class APIs
5. Overriding Properties in Subclasses

---

## super()
Return a proxy object that delegates method calls to a parent or sibling class of type.  
It allows you to call methods of the superclass in your subclass - mainly used with **\_\_init\_\_**  
### Basic use
```python
class B:
    def method(self, argb):
        self.arg = argb * 2 + '_'
        return True

class C(B):
    def method(self, argc1, argc2):
        super().method(argc1)  # same as super(C, self).method(argc1)
        self.arg += argc2 * 3  # self.arg could be used because of super()
        return True

c = C()
c.method('a', 'b')
v = c.arg  # v = 'aa_bbb'
```
### Multiple inheritance
1. MRO method resolution order - order of super() callings
2. All methods that are called with super() need to have a call to their superclass’s version of that method.  
3. inheritance - "is a", other methods:
   1. composition - "has a"
   2. mixin - "includes a"
4. !!! composition instead of inheritance !!!

Matching arguments' signature:
1. fixed positional arguments
2. keyword arguments:
```python
class Shape:
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)        

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

cs = ColoredShape(color='red', shapename='circle')
```
Make sure target exists: (at the end  - **object** doesn't have method)
1. root class
```python
class Root:
    def method(self):
        # do something
        assert not hasattr(super(), 'method')

class B(Root):
    def method(self):
        super().method()

class C(B):
    def method(self):
        super().method()

c = C()
c.method()
```
Incorporating non-cooperative class and other things collected together
```python
class Root:
    def __init__(self, **kwds):
        print('root init', kwds)
    def method(self):
        print('root method')
        assert not hasattr(super(), 'method')

class NonCooperative:
    def __init__(self, x, y):
        print('non-cooperative init', x, y, end=' -> ')
        self.x = x
        self.y = y
    def method(self):
        print('non-cooperative method', end=' -> ')

class NonCooperativeAdapter(Root):
    def __init__(self, x, y, **kwds):
        print('adapter init', kwds, end=' -> ')
        self.nc = NonCooperative(x, y)
        super().__init__(**kwds)
    def method(self):
        print('adapter method', end=' -> ')
        self.nc.method()
        super().method()

class B(Root):
    def __init__(self, a, b, **kwds):
        print('B init', a, b, kwds, end=' -> ')
        self.a = a
        self.b = b
        super().__init__(**kwds)
    def method(self):
        print('B method', end=' -> ')
        super().method()

class C(B, NonCooperativeAdapter):
    pass

c = C(a='a', b='b', x='x', y='y')
c.method()
d = C.__bases__  # d = (<class '__main__.B'>, <class '__main__.NonCooperativeAdapter'>)
j = C.__mro__    # j = (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.NonCooperativeAdapter'>, <class '__main__.Root'>, <class 'object'>)
# output:
# B init a b {'x': 'x', 'y': 'y'} -> adapter init {} -> non-cooperative init x y -> root init {}
# B method -> adapter method -> non-cooperative method -> root method
```
### Mixin  

Mixins are small classes (mini-classes) that focus on providing a small set of specific features that you can later combine with code that live in other classes.  
Mixins are used to enhance or to add features to another set of code. A mixin is not meant to be used by itself.  
In general, there are 2 cases where you would like to implement something like this:
- You want to provide a lot of optional features for a class.
- You want to use one particular feature in a lot of different classes.
```python
class MixIn:
    def print_data(self):
        print(self.data)

class SomeClass(MixIn):
    def __init__(self):
        self.data = 'Some data'

o = SomeClass()
o.print_data()  # output: Some data
```

---

## \_\_new\_\_
The **\_\_new\_\_()** is a static method of the object class. 
**\_\_init\_\_()** adds attributes to **\_\_dict\_\_**
```python
class C:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return super().__new__(cls)  # this returning instance of C and passing it to __init__
        # same: return object.__new__(cls, *args, **kwargs)
        # or: return super(C, cls).__new__(cls, *args, **kwargs)
    def __init__(self):
        print('Initialising instance')

c = C()  # c = <__main__.C object at 0x000000000266D1F0>
# output: Creating instance
#         Initialising instance
```
If **\_\_new\_\_()** doesn't return **object.\_\_new\_\_()** or **super().\_\_new\_\_()**, or return object of different class **\_\_init\_\_()** will not be executed!!!
, in this case **\_\_new\_\_()** returns None !!!  
But **\_\_new\_\_()** could return any object which will became instance of class !!! **\_\_init\_\_()** not executed !!!
```python
class C(object):
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return 'abcd' 
    def __init__(self):
        print('Initialising instance')

c = C()  # c = 'abcd'
# output: Creating instance
```
Arguments for **\_\_init\_\_()** and **\_\_new\_\_()** have to have same arguments but...  
!!! Caution: **super().\_\_new\_\_()* for sure have different number of arguments and it will cause error:
```python
class SomeClass:
    def __new__(cls, value):                # or  __new__(cls, *args, **kwargs):
        return super().__new__(cls, value)  # or super().__new__(cls, *args, **kwargs)
    def __init__(self, value):
        self.value = value

x = SomeClass(42)
# TypeError: object.__new__() takes exactly one argument (the type to instantiate)
```
Proper way:
```python
class SomeClass:
    def __new__(cls, value):                # or  __new__(cls, *args, **kwargs):
        return super().__new__(cls)  # or super().__new__(cls, *args, **kwargs)
    def __init__(self, value):
        self.value = value

x = SomeClass(42)
v = x.value   # v = 42
```
Everything you can do in the **\_\_init\_\_()** method, you can do it in the **\_\_new\_\_()**  
Usage:
1. Inheriting from immutable built-in types:
```python
class SquareNumber(int):
    def __new__(cls, value):
        return super().__new__(cls, value ** 2)

x = SquareNumber(3)  # x = 9
```
2. Returning object of different class - init is not executed - described above
 

3. Singelton
```python
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

first = Singleton()
second = Singleton()
v = (first is second)  # v = True
```
Be careful: in this example  **\_\_init\_\_()** run every time you call Singleton().  
Use **\_\_new\_\_()** for initialization !!  

