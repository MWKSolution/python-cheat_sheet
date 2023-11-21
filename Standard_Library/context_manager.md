# Context manager
1. [Brief]()
2. [**With** statement]()
3. [Custom context manager]()
   1. **\_\_enter\_\_**, **\_\_exit\_\_**
   2. Handling exceptions
4. [Context manager with generator (@contextmanager)]()
5. async with
6. Asynchronous context manager
---

## Brief
1. External resources management (files, locks)
2. Allows reusing the code that automatically manages the setup and teardown phases of a given operation  
3. Encapsulates standard uses of try ... finally statements in context managers

---

## With statement
Using existing context managers.  
Supports multiple context managers.  
```python
with open("hello.txt", mode="w") as file:
    file.write("Hello, World!")
# equivalent to: 
file = open("hello.txt", mode="w")
with file:
    file.write("Hello, World!")
# multiple:
with open("input.txt") as in_file, open("output.txt", "w") as out_file:
    ...
```

---

## Custom context manager
### **\_\_enter\_\_**, **\_\_exit\_\_**
```python
class ContextManager:
    def __init__(self):
        pass
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"  # return value bounded to target variable (after 'with ... as' expression)
    def __exit__(self, exc_type, exc_value, exc_tb):  # can use: __exit__(self, *args, **kwargs):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep=" , ")  # if no errors all 3 set to None
        # return True  # - if True is returned any errors are suppressed

with ContextManager() as hello:  # remember to put: () !!!
    print(hello)
# Output:
# Entering the context...
# Hello, World!
# Leaving the context...
# None , None , None
```
### Handling exceptions
For previously defined context manager:
```python
with ContextManager() as hello:
    print(hello)
    hello[100]
# Output:
# Entering the context...
# Hello, World!
# Leaving the context...
# <class 'IndexError'> , string index out of range , <traceback object at 0x...>
# ...
# IndexError: string index out of range
```
To handle this:
```python
class ContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type.__name__}")
            print(f"Exception message: {exc_value}")
            return True # must return True to suppress exceptions !!!!

with ContextManager() as hello:  # remember to put: () !!!
    print(hello)
    hello[100]
print("Continue normally from here...")
# Output:
# Entering the context...
# Hello, World!
# Leaving the context...
# An exception occurred in your with block: IndexError
# Exception message: string index out of range
# Continue normally from here...
```
!!!! **\_\_exit\_\_** must return True to suppress exceptions !!!!  
**\_\_enter\_\_** could return **None** !:  
```python
import sys

class RedirectedStdout:
    def __init__(self, new_output):
        self.new_output = new_output
    def __enter__(self):
        self.saved_output = sys.stdout
        sys.stdout = self.new_output
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.saved_output
```

---

## Context manager with generator (@contextmanager)
This function is a decorator that can be used to define a factory function for with statement context managers, without needing to create a class or separate __enter__() and __exit__() methods.  
```python
from contextlib import contextmanager

@contextmanager
def context_manager():
    print("Entering the context...")     # __enter__
    try:                                 
        yield "Hello, World!"            # __enter__ return
    finally:
        print("Leaving the context...")  # __exit__

with context_manager() as hello:
    print(hello)
# Output:
# Entering the context...
# Hello, World!
# Leaving the context..
```
Same with error handling
```python
from contextlib import contextmanager

@contextmanager
def context_manager():
    print("Entering the context...")
    try:
        raise TypeError
        yield "Hello, World!"
    except TypeError:
        yield 'Error'
    finally:
        print("Leaving the context...")

with context_manager() as hello:
    print(hello)
# Output:
# Entering the context...
# Error
# Leaving the context...
```
---

## async with
Asynchronous version   
...  
## Asynchronous context manager
**\_\_aenter\_\_()** and **\_\_aexit\_\_()**  
...  
