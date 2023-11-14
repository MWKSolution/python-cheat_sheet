# typing

<!-- TOC -->
* [typing](#typing)
  * [Brief](#brief)
  * [Simple types](#simple-types)
  * [Any type](#any-type)
  * [types](#types)
  * [collections.abc module](#collectionsabc-module)
  * [Variable hint](#variable-hint)
  * [Functions](#functions)
  * [Alias, NewType](#alias-newtype)
  * [Class as Type](#class-as-type)
  * [Decorator](#decorator)
  * [Generic type](#generic-type)
  * [types module](#types-module)
  * [Stub files](#stub-files)
  * [MyPy](#mypy)
  * [Pydantic, MyPy](#pydantic-mypy)
<!-- TOC -->
---

## Brief

Not usefull for short personal scripts  
type hints should be used whenever unit tests are worth writing  
type hinst are stored in __annotations __  
[hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

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

## types

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
IO[str]
IO[bytes]
```
All:
```python
Annotated
Any
AnyStr
BinaryIO
ChainMap
ClassVar
Counter
DefaultDict
Deque
Dict
Final
FrozenSet
Generic
IO
List
Literal
Match
NamedTuple
NewType
NoReturn
Optional
OrderedDict
Pattern
Protocol
Set
Self
Text
TextIO
Tuple
Type
TypeVar
TypedDict
Union
```
plus types defined in collections. abc
## collections.abc module
```python
Iterable 
Container 
Sized 
Callable 
Hashable
Buffer 
Awaitable
AsyncIterable 

Iterator 
Reversible 
Collection 
Coroutine 
AsyncIterator 

Generator 
Sequence
Mapping 
Set 
MappingView 
AsyncGenerator 

MutableSequence 
MutableMapping 
MutableSet 
KeysView 
ItemsView 
ValuesView 
ByteString 
```

[collections.abc - abstract base classes](../Standard_Library/collections/abc.md)

## Variable hint
```python
a: int
b: str = 'xxx'
```

## Functions

```python
from typing import Union, Optional, ...
None             # if function doesn't return a value use -> None !!!! __init__()
Union[int, str]  # variable/argument is int or str
Optional[int]    # variable/argument is int or None
Callable[[<arguments>], <output>]  # for functons as arguments
Iterator # could be used for generator
NoReturn         # for functions that never return
None
```

## Alias, NewType
```python
from typing import Tuple, NewType
MyNewType1 = Tuple[str, ...]  # new type as tuple of some strings
MyNewType3 = NewType('MyNewType3', Tuple[str, ...])
```

## Class as Type
```python
# Just use class Name.  
var: ClassVar[int] = 1  # class variable
```
When not defined use string literal:
```python
class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> "Deck":
```
or:
```python
from __future__ import annotations

class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> Deck:
```
or use:
```python
T = TypeVar('T')
```
## Decorator
```python
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])
def bare_decorator(func: F) -> F:
    ...
def decorator_args(url: str) -> Callable[[F], F]:
    ...
```

## Generic type
Better than Any:
```python
T = TypeVar('T')
```
limitin generic type:
```python
T = TypeVar("T", str, int) # T can only represent types of int and st
T = TypeVar("T", bound=int) # T can only be an int or subtype of int
```
Generic class:
```python
T = TypeVar("T")

class SomeClass(Generic[T]):  
    # After instantiation that instance will only accept arguments of that type...
    ...

instance1 = SomeClass[str]
instance2 = SomeClass[int]
```

## types module
Names for some object types that are used by the standard Python interpreter, but not exposed as builtins like **int** or **str** are.
```python
AsyncGeneratorType
BuiltinFunctionType
BuiltinMethodType
CellType
ClassMethodDescriptorType
CodeType
CoroutineType
DynamicClassAttribute
FrameType
FunctionType
GeneratorType
GenericAlias
GetSetDescriptorType
LambdaType
MappingProxyType
MemberDescriptorType
MethodDescriptorType
MethodType
MethodWrapperType
ModuleType
SimpleNamespace
TracebackType
WrapperDescriptorType
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

## Pydantic, MyPy

Checking type hints at runtime.    

[mypy](https://mypy.readthedocs.io/en/stable/index.html)  
[medium](https://medium.com/@steveYeah/using-generics-in-python-99010e5056eb)


---



