# Functools


1. [Functional programming](#functional-programming)  

Tools:  

2. [partial()](#partial)
3. [partialmethod()](#partialmethod)
4. [@lru_cache(), @cache](#lrucache-cache)
5. [@cached_property](#cachedproperty)
6. [@wraps, update_wrapper()](#wraps-updatewrapper)
7. [@total_ordering](#totalordering)
8. [@singledispatch](#singledispatch)
9. [@singledispatchmethod](#singledispatchmethod)  

Deprecated or non-pythonic:  

10. [reduce()](#reduce)
11. [cmp_to_key()](#cmptokey)  

---
## Functional programming
Recursion, pure functions, higher-order functions.  
Python:
- Functions as first-class objects
- Recursion capabilities
- Anonymous functions with lambda
- Iterators and generators
- Standard modules like functools and itertools
- Tools like map(), filter(), reduce(), sum(), len(), any(), all(), min(), max(), and so on
```python
import sys
x = sys.getrecursionlimit()  # x = 1000
```

---

## partial()
Return a new partial object which when called will behave like func called with the positional arguments and keyword arguments.    
```python
from functools import partial

def fun(a, b):
    return a ** b

pfun2 = partial(fun, b=2)
pfun2.__doc__ = 'Second power'
pfun3 = partial(fun, b=3)

v = pfun2(5)        # v = 25
x = pfun2.func      # x = <function fun at 0x...>
y = pfun2.args      # y = ()
z = pfun2.keywords  # z = {'b': 2}
t = pfun2.__doc__   # t = 'Second power'
m = pfun3.__doc__   # m = 'partial(func, *args, **keywords) - new function with partial application\n    of the given arguments and keywords.\n'
f = pfun3           # f = functools.partial(<function fun at 0x0000000002814280>, b=3
pfun3.__name__ = 'pow3'
```

---

## partialmethod()
Return a new partialmethod descriptor which behaves like partial except that it is ***designed to be used as a method definition rather than being directly callable***.  
Basic:
```python
from functools import partialmethod

class C:
    def __init__(self):
        self.a = 0
    def set_a(self, i):
        self.a = i
    set_10 = partialmethod(set_a, 10)
    set_99 = partialmethod(set_a, 99)

c = C()
v = c.a       # v =0
c.set_a(55)
w = c.a       # w = 55
c.set_10()
x = c.a       # x = 10
c.set_99()
y = c.a       # y = 99
z = c.set_10  # z = functools.partial(<bound method C.set_a of <__main__.C object at 0x0000000002819460>>, 10)
```
Advanced: (adding methods dynamically)
```python
from functools import partialmethod
from operator import mul

class C:
    def __init__(self, a):
        self.a = a

    def __mul(self, b):
        return mul(self.a, b)

    @classmethod
    def new_method(cls, b):
        setattr(cls, f'mul_{b}', partialmethod(cls.__mul, b))

c = C(2)
v = c.mul_10()    # AttributeError: 'C' object has no attribute 'mul_10'
C.new_method(10)
v = c.mul_10()    # v = 20
```

---

## @lru_cache, @cache
Least Recently Used cache.  
Other startegies:
- FIFO (first in first out)
- LIFO (last in first out)
- LRU
- MRU (most recently used)
- LFU (least frequently used)  

Function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.  
With function as argument:
```python
from functools import lru_cache

def factorial(n):
    print(f'{n}', end=', ')
    return n * factorial(n-1) if n else 1

factorial = lru_cache(factorial)
q = factorial(10)           # q = 3628800
print('<')
# output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, <
z = factorial.cache_info()  # z = CacheInfo(hits=0, misses=11, maxsize=128, currsize=11)
m = factorial(15)           # m = 1307674368000
print('<') 
# output: 15, 14, 13, 12, 11, <
x = factorial.cache_info()  # x = CacheInfo(hits=1, misses=16, maxsize=128, currsize=16)
o = factorial.__wrapped__   # o = <function factorial at 0x...>
p = factorial               # p = <functools._lru_cache_wrapper object at 0x...>
```
As a decorator:
```python
from functools import lru_cache

@lru_cache(maxsize=10)
def fibonacci(n):
    print(n, end=', ')
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

v = fibonacci.cache_info()  # v = CacheInfo(hits=0, misses=0, maxsize=10, currsize=0)
x = fibonacci(10)           # x = 55
print('<')
# output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, <
w = fibonacci.cache_info()  # w = CacheInfo(hits=8, misses=11, maxsize=10, currsize
y = fibonacci(5)            # y = 5
print('<')
# output: <
z = fibonacci.cache_info()  # z = CacheInfo(hits=9, misses=11, maxsize=10, currsize=10)
k = fibonacci(20)           # k = 6765
print('<')
# output: 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, <
o = fibonacci.cache_info()  # o = CacheInfo(hits=20, misses=21, maxsize=10, currsize=10)
p = fibonacci(4)            # p =3
print('<')
# output: 4, 3, 2, 1, 0, <
g = fibonacci.cache_info()  # g = CacheInfo(hits=22, misses=26, maxsize=10, currsize=10)
fibonacci.cache_clear()
e = fibonacci.cache_info()  # e = CacheInfo(hits=0, misses=0, maxsize=10, currsize=0)
# in Pyton 3.9:
fibonacci.cache_parameters() # - returns maxsize and typed
```
Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.
- If *maxsize* (default is 128) is set to None, the LRU feature is disabled and the cache can grow without bound.
- If *typed* is set to true, function arguments of different types will be cached separately.
- The original underlying function is accessible through the *\_\_wrapped\_\_* attribute.
Timed lru cashe:
```python
from functools import lru_cache, wraps
from datetime import datetime, timedelta

def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache
```
New in Python 3.9
```python
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
```
Simple lightweight unbounded function cache.   
Returns the same as *lru_cache(maxsize=None)*. Because it never needs to evict old values, this is smaller and faster than lru_cache() with a size limit.


---

## @cached_property
Transform a method of a class into a property whose value is computed once and then cached as a normal attribute for the life of the instance.  
There are differences between @property and @cached_property - check documentation...  
Unlike property(), cached_property() doesn’t block attribute mutations unless you provide a proper setter method. 
```python
from functools import cached_property
import statistics
class DataSet:

    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)
```
Cached property that doesn’t allow modification:
```python
from functools import lru_cache
import statistics
class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = sequence_of_numbers

    @property
    @lru_cache  # or @cache from 3.9
    def stdev(self):
        return statistics.stdev(self._data)
```

---

## @wraps, update_wrapper()
Preserve information about the original function.  By default, preserved attributes: 
**\_\_module\_\_, \_\_name\_\_, \_\_qualname\_\_, \_\_annotations\_\_, \_\_doc\_\_, \_\_dict\_\_**.   
Only decorator:
```python
def decorator(func):

    def wrapper(*args, **kwargs):
        """I'm wrapper"""
        print(f'Decorating {args} + {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@decorator
def fun(a, b):
    """I'm fun."""
    print('This is some function')
    return a + b

v = fun(1, b=2)

w = fun.__name__     # w = 'wrapper'
z = fun.__doc__      # z = "I'm wrapper"
m = fun.__wrapped__  # 'function' object has no attribute '__wrapped__'
```
With **@wraps**:
```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """I'm wrapper"""
        print(f'Decorating {args} + {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@decorator
def fun(a, b):
    """I'm fun."""
    print('This is some function')
    return a + b

v = fun(1, b=2)

w = fun.__name__     # w = 'fun'
z = fun.__doc__      # z = "I'm fun."
m = fun.__wrapped__  # m = <function fun at 0x...>
```
Actually **@wraps** is invoking **update_wrapper()** and is equivalent to calling:  
**partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)(func)**  
By default:  *assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES*  
Previous example with **update_wrapper()** would look like this:
```python
from functools import update_wrapper

def decorator(func):

    def wrapper(*args, **kwargs):
        """I'm wrapper"""
        print(f'Decorating {args} + {kwargs}')
        return func(*args, **kwargs)
    
    update_wrapper(wrapper, func)
    
    return wrapper

@decorator
def fun(a, b):
    """I'm fun."""
    print('This is some function')
    return a + b

v = fun(1, b=2)

w = fun.__name__     # w = 'fun'
z = fun.__doc__      # z = "I'm fun."
m = fun.__wrapped__  # m = <function fun at 0x...>
```

---

## @total_ordering
Given a class defining one or more rich comparison ordering methods, this class decorator supplies the rest.  
The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). In addition, the class should supply an __eq__() method.  
```python
from functools import total_ordering

@total_ordering
class StrangeNumber:
    def __init__(self, number):
        self.number = number
    def __repr__(self):
        return f'{type(self).__name__}({self.number})'
    def __lt__(self, other):
        return self.strange(self.number) < self.strange(other.number)
    def __eq__(self, other):
        return self.strange(self.number) == self.strange(other.number)
    @staticmethod
    def strange(n):
        return float("".join(reversed(str(n))))

x = StrangeNumber(12345.56)    # x = StrangeNumber(12345.56)
y = StrangeNumber(13.3333333)  # y = StrangeNumber(13.3333333)
z = (x >= y)                   # z = False
k = max(x, y)                  # k = StrangeNumber(13.3333333)
```
While this decorator makes it easy to create well behaved totally ordered types, it does come at the cost of slower execution and more complex stack traces for the derived comparison methods. If performance benchmarking indicates this is a bottleneck for a given application, implementing all six rich comparison methods instead is likely to provide an easy speed boost.  
This decorator makes no attempt to override methods that have been declared in the class or its superclasses. Meaning that if a superclass defines a comparison operator, total_ordering will not implement it again, even if the original method is abstract.  

---

## @singledispatch
Function overloading. Transform a function into a single-dispatch generic function.  
The original function decorated with @singledispatch is registered for the base object type,
```python
from functools import singledispatch

@singledispatch
def fun(arg):
    return 'No implementations for this argument type!'

@fun.register
def _(arg: list):
    return list(enumerate(arg))

@fun.register(float)
@fun.register(int)
def _(arg):
    return arg*5

fun.register(str, lambda x: x.upper())

@fun.register
def _(arg: type(None)):
    return 'Nothing'

v = fun(1+1j)             # v = 'No implementations for this argument type!'
w = fun(10.5)             # w = 52.5
u = fun('txt')            # u = 'TXT'
x = fun(['a', 'b', 'c'])  # x = [(0, 'a'), (1, 'b'), (2, 'c')]
y = fun(None)             # y = 'Nothing'

o = fun.dispatch(int)     # o = <function _ at 0x...> == fun.registry[int]
p = fun.registry.keys()   # p = dict_keys([<class 'object'>, <class 'list'>, <class 'int'>, <class 'float'>, <class 'str'>, <class 'NoneType'>])
```
More than one argument:  
```python
from functools import singledispatch

@singledispatch
def fun(arg1, arg2):
    return 'No implementations for this argument type!'

@fun.register
def fun_int(arg1: int, arg2: int):
    return arg1 + arg2

@fun.register(float)
def fun_float(arg1, arg2):
    return arg1 - arg2

z = fun('a', 5)           # z = 'No implementations for this argument type!'
v = fun(1, 1)             # v = 2
w = fun(1.5, 1.5)         # w = 0.0

o = fun.dispatch(int)     # o = <function _int at 0x...> == fun.registry[int]
p = fun.registry.values() # p = dict_values([<function fun at 0x...>, <function fun_int at 0x...>, <function fun_float at 0x...>])
```
If an implementation is registered to an abstract base class, virtual subclasses of the base class will be dispatched to that implementation.  

---

## @singledispatchmethod
Like @singledipatch but for methods in class.  
Transform a method into a single-dispatch generic function.  
```python
from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg

n = Negator()
v = n.neg(1)        # v = -1
w = n.neg(True)     # w = False
# z = n.neg('abc')  # NotImplementedError: Cannot negate a
```
Add multiple constructors to your classes and run them selectively, according to the type of their first argument.  
```python
from functools import singledispatchmethod

class C:
    @singledispatchmethod
    def __init__(self, arg):
        raise NotImplementedError
    @__init__.register(int)
    def from_int(self, arg):
        self.n = arg
    @__init__.register(float)
    def from_float(self, arg):
        self.n = int(arg)

n1 = C(1)
v = n1.n        # v = 1
n2 = C(1.5)
w = n2.n        # w = 1
# x = C('aaa')  # NotImplementedError
```
@singledispatchmethod supports nesting with other decorators such as @classmethod...  
... but there is bug before Python 3.9.8 - need to be tweeked
```python
from functools import singledispatchmethod
# tweek:
def _register(self, cls, method=None):
    if hasattr(cls, '__func__'):
        setattr(cls, '__annotations__', cls.__func__.__annotations__)
    return self.dispatcher.register(cls, func=method)
singledispatchmethod.register = _register

class Negator:
    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    @classmethod
    def neg_int(cls, arg: int):
        return -arg

    @neg.register
    @classmethod
    def neg_bool(cls, arg: bool):
        return not arg


v = Negator.neg(1)     # v = -1
w = Negator.neg(True)  # w = False
```

---

## reduce()
Reduce the iterable to a single value.  
```python
from functools import reduce
l = [0, 1, 2, 3]
rl = reduce(lambda x, y: x+y, l, 100)  # rl = 106, rl = ((((100 + 0) + 1 ) + 2 ) + 3) 
```
reduce() perform better than for loop but for loop is more readable.
still slower than built-in functions.  
reduce() is not considered pythonic.  
1. Use a dedicated function to solve use cases for Python’s reduce() whenever possible. (sum(), all(), any(), max(), min(), len(), ...)  
2. Avoid complex user-defined functions when using reduce()  
3. Avoid complex lambda functions when using reduce()  

---

## cmp_to_key()
Transform an old-style comparison function (returns -1, 0, 1) to a key function.  
This function is primarily used as a transition tool for programs being converted from Python 2 which supported the use of comparison functions.  

