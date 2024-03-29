# Decorator
1. [Inner function and enclosing scope](#inner-function-and-enclosing-scope)
2. [Closure](#closure)
3. [Decorator](#decorator)
4. [Parameters and return](#parameters-and-return)
5. [Introspection](#introspection)
6. [Chaining decorators](#chaining-decorators)
7. [Decorator without wrapper](#decorator-without-wrapper)
8. [Decorators with arguments](#decorators-with-arguments)
9. [Decorating classes](#decorating-classes)
10. [Classes as decorators](#classes-as-decorators)
11. [Decorators with state](#decorators-with-state)

---

## Inner function and enclosing scope
- Inner (nested) function has enclosing scope which is local for enclosing function.    
- Variables in enclosing scope are read-only. Assigning value to enclosing-scope variable creates new local-scope variable. This variable is still present as local in enclosing function scope or...  
- ...you can use **nonlocal** kyeword to change variable in enclosing scope.  

```python
def enclosing_function(arg):

    def inner_function():
        print(f'From enclosing scope: {arg}')

    print(f'From local scope: {arg}')
    inner_function()

enclosing_function('abc')
# output: From local scope: abc
#         From enclosing scope: abc
```

---

## Closure
- We must have a inner(nested) function (function inside a function).
- The nested function must refer to a value defined in the enclosing function.
- The enclosing function must return the nested function. *<- this is new*
```python
def enclosing_function(arg):

    def inner_function():
        print(f'From enclosing scope: {arg}')

    return inner_function

fun = enclosing_function('abc')
fun()
# it returned inner function, enclosing function can be deleted !!!
del enclosing_function
fun()
# Output: From enclosing scope: abc
#         From enclosing scope: abc
```
Closure usage:
- avoiding usage of global variables (encapsulation)
- if one(few) method - use closure over class
- decorators

Every function has **\_\_closure\_\_** attribute. It is tuple of variables from enclosing scope.  
```python
def enclosing_function(arg):
    x = 5
    def inner_function():
        print(f'From enclosing scope: {arg}')
        print(f'From enclosing scope: {x}')

    return inner_function

fun = enclosing_function('abc')

v = enclosing_function.__closure__    # v = None
w = fun.__closure__                   # w = (<cell at 0x...: str object at 0x000000000042FB70>, <cell at 0x...: int object at 0x000007FED2631790>)

z = fun.__closure__[0].cell_contents  # z = 'abc'
t = fun.__closure__[1].cell_contents  # t = 5
```

---

## Decorator
Closure with function as argument is a decorator.  
Decorator wraps a function, modifying its behavior.  
```python
def decorator(func):
    def wrapper():
        print('Decorating before')
        func()
        print('Decorating after')
    return wrapper

def fun():
    print('This is some function')

fun()
fun = decorator(fun)  # decorating function
fun()
# Output: This is some function
#         Decorating before
#         This is some function
#         Decorating after
```
With @ syntax:
```python
def decorator(func):
    def wrapper():
        print('Decorating before')
        func()
        print('Decorating after')
    return wrapper

@decorator
def fun():
    print('This is some function')

fun()
# Output: Decorating before
#         This is some function
#         Decorating after
```
**!!! IMPORTANT !!!**  
Actually @ syntax:
```python
@decorator
def fun():
    pass
```
means:
```python
fun = decorator(fun)
```
Which is changing assignment to *fun* (now *wrapper* is assigned). But now every call to *fun* will run *wrapper* and *fun* inside it. Which is actual functionality of decorator.  
Possible is:  
```python
something = decorator(fun)
```
*something* function will be decorated *fun* function. But this will not alter behavior of *fun* after calls to *fun* !!!  
See also **Decorator without wrapper**

---

## Parameters and return
Decorating functions with parameters and returning values from decorated functions.
```python
def decorator(func):
    def wrapper(a, b):                 # same parameters as decorated function !
        print(f'Decorating {a} + {b}')
        return func(a, b)              # wrapper returns function call with parameters !
    return wrapper

@decorator
def fun(a, b):
    print('This is some function')
    return a + b

v = fun(1, 2)  # v =3
# Output: Decorating 1 + 2
#         This is some function

```
More general case
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print('Decorating')
        return func(*args, **kwargs)
    return wrapper

@decorator
def fun(a, b):
    print('This is some function')
    return a + b

v = fun(1, 2)  # v = 3
# Output: Decorating
#         This is some function
```
---

## Introspection
Preserve information about the original function.  By default, preserved attributes: 
**\_\_module\_\_, \_\_name\_\_, \_\_qualname\_\_, \_\_annotations\_\_, \_\_doc\_\_, \_\_dict\_\_**.  
See [@wraps](functools.md)  
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

---

## Chaining decorators
```python
from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """I'm wrapper1"""
        print(f'Decorator1 >>>>> {args} + {kwargs}')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """I'm wrapper2"""
        print(f'Decorator2 ##### {args} + {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def fun(a, b):
    """I'm fun."""
    print('This is some function')
    return a + b

v = fun(1, b=2)
# Output: Decorator1 >>>>> (1,) + {'b': 2}
#         Decorator2 ##### (1,) + {'b': 2}
#         This is some function
```

---

## Decorator without wrapper
**!!! IMPORTANT !!!**  
**Wrapper is needed for three things:**
- **to get access to arguments of decorated function**
- **to actually run decorated function inside wrapper**
- **to use decorator with arguments - additional wrapper**
```python
PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def func1():
    pass

@register
def func2():
    pass

def fun3():
    pass

fun3 = register(fun3)

v = PLUGINS  # v = {'func1': <function func1 at 0x...>, 'func2': <function func2 at 0x... >, 'fun3': <function fun3 at 0x...}
```

---

## Decorators with arguments
Additional wrapper for decorator arguments. Argument must be given or "()" if default value is defined.  
```python
from functools import wraps

def decorator_arg(n):
    def decorator(func):
        @wraps(func)
        def wrapper(a, b):
            print(f'Decorating ({a} + {b}) * {n}')
            return func(a, b) * n
        return wrapper
    return decorator

@ decorator_arg(n=5)
def fun(a, b):
    print('This is some function')
    return a + b

v = fun(1, 2)  # v = 15
# Output: Decorating (1 + 2) * 5
#         This is some function
```
Using decorator with or without arguments.  
!!! But parameters should be all keywords arguments !!!  
Two wrappers as above:
```python
from functools import wraps, partial

def decorator_arg(func=None, *, n=2):  # when no parameters func is passed as first argument !!!
    def decorator(func):
        @wraps(func)
        def wrapper(a, b):
            print(f'Decorating ({a} + {b}) * {n}')
            return func(a, b) * n
        return wrapper
    if func is None:
        return decorator
    else:
        return decorator(func)

@decorator_arg
def fun(a, b):
    print('This is some function')
    return a + b

v = fun(1, 2)  # v = 6
```
One wrapper with **partial()**  
```python
from functools import wraps, partial

def decorator(func=None, *, n=2):
    if func is None:
        return partial(decorator, n=n)
    @wraps(func)
    def wrapper(a, b):
        print(f'Decorating ({a} + {b}) * {n}')
        return func(a, b) * n
    return wrapper

@decorator()
def fun(a, b):
    print('This is some function')
    return a + b

v = fun(1, 2)  # v = 6
```
Can be used like:
```python
@decorator
@decorator()
@decorator(n=10)
```

---

## Decorating classes
Decorating methods:  
**@classmethod**, **@staticmethod**, **@property**.   
As for ordinary function...  

Decorating class:  
**@dataclass**  
Simpler alternative of metaclasses.  
Changing class definition dynamically.  
Decorator receives class.  
1. decorating all instances at once:
```python
def class_decorator(Cls):
    class NewCls(Cls):
        def __init__(self, *args, **kwargs):
            print('Decorating class')
            self.oInstance = Cls(*args, **kwargs)
        def __getattribute__(self,s):
            x = super(NewCls,self).__getattribute__(s)
            print('Decorating method')
            return x
    return NewCls

@class_decorator
class C:
    def m1(self):
        print('Method 1')

    def m2(self):
        print('Method 2')

c = C()
c.m1()
c.m2()
# Output: 
# Decorating class
# Decorating method
# Method 1
# Decorating method
# Method 2
```
Singelton:
```python
from functools import wraps

def singleton(cls):
    @wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None    # wrapper keeps state if class has instance
    return wrapper_singleton

@singleton
class C:
    pass

c1 = C()
c2 = C()

v = c1 is c2  # v = True
```

---

## Classes as decorators
**\_\_init\_\_** in class gets function as an argument.  
Also class should be callable - **\_\_call\_\_** method.  
```python
from functools import update_wrapper

class Decorator:
    def __init__(self, func):
        update_wrapper(self, func)  # instead of wraps
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'Function {self.func.__name__} called {self.calls} time(s).')
        return self.func(*args, **kwargs)

@Decorator   # crating instance of Decorator: fun = Decorator(fun)
def fun():
    print("I'm function")
    return None

fun()
fun()
# Output:
# Function fun called 1 time(s).
# I'm function
# Function fun called 2 time(s).
# I'm function
```

---

## Decorators with state
Class decorator from previous example is an example of stateful decorator.  
Since it changes fun in instance of Decorator it is able to keep state throughout all calls to fun().  

Classic stateful decorator:  
```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.func_calls += 1
        print(f'Function {func.__name__} called {wrapper.func_calls} time(s).')
        return func(*args, **kwargs)
    wrapper.func_calls = 0
    return wrapper

@decorator
def fun():
    print("I'm function")

fun()
fun()
# Output:
# Function fun called 1 time(s).
# I'm function
# Function fun called 2 time(s).
# I'm function
```

---

