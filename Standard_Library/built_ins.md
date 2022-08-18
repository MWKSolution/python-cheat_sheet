# Built-in Functions

1. [Builtins module](built_ins.md)
2. [Boolean](built_ins/boolean.md)
   1. **all()**
   2. **any()**
   3. **bool()**
3. [General](#General)
   1. len()
   2. max()
   3. min()
   4. slice()
4. [Scope](built_ins/scope.md)
   1. dir()
   2. globals()
   3. locals()
   4. vars()
5. [Iterators](built_ins/iterators.md)
   1. **enumerate()**
   2. filter()
   3. map()
   4. iter()
   5. next()
   6. **range()**
   7. **zip()**
   8. **reversed()**
   9. **sorted()**
6. [Math](#Math)
   1. abs()
   2. bin()
   3. complex()
   4. divmode()
   5. hex()
   6. float()
   7. int()
   8. oct()
   9. pow(), **
   10. round()
   11. sum()
7. [Strings](#Strings)
   1. ascii()
   2. chr()
   3. format()
   4. input()
   5. ord()
   6. print()
   7. str()
8. [Objects](built_ins/objects.md)
   1. **object()**
   2. **id()**
   3. **type()**
   4. **repr()**
   5. **hash()**
   6. **setattr()**
   7. **delattr()**
   8. **getattr()**
   9. **hasattr()**
   10. **isinstance()**
   11. **issubclass()**
   12. **callable()**
9. [Class](#Class)
   1. @classmethod
   2. property(), @property
   3. @staticmethod
   4. super()
10. [Files](#Files)
    1. open()
11. [Code](#Code)
    1. breakpoint()
    2. compile()
    3. eval()
    4. exec()
    5. help()
    6. \_\_import\_\_
12. [Creating variables](built_ins.md)
    1. **bytearray()**
    2. **bytes()**
    3. **dict()**
    4. **frozenset()**
    5. **list()**
    6. **set()**
    7. **tuple()**
    8. **memoryview()**





---
## builtins module

This module is not normally accessed explicitly by most applications, but can be useful in modules that provide objects with the same name as a built-in value.  
most modules have the name **\_\_builtins\_\_** made available as part of their globals. The value of **\_\_builtins\_\_** is normally either this module or the value of this module’s **\_\_dict\_\_** attribute.  

---

## Creating variables
Functions that creates new: **bytearray()**, **bytes()**, **dict()**, **frozenset()**, **list()**, **set()**, **tuple()**, **memoryview()**.  

---


## Math  

### abs()
### bin()
### complex()
### divmode()
### hex()
### float()
### int()
### oct()
### pow(), **
### round()
### sum()

---

## Strings  

### ascii()
### chr()
### format()
### input()
### ord()
### print()
### str()

---

## General
### len()
### max()
### min()
### slice()

---

## Class
### @classmethod
### property(), @property
### @staticmethod
### super()

---

## Files
### Open

---

## Code
### breakpoint()
### compile()
### eval()
### exec()
### help()
### \_\_import\_\_

---


