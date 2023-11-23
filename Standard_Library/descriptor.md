# Descriptor
<!-- TOC -->
* [Descriptor](#descriptor)
  * [Brief](#brief)
  * [Descriptor protocol](#descriptor-protocol)
  * [Standard descriptor](#standard-descriptor)
  * [Descriptor using **\_\_dict__**](#descriptor-using-dict)
  * [Owner without **\_\_init__**](#owner-without-init)
  * [Descriptor abstarct class](#descriptor-abstarct-class)
  * [Descriptor with the metaclass](#descriptor-with-the-metaclass)
<!-- TOC -->
---
## Brief
- Descriptors let objects customize attribute lookup, storage, and deletion.
- Typical use case for descriptors is to write reusable code and make your code D.R.Y.
- Lazy properties. These are properties whose initial values are not loaded until they’re accessed for the first time.

## Descriptor protocol
Descriptors are Python objects that implement methods of the descriptor protocol:  
```python
class Descriptor:
    def __get__(self, instance, owner):
        ...
    def __set__(self, instance, value):
        ...
    def __delete__(self, instance):
        ...
    def __set_name__(self, owner, name):
        ...
```
## Standard descriptor

Standard definition using getaddr, setaddr(), deladdr(). Have to use _name for referencing
```python
class Descriptor:  # Descriptor class

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self._name = '_' + name  # <--- use this for referencing to avoid recurrently calling inst.d by getaddr !!! 

    def __get__(self, instance: object, owner: type) -> T:
        return getattr(instance, self._name, None)  # < ----- default value is None

    def __set__(self, instance: object, value: T) -> None:
        setattr(instance, self._name, value)

    def __delete__(self, instance: object) -> None:
        delattr(instance, self._name)

class Owner:
    d: int = Descriptor()  # descriptor instance

    def __init__(self, d: int = 0):  # <--  or you can define default value in here
        self.d = d
```

## Descriptor using **\_\_dict__**

Defining descriptor using **\_\_dict__** instead of getaddr, setaddr, ...
```python
class Descriptor:  # Descriptor class

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name  # <<----  when __dict__ is used you could reference just by name !!!

    def __get__(self, instance: object, owner: type) -> T:
        return instance.__dict__.get(self.name, None)  # < ----- default value is None

    def __set__(self, instance: object, value: T) -> None:
        instance.__dict__[self.name] = value

    def __delete__(self, instance: object) -> None:
        del instance.__dict__[self.name]

class Owner:
    d: int = Descriptor()  # descriptor instance

    def __init__(self, d: int = 0):  # <--  or you can define default value in here
        self.d = d
```
## Owner without **\_\_init__**
without **\_\_init__** in owner class and with default value:
```python
class Descriptor:  # Descriptor class

    def __init__(self, default: T = 100) -> None:  # for defining default value here or...
        self.default = default

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name  # <<----  when __dict__ is used you could reference just by name !!!

    def __get__(self, instance: object, owner: type) -> T:
        return instance.__dict__.get(self.name, self.default)  # < ----- default value is None

    def __set__(self, instance: object, value: T) -> None:
        instance.__dict__[self.name] = value

    def __delete__(self, instance: object) -> None:
        del instance.__dict__[self.name]

class Owner:
    d: int = Descriptor(15)  # descriptor instance with default value   ...or here
```
## Descriptor abstarct class
with descriptor as abstract class and  with validation
```python
from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar('T')

class Descriptor(ABC):

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name  # <<----  when __dict__ is used you could reference just by name !!!

    def __get__(self, instance: object, owner: type) -> T:
        return instance.__dict__.get(self.name, None)  # < ----- default value is None

    def __set__(self, instance: object, value: T) -> None:
        self.validate(value)  #  < --- for validating
        instance.__dict__[self.name] = value

    def __delete__(self, instance: object) -> None:
        del instance.__dict__[self.name]

    @abstractmethod
    def validate(self, value: int):
        pass

class Desc(Descriptor):  #descriptor class with validator
    def validate(self, value):
        if value < 0:
            raise ValueError('Must be grater than zero.')

class Owner:
    d: int = Desc()  # descriptor instance

    def __init__(self, d: int = 0):
        self.d = d

    def inc_d(self) -> None:
        self.d += 1
```
results
```python
inst = Owner() # inst.d=0
inst.d = 5555  # inst.d=5555 
del inst.d     # inst.d=None
inst.d = 7777  # inst.d=7777
inst.d = -13   # ValueError: Must be grater than zero.
inst.inc_d()   # 7778
```
## Descriptor with the metaclass

Automated adding __init__ to owner class with use of metaclasses
```python
import sys
from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar('T')

class Descriptor(ABC):  # Descriptor abstract class

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name  # <<----  when __dict__ is used you could reference just by name !!!

    def __get__(self, instance: object, owner: type) -> T:
        return instance.__dict__.get(self.name, None)  # < ----- default value is None

    def __set__(self, instance: object, value: T) -> None:
        self.validate(value)  #  < --- for validating
        instance.__dict__[self.name] = value

    def __delete__(self, instance: object) -> None:
        del instance.__dict__[self.name]

    @abstractmethod
    def validate(self, value: int):
        pass

def _make_init(fields, **kwargs):  # <-- makes code for __init__ in owner instance
    sig = [f + '=' + repr(kwargs[f]) if f in kwargs.keys() else f for f in fields]  #<-- check if any defaults were provided in owner definition
    code = f"def __init__(self, {', '.join(sig)}):\n"
    for name in fields:
        code += f'    self.{name} = {name}\n'
    return code

class OwnerMeta(type):  # meta class for owner
    def __new__(cls, name, bases, attrs, **kwargs):
        descriptors = [k for k, v in attrs.items() if isinstance(v, Descriptor)]  # list of provided descriptors
        if descriptors:
            exec(_make_init(descriptors, **kwargs), globals(), attrs)  # adding __init__ to class definition, default values are in kwargs
        return super().__new__(cls, name, bases, attrs)

class Desc(Descriptor):  # Descriptor class with validator
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError('value must be int.')
        if value < 0:
            raise ValueError('Must be grater than zero.')

class Owner(metaclass=OwnerMeta, d=17):  # <--- default value is put here as kwarg!!!
    d: int = Desc()  # descriptor instance

    def inc_d(self) -> None:
        self.d += 1
```
results
```python
inst = Owner() # inst.d=17
inst.d = 5555  # inst.d=5555 
del inst.d     # inst.d=None  # preserving default value could be added to metaclass !!!
inst.d = 7777  # inst.d=7777
inst.d = -13   # ValueError: Must be grater than zero.
inst.inc_d()   # 7778
inst.__init__  # <bound method __init__ of <__main__.Owner object at 0x...> - so method is present
inspect.signature(inst.__init__)  # (d=17)
inspect.ismethod(inst.__init__))  # True
```
