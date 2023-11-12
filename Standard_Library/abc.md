# Abstarct Base Classes (abc)  

1. [Brief](#brief)
2. [ABCMeta](#abcmeta)
   1. [Usage](#usage)
   2. [Formal interface](#formal-interface)
3. [ABC](#abc)
4. [Virtual Base Classes](#virtual-base-classes)
   1. [Usage](#usage-1)
   2. [\_\_subclasshook__()](#subclasshook)
   3. [Other functions](#other-functions)
---

## Brief

ABCMeta is a metaclass for defining Abstract Base Classes.  

## ABCMeta
ABCMeta is used for defining formal interface with **@abstractmethod, @abstractclassmethod, @abstractstaticmethod, @abstarctproperty**  Use type hints!!!   
### Usage
```python
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass
```
### Formal interface
Definition:
```python
class SomeInterface(metaclass=ABCMeta):
    @abstractmethod
    def required_method_1(self):
        pass
    @abstractmethod
    def required_method_2(self):
        pass
```
Class defined in the way shown belown cannot be instatiated: 
```python
class SomeClass(SomeInterface):
    pass

o = SomeClass()  # error: TypeError: Can't instantiate abstract class SomeClass with abstract methods required_method_1, required_method_2
```
Proper way:
```python
class SomeClass(SomeInterface):
    def required_method_1(self):
        pass
    def required_method_2(self):
        pass

o = SomeClass()
```
Methods defined without @abstarctmethod... could be used as Mixin methods!

## ABC
A helper class that has ABCMeta as its metaclass.  
```python
from abc import ABC
class MyABC(ABC):
    pass
```
it is generally equivalent to:
```python
from abc import ABCMeta
class MyABC(metaclass=ABCMeta):
    pass
```


## Virtual Base Classes

### Usage

ABCs introduce virtual subclasses, which are classes that don’t inherit from a class but are still recognized by isinstance() and issubclass().  
We tell the interpreter explicitly "it implemented our interface, please treat it as the subclass of our own class."  
Registered class don't show up in ABC MRO and are not accessible by super().   
```python
from abc import ABCMeta, abstractmethod

class SomeAbstract(metaclass=ABCMeta):
    @abstractmethod
    def duck_method(self):
        pass

class SomeClass(SomeAbstract):
    def duck_method(self):
        print('Quack from some class object...')

sco = SomeClass()
sco.duck_method()

@SomeClass.register # <--------------- register with decorator...
class OtherClass:
    def duck_methodx(self):
        print('Quack from somewhere else...')

SomeClass.register(OtherClass) # <---- ... or register with statement

oco = OtherClass()
oco.duck_methodx()
```
output when not registered:
```python
# Quack from some class object...
# Quack from somewhere else...
print(isinstance(oco, SomeClass))  # False
print(isinstance(oco, OtherClass)) # True
print(isinstance(sco, SomeClass))  # True
print(isinstance(sco, OtherClass)) # False

print(issubclass(SomeClass, OtherClass)) # False
print(issubclass(OtherClass, SomeClass)) # False
```
output when registered:
```python
# Quack from some class object...
# Quack from somewhere else...
print(isinstance(oco, SomeClass)) # True
print(isinstance(oco, OtherClass)) # True
print(isinstance(sco, SomeClass)) # True
print(isinstance(sco, OtherClass)) # False

print(issubclass(SomeClass, OtherClass)) # False
print(issubclass(OtherClass, SomeClass)) # True
```

Or even with built-in classes:
```python
from abc import ABC
class MyABC(ABC):
    pass
MyABC.register(tuple)

assert issubclass(tuple, MyABC)  # True
assert isinstance((), MyABC)     # True
```
When usesed with ABC classes could be registered to abstractclass, when used wirh metaclass= register to concrete class otherwise it doesn't work!  
### \_\_subclasshook__
Method **abc.register** could be overriden with **\_\_subclasshook__** to prevent registering anythin you want. It enables to check what class should have to be considered subclass.     
It returns True when a class is found to be subclass of a ABC class, it returns False if it is not and returns NotImplemented if the subclass check is continued with the usual mechanism.  
```python
from abc import ABC, abstractmethod

class AssumedSubclass:
    def __method__(self):
        pass

class NotSubClass:
    pass

class SomeClass(ABC):
    @abstractmethod
    def __method__(self):
        pass
    @classmethod
    def __subclasshook__(cls, other_cls):
        if cls is SomeClass:
            if any("__method__" in c.__dict__ for c in other_cls.__mro__):
                return True
        return NotImplemented

print(issubclass(AssumedSubclass, SomeClass)) # TRUE
print(issubclass(NotSubClass, SomeClass))     # FALSE
```

### Other functions

```python
abc.get_cache_token()
abc.update_abstractmethods(cls)
```