# Dunder

<!-- TOC -->
* [Dunder](#dunder)
  * [**dir**(object) and **vars**(object)](#dirobject-and-varsobject)
  * [dunder methods](#dunder-methods)
  * [**\_\_getattr__**](#getattr)
  * [**\_\_slots__**](#slots)
  * [**\_\_weakref__**](#weakref-)
<!-- TOC -->

---

## **dir**(object) and **vars**(object)

```python
dir(o)
 |  # attributes of the object (class level)
o.__class__
o.__doc__
o.__dict__   ---> vars(o) # __dict__ attr of object
  ...               |  # atributes of the object (instance level)
                    .__init__
                    .__str__
                    ...
```
## dunder methods

```python
 __dir__             # called by dir(object)
 __format__          # called by spec.format(object)  object.__format__(spec)
 __getstate__        # Classes can further influence how their instances are pickled by overriding the method
 __init_subclass__   # his method is called whenever the containing class is subclassed
 __sizeof__          # called by sys.sizeof(object)
```

## **\_\_getattr__**

There are two methods for getting attribute of object:
- First **\_\_getattribute__** is called
- If raises **AttributeError** **\_\_getattr__** is called:

```python
class Foo:
    DEFAULT = 'Default'

    def __init__(self):
        self.a = 1
        self.b = 2

    # def __getattribute__(self, item):  
    #     return object.__getattribute__(self, item) - original method is doing sth like that
    #     return super().__getattribute__(item)      - or this

    def __getattr__(self, item):
        print(f'Instance has no {item} attribute...\nSo try get with {item} with this method...')
        setattr(self, item, self.DEFAULT)
        return self.DEFAULT

f = Foo()

print(f'a= {f.a}, b={f.b}')
print(f'c= {f.c}')
print(f'c= {f.c}')
# output:
# a= 1, b=2
# Instance has no c attribute...
# So try get with c with this method...
# c= Default
# c= Default
```
## **\_\_slots__**

 **\_\_slots__** reserves space for the declared variables and prevents the automatic creation of __dict__ and __weakref__ for each instance.  
Saves memory if creating lots of instances.  

##  **\_\_weakref__** 

Weak referenced objects could be garbage collected. Used for cache for large objects.  
Use high level WeakKeyDictionary and WeakValueDictionary.

