# dataclasses

---

## Defining  
```python
from dataclasses import dataclass

@dataclass
class DC:
    x: int = 5
    s: str = 'abc'  # variables with default should be at the end

dc = DC()

dc.x = 7
dc.s = 'ABC'
```
Auto added methods:
```python
__init__()
__repr__()
__eq__()    # == operator can be used
```
Arguments of the decorator:
```python
@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
           match_args=True, kw_only=False, slots=False, weakref_slot=False)
```

## Methods
```python
from dataclasses import astuple, asdict, field
asdict(dc)   # return as dict
astuple(dc)  # retuern as tuple
fields(dc)   # return detailed info about fileds
field(default=MISSING, default_factory=MISSING, init=True, repr=True,
      hash=None, compare=True, metadata=None, kw_only=MISSING)  # default behaviour of vars
      # x: int = 0 is equivalent to x: int = field(default=0)
      # compare = include in comparisons
      # metadata - additional information: metadata={'unit': 'meter'}
      # default_factory - for mutable default values
make_dataclass(...)
repalce(...)
is_dataclass(...)
```
## Immutable dataclass
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class DC:
    x: int = 5
    s: str = 'abc'  # variables with default should be at the end

dc = DC()
```

## post init
```python
from dataclasses import dataclass, field

@dataclass
class DC:
    x: int = 5
    s: str = 'abc'
    z: str = field(init=False)
    
    def __post_init__(self):
        self.z = self.s*self.x
        
dc = DC()  # dc.z = 'abcabcabcabcabc'
```

## Order and sorting
```python
from dataclasses import dataclass, field

@dataclass(order=True)
class DC:
    x: int = 0
    s: str = ''  
    sort_index: int = field(init=False)

    def __post_init__(self):
        self.sort_index = len(self.s) * self.x

dc1 = DC(3, 'xx')
dc2 = DC(1, 'aaa')
b = dc1 > dc2  # b=True
```

# default_factory
```python
from random import randint, choices
from string import ascii_letters
from functools import partial
from dataclasses import dataclass, field, astuple

def randstr(n=3):
    return ''.join(choices(ascii_letters, k=n))

@dataclass(frozen=True)
class DC:
    x: int = field(default_factory=partial(randint, 0, 100))
    s: str = field(default_factory=partial(randstr, 10))


dc1 = astuple(DC())  # (69, 'MuIQUChATG')
dc2 = astuple(DC())  # (48, 'eqshlSKpqJ')
```

## slots
faster and less memory (no __dict __ and __weakref __):
```python
from dataclasses import dataclass, field, astuple
@dataclass
class DC:
    __slots__ = ['x', 's']
    x: int
    s: str

dc = DC(1, 'a')
```
## Alternatives
```python
namedtuple
typing.NamedTuple
```
