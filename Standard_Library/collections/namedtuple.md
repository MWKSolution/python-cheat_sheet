# namedtuple()  
Function!  
Returns new subclass of **tuple** with named fields.  
Have similar memory consumption to regular tuples.  
Use to return multiple values from functions.  
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
## Methods inherited from tuples
+, len(), index(), count(), ...
## Named tuple methods and attributes  
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

__doc__ helpful docstring

conversions
make, asdict, **

vs @dataclass

Iterating over fields and values:
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

named tuples:
1. Using Field Names Instead of Indices
2. Returning Multiple Named Values From Functions
3. Reducing the Number of Arguments to Functions
