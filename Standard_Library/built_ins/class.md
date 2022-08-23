# Class
1. @staticmethod, @classmethod
   1. @staticmethod
   2. @classmethod
   3. instance method
2. @property
3. super()
4. \_\_new\_\_()

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
Restricting access (read, write and even delete only properties)
When you omit property methods you get access level you want. (see property with lambda)   

Usage:
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

