# Scope
1. globals(), locals()
2. vars(), dir()

---

Python scope determines where in your program a name is visible.  
Python scopes are implemented as dictionaries that map names to objects. These dictionaries are commonly called namespaces.  
They’re stored in a special attribute called **\_\_dict\_\_.**
Resolving names (LEGB rule) through scopes:
1. **Local** / function (functions, **lambda**)
2. **Enclosing** / nonlocal (enclosing functions enclosing nested functions)
3. **Global** / module (top_most: program, script, module)
4. **Built-in** (interpreter, keywords, builtin functions, exceptions)

```python
# global scope
gd = dir()
# built-ins scope
gbi = dir(__builtins__)
```
**\_\_dict\_\_**, **\_\_code\_\_**

**\_\_main\_\_**
Python turns your program’s main script into a module called __main__ to hold the main program’s execution.  
```python
if __name__ == '__main__':
    pass
```

---

## globals(), locals()
**globals()**:  
Return the dictionary implementing the current module namespace.  
**locals()**:  
Update and return a dictionary representing the current local symbol table.
```python
z = (locals() == globals())
v = globals()
# v = {'__name__': '__main__', ... , '__cached__': None, 'sys': <module 'sys' (built-in)>, 'z': True, 'v': {...}}
def foo():
    x = 5
    def fuu():
        y = x + 1
        nl = 0
        def fii():
            global gg
            nonlocal nl
            gg = 33
            nl = 55
            z = x + 2
            t = y + 10
            m = locals()  # m = {'z': 7, 't': 16, 'nl': 55, 'x': 5, 'y': 6}
            n = globals()
            # n = {'__name__': '__main__', ... , '__cached__': None, 'sys': <module 'sys' (built-in)>, 'z': True, 'v': {...}, 'foo': <function foo at 0x...>, 'gg': 33}
            return None
        fii()
        l = locals()  # l = {'fii': <function foo.<locals>.fuu.<locals>.fii at 0x...>, 'nl': 55, 'y': 6, 'x': 5}
        return None
    fuu()
    k = locals()  # k = {'fuu': <function foo.<locals>.fuu at 0x...>, 'x': 5}
    return None

foo()
```

---

## vars(), dir()
**vars()**  
Returns the **\_\_dict\_\_** attribute of a module, class, instance, or any other object which has a dictionary attribute.  
Without an argument, **vars()** acts like **locals()**.  
**dir()**  
With an argument, attempt to return a list of valid attributes for that object.  
**\_\_dict\_\_** is on that list. Without arguments, return the list of names in the current local scope.  
The default dir() mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:
- If the object is a module object, the list contains the names of the module’s attributes.
- If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.
- Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.  

```python
v = (locals() == vars())  # v = True
q = locals()  # q = {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x...>,
              # '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '....py', '__cached__': None}
r = dir()     # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
def foo():
    x = 5
    w = locals()  # w = {'x': 5}
    z = vars()    # z = {'x': 5}
    s = dir()     # s = ['x']
class Foo:
    y = 10    
    
y = vars(Foo)  # y = {'__module__': '__main__', 'y': 10, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>,
               # '__doc__': None}
u = vars(foo)  # u = {}
o = dir(Foo)   # o = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
               # '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
               # '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'y']
p = dir(foo)   # p = ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__',
               # '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__',
               # '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
               # '__sizeof__', '__str__', '__subclasshook__']    
    
    
t = vars(10)  # TypeError: vars() argument must have __dict__ attribute
```