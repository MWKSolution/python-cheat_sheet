# Code
1. breakpoint()
2. compile()
3. eval()
4. exec()
5. help()

---

## breakpoint()
Enters debugger - very usefull for debugging.  
!!! Use instead of ***print()*** !!!  
In (pdb) use *p* for frint variable.  
```python
b = 5
breakpoint()
# (Pdb) p b
# 5
# (Pdb) 

```

---

## compile()

---

##  eval()
Evaluates an **single** expression and return value.
Cannot contain statements.  
**!!! Never ever use it with untrusted input !!!**   
```python
v = eval('max(10, 5)')  # v = 10
```
```python
v = eval("for i in range(5): print(i, sep=' ')")
# SyntaxError: invalid syntax
```
But this is single expression (exec) !!! :
```python
v = eval(compile('for i in range(5): print(i, end=" ")', '<string>', 'exec'))
# output: 0 1 2 3 4
```
Changing scopes.  
```python
v = eval('1+1', globals(), locals())
# is equivalent to
v = eval ('1+1')
```
```python
v = x  # NameError: name 'x' is not defined
w = y  # NameError: name 'y' is not defined
z = eval('1+x+y', {'x':10}, {'y':10})  # z = 21
```
Changing builtins:
```python
eval("print(1+1)",{'__builtins__': {}} ,{})
# NameError: name 'print' is not defined 
```
 Use it to prevent run malicious code
```python
eval("__import__('subprocess').getoutput('echo Hello, World')", {'__builtins__': {}} ,{} )  # 'rm –rf *'
```
Some holes still exist...  
See **ast.literal_eval()** for a function that can safely evaluate strings with expressions containing only literals.  
---

## exec()
Executes code block and doesn't return any value (None).  
Can contain statements.  
**!!! Never ever use it with untrusted input !!!**  
```python
exec("for i in range(5): print(i, end=' ')")
# output: 0 1 2 3 4
```
```python
v = exec('print(1+x+y)', {'x':10}, {'y':10})  # v = None
# output: 21
```
Mimic python REPL:
```python
while True:
    exec(input(">>> "))
```
rest similar to eval().  

---

## help()
Invoke the built-in help system. (This function is intended for interactive use.)  
if a slash(/) appears in the parameter list of a function when invoking help(), it means that the parameters prior to the slash are positional-only. 
Used doc strings form classes.
```python
x  = help(help)
help(help)
# Help on _Helper in module _sitebuiltins object:
# class _Helper(builtins.object)
#  |  Define the builtin 'help'.
#  |  
#  |  This is a wrapper around pydoc.help that provides a helpful message
#  |  when 'help' is typed at the Python interactive prompt.
#  |  
#  |  Calling help() at the Python prompt starts an interactive help session.
#  |  Calling help(thing) prints help for the python object 'thing'.
#  |  
#  |  Methods defined here:
#  |  
#  |  __call__(self, *args, **kwds)
#  |      Call self as a function.
#  |  
#  |  __repr__(self)
#  |      Return repr(self).
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
```
Doc strings:
```python
class C:
    """Class docstring"""
    def m(self):
        """Method docstring"""

x = C.__doc__  # x = 'Class docstring'
help(C)
# class C(builtins.object)
#  |  Class docstring
#  |  
#  |  Methods defined here:
#  |  
#  |  m(self)
#  |      Method docstring
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
```