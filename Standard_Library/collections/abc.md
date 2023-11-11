# collections.abc - Abstract Base Classes for Containers  

This module provides abstract base classes that can be used to test whether a class provides a particular interface. 
Can be used with **\_\_issubclass()__** or **\_\_isinstance()__** to test object:
```python
issubclass(C, Sequence)
isinstance(C(), Sequence)
```
Could be registered instead of inherit  

**Abstract methods** should be implemented, *Mixin methods* are optional:

**Base:**
- Iterable : **\_\_iter__**
- Container : **\_\_contains__**  
- Sized : **\_\_len__**  
- Callable : **\_\_call__**  
- Hashable : **\_\_hash__**
- Buffer : **\_\_buffer__**
- Awaitable : **\_\_await__**
- AsyncIterable : **\_\_aiter__**

**Derived 1st level:**
- Iterator <- Iterable : **\_\_next__**, *\_\_iter__*
- Reversible <- Iterable : **\_\_reversed__**
- Collection <- Iterable : Container, Sized : **\_\_contains__, \_\_iter__, \_\_len__**, 
- Coroutine <- Awaitable : **send, throw**, *close*
- AsyncIterator <- AsyncIterable : **asend, athrow**, *aclose, \_\_aiter__, \_\_anext__*

**Derived 2nd level:**
- Generator <- Iterator : ...
- Sequence <- Collection, Reversible : ...
- Mapping <- Collection : ...
- Set <- Collection : ...
- MappingView <- Sized : ...
- AsyncGenerator <- AsyncItertor : ...

**Derived 3rd level:**
- MutableSequence <- Sequence : ...
- MutableMapping <- Mapping : ...
- MutableSet <- Set : ...
- KeysView <- Set, MappingView : ...
- ItemsView <- Set, MappingView : ...
- ValuesView <- MappingView, Collection : ...
- ByteString <- Sequence : ...

[Abstract Base Classes - docs.python...](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes)  

	