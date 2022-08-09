# namedtuple()  
1. [Brief]()
2. [Creating]()
   1. Required arguments
   2. Additional arguments
      1. rename
      2. defaults
      3. module
   3. \_\_doc\_\_
3. [Creating instances]()
4. [Accessing]()
5. [Methods inherited from tuple]()
6. [namedtuple methods and attributes]()
   1. _make()
   2. _asdict()
   3. _replace()
   4. _fields
   5. _field_defaults
7. [namedtuple operations]()
   1. Iterating over fields and values
   2. Conversions
   3. Subclassing namedtuple
8. [namedtuples usage]()
9. [namedtuple vs ...]()
   1. @dataclass
   2. typing.NamedTuple


---

## Brief
1. Function! that creates class.  
2. Returns new subclass of **tuple** with named fields.
3. Have similar memory consumption to regular tuples.  
4. Instance creation is ! much slower ! than for tuple

---

## Creating
### Required arguments
Typename ("Point") should be valid Python identifier.  
Names ("x y") cannot start with underscore (_)
```python
from collections import namedtuple
# list of sting
Point = namedtuple("Point", ["x", "y"])
# comma-separated string
Point = namedtuple("Point", "x, y")
# space-separated sring
Point = namedtuple("Point", "x y")
p = Point(2, 4)  # p = Point(x=2, y=4), Point = type(p) = <class '__main__.Point'>
```
### Additional arguments:  
**rename**  
If rename is true, invalid fieldnames are automatically replaced with positional names.  
```python
from collections import namedtuple

def get_data():
    return ['a', 'b', 'a', 'class', '_x', 'y', '12', 'z']

Data = namedtuple("Data", get_data(), rename=True)
t = Data._fields  # t = ('a', 'b', '_2', '_3', '_4', 'y', '_6', 'z')
```
**defaults**  
Fills with default values from given list. Starting from right !!!  
Number of given + default parameters should match number of parameters in definition.
```python
from collections import namedtuple
Developer = namedtuple("Developer",
                       "name level language",
                       defaults=["Junior", "Python"])
d = Developer("John")  # d = Developer(name='John', level='Junior', language='Python')
```
**module**  
Sets **\_\_module\_\_** attribute of namedtuple
```python
from collections import namedtuple
Point = namedtuple("Point", "x y", module='point')
p = Point(2, 4)
v = Point.__module__  # v = 'point'
v = p.__module__      # v = 'point'
```
### \_\_doc\_\_
Docstrings can be customized by making direct assignments to the \_\_doc\_\_.
```python
from collections import namedtuple
Point = namedtuple("Point", "x y", module='point')
v = Point.__doc__  # v = 'Point(x, y)'
Point.__doc__ = 'pxy'
v = Point.__doc__  # v = 'pxy'
```

---

## Creating instances  
```python
from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point(2, 4)
p = Point(x=2, y=4)
p = Point(**{"x": 2, "y": 4})  # p = Point(x=2, y=4)
# from iterable
p = Point._make([2, 4])
```

---

## Accessing
Fields can be accessed by names:  
```python
from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point(2, 4)      # p = Point(x=2, y=4)
x = p[0]             # x = 2, like normal tuple
y = p[1]             # y = 4
x = p.x              # x = 2
y = p.y              # y = 4
x = getattr(p, 'x')  # x = 2
y = getattr(p, 'y')  # y = 4
```

---

## Methods inherited from tuple
+, len(), index(), count(), ...

---

## namedtuple methods and attributes  
To prevent name conflicts with custom fields, the names of these attributes and methods start with an underscore.  
### _make()
Create named tuple instance from iterable.
```python
from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point._make([2, 4])  # p = Point(x=2, y=4)
```
### _asdict()
Convert existing named tuple instance into dictionary.  
From Python 3.8 regular dict, earlier - OrderedDict.
```python
from collections import namedtuple
Person = namedtuple("Person", "name age height")
jane = Person("Jane", 25, 1.75)
j = jane._asdict()  # j = {'name': 'Jane', 'age': 25, 'height': 1.75}
```
### _replace()
Returns ! *new* ! namedtuple instance with changed value.
```python
from collections import namedtuple
Person = namedtuple("Person", "name age height")
jane = Person("Jane", 25, 1.75)
# It's like updating tuple !!!
jane = jane._replace(age=26)  # jane = Person(name='Jane', age=26, height=1.75)
```
### _fields
Tuple of field names.  
```python
from collections import namedtuple
Person = namedtuple("Person", "name age height")
jane = Person("Jane", 25, 1.75)
f = Person._fields  # f = ('name', 'age', 'height')
f = jane._fields    # f = ('name', 'age', 'height')
```
### _field_defaults
```python
from collections import namedtuple
Developer = namedtuple("Developer",
                       "name level language",
                       defaults=["Junior", "Python"])
d = Developer._field_defaults  # d = {'level': 'Junior', 'language': 'Python'}
```

---

## namedtuple operations
### Iterating over fields and values:
```python
from collections import namedtuple
Nt = namedtuple('Nt','a b')
nt = Nt(1, 2)
# 1.
for field , value in zip(nt._fields, nt):
    ...
# 2.
for filed, value in nt._asdict().items():
    ...
```
### Conversions
**\_make()** - converting iterable to namedtuple  
**\_asdict()** - converting namedtuple to dict  
****kwargs** - converting dict to namedtuple  
### Subclassing namedtuple
```python
from collections import namedtuple
from datetime import date

BasePerson = namedtuple("BasePerson",
                        "name birthdate country",
                        defaults=["Canada"])

class Person(BasePerson):
    """A namedtuple subclass to hold a person's data."""
    __slots__ = ()  # prevents the automatic creation of a per-instance .__dict__
    def __repr__(self):
        return f"Name: {self.name}, age: {self.age} years old."
    @property
    def age(self):
        return (date.today() - self.birthdate).days // 365

# Person.__doc__ = "A namedtuple subclass to hold a person's data."
jane = Person("Jane", date(1996, 3, 5))
v = jane.age  # v = 25
v = jane      # v = Name: Jane, age: 25 years old.
```

---

## Namedtuples usage:
1. Using Field Names Instead of Indices
2. Returning Multiple Named Values From Functions
3. Reducing the Number of Arguments to Functions 
4. Reading tabular data from files(csv) or databases
5. If data is immutable use namedtuple over dict (less memory and faster)

---

## namedtuple vs ...
### @dataclass
Data classes are similar to namedtuples, but they’re mutable.  
Data Classes can be thought of as "mutable namedtuples with defaults."
```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    height: float
    weight: float
    country: str = "Canada"

jane = Person("Jane", 25, 1.75, 67)
# jane = Person(name='Jane', age=25, height=1.75, weight=67, country='Canada')
```
With @dataclass(frozen=True) dataclass is immutable
```python
@dataclass(frozen=True)
```
dataclasses aren't **iterable** !!! - add **\_\_iter\_\_** method 
```python
from dataclasses import astuple, dataclass

@dataclass
class Person:
    name: str
    age: int
    height: float
    weight: float
    country: str = "Canada"
    def __iter__(self):
        return iter(astuple(self))
```
dataclasses consume more memory - have per instance **\_\_dict\_\_**  
Performance (time) is similar.  
### typing.NamedTuple
It's typed version of namedtuple.  
It's immutable.
Both use same amount of memory.
Both subclasses of tuple.  
Performance (time) is similar.

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    height: float
    weight: float
    country: str = "Canada"
```

---
