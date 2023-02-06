# typing


---

## Brief

Not usefull for short personal scripts  
type hints should be used whenever unit tests are worth writing  
type hinst are stored in __annotations __

## Simple types

```python
int     # integer
float   # floating point number
bool    # boolean value (subclass of int)
str     # text, sequence of unicode codepoints
bytes   # 8-bit string, sequence of byte values
object  # an arbitrary object (object is the common base class)
```

## Any type

```python
Any  # dynamically typed value with an arbitrary type
```

## Generic types

```python
from typing import List, Tuple, ...
List[str]         # list of str objects
Tuple[int, int]   # tuple of two int objects (Tuple[()] is the empty tuple)
Tuple[int, ...]   # tuple of an arbitrary number of int objects
Dict[str, int]    # dictionary from str keys to int values
Iterable[int]     # iterable object containing ints
Sequence[bool]    # sequence of booleans (read-only)
Mapping[str, int] # mapping from str keys to int values (read-only)
Type[C]           # type object of C (C is a class/type variable/union of types)
Sequence[int]     # any sequence: list, tuple, ... (anything supporting len() and __getitem __()
```

## Functions

```python
from typing import Union, Optional, ...
None             # if function doesn't return a value use -> None !!!! __init__()
Union[int, str]  # variable/argument is int or str
Optional[int]    # variable/argument is int or None
Callable[[<arguments>], <output>]  # for functons as arguments
NoReturn         # for functions that never return
```

## Aliases and stuff...
```python
from typing import Tuple, TypeVar, NewType
MyNewType1 = Tuple[str, ...]  # new type as tuple of some strings
MyNewType2 = TypeVar('MyNewType2', str, int)
MyNewType3 = NewType('MyNewType3', Tuple[str, ...])
```

## Protocols
[Predefined protocol reference](https://mypy.readthedocs.io/en/stable/protocols.html#predefined-protocol-reference)  

## Class as Type

Just use class Name.  
When not fully defined use string literal or :
```python
from __future__ import annotations
```

## Stub files

 A stub file is a text file that contains the signatures of methods and functions, but not their implementations. Their main function is to add type hints to code that you for some reason can’t change.  


## MyPy
Use "TYPE_CHECKING" if you want to have code that mypy can see but will not be executed at runtime
```python
if TYPE_CHECKING:
    print('Seen by MyPy but not executed')
else:
    print('Executed but not seen by MyPy')
```

## Pydantic

Checking type hints at runtime.  

---



