# Decorator
1. Inner function and enclosing scope
2. Closure
3. Decorator
4. Parameters and return
5. Introspection
6. Chaining decorators

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

---

## Chaining decorators
