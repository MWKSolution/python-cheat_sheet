# Class
1. @staticmethod, @classmethod
   1. @staticmethod
   2. @classmethod
   3. instance method
2. property(), @property
3. super()

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

instance methods can access class by using:
self.__class__

__new__ - singelton ????