# metaclasses  
<!-- TOC -->
* [metaclasses](#metaclasses-)
  * [Brief](#brief-)
  * [Use cases for metaclasses:](#use-cases-for-metaclasses)
  * [Creating metaclass](#creating-metaclass)
  * [Examples](#examples)
  * [**\_\_instancecheck\_\_()**, **\_\_subclasscheck__()**](#instancecheck-subclasscheck-)
  * [Links](#links)
<!-- TOC -->

---

## Brief 
**object** ---instance of--> **class** ---instance of--> **metaclass**  
**type** is basic standard **metaclass**  
**object** is basic standard **class**  
Mataclasses are used in Django, SQLAlchemy, Pydantic, ...  

## Use cases for metaclasses:
- **Creating APIs or DSLs**: Metaclasses can be used to create domain-specific languages (DSLs) or application programming interfaces (APIs) that make it easier for other programmers to interact with your code. For example, you might create a metaclass that automatically generates a set of methods and properties for working with a specific set of data types.  
- **Adding validation or enforcement**: Metaclasses can be used to add validation or enforcement rules to your code. For example, you might create a metaclass that ensures that all instances of a class conform to a certain interface or have certain attributes (**ABCMeta**).
- **Implementing singletons**: A singleton is a design pattern that ensures that only one instance of a class is ever created. Metaclasses can be used to implement singletons by ensuring that a new instance is only created when one does not already exist.
- **Dynamically generating code**: Metaclasses can be used to dynamically generate code at runtime. For example, you might use a metaclass to generate classes and methods based on data retrieved from a database or external API.
- **Creating plugins or extensions**: Metaclasses can be used to create plugins or extensions for your code. For example, you might create a metaclass that allows other developers to add custom methods or functionality to your classes.  

## Creating metaclass

```python
class Meta(type):  # <---------- metaclass is a subclass of type!!!!
    def __new__(cls, name, bases, attrs, **kwargs): # kwargs ------
        # customize the creation of new classes here...            |
        return super().__new__(cls, name, bases, attrs) #         \|/ see below
                                                                   
    def __init__(self, name, bases, attrs, **kwargs):
        # perform any additional initialization here...
        super().__init__(name, bases, attrs)
```
New class from metaclass:
```python
class Foo(metaclass=Meta, **kwargs): # <- additional keywords that can be used in class creation
    pass
```
Same using **type** keyword with 3 arguments:
```python
Meta = type('Meta', (type,), {})
Foo = Meta('Foo', (), {})
f = Foo()
print(type(type),   type(Meta),          type(Foo),            type(f))
#   <class 'type'> <class 'type'> <class '__main__.Meta'> <class '__main__.Foo'>
```
## Examples
- auto adding methods  
```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['new_attribute'] = 'Hello, World!'
        attrs['new_method'] = lambda self: 'Hello from a new method!'
        return super().__new__(cls, name, bases, attrs)
```
- enforcing constraints on the creation of classes
```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        if 'required_attribute' not in attrs:
            raise TypeError('Class must define required_attribute')
        return super().__new__(cls, name, bases, attrs)
```
- Implementing domain-specific languages (DSLs)

- Custom class that automatically generates its own methods based on the attributes it is given:  
```python
class AttributeGetterMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name in attrs:
            if not attr_name.startswith('__'):           
                def make_getter(attr_name):
                    def getter(self):
                        return getattr(self, attr_name)
                    return getter          
                attrs['get_'+attr_name] = make_getter(attr_name)
        return type.__new__(cls, name, bases, attrs)

class MyClass(metaclass=AttributeGetterMeta):
    name = 'John'
    age = 30

obj = MyClass()
print(obj.get_name()) # Output: 'John'
print(obj.get_age()) # Output: 30
```

## **\_\_instancecheck\_\_()**, **\_\_subclasscheck__()** 
Could be defined only in metaclass.  
Customisation of **isistance()** and **isdubclass()** built-in methods.

## **\_\_prepare__()**
The namespace returned by **\_\_prepare__** is passed in to **\_\_new__**, but when the final class object is created the namespace is copied into a new dict.  
If the metaclass has no **\_\_prepare__** attribute, then the class namespace is initialised as an empty ordered mapping.  
```python
from collections import OrderedDict
class Meta(type):  
    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        ...
        return OrderedDict()
    def __new__(cls, name, bases, attrs, **kwargs):
        ...
        return super().__new__(cls, name, bases, attrs)                                                     
    def __init__(self, name, bases, attrs, **kwargs):
        ...
        super().__init__(name, bases, attrs)
```
## Links
[What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)  
[real python](https://realpython.com/python-metaclasses/)  
[medium](https://medium.com/@miguel.amezola/demystifying-python-metaclasses-understanding-and-harnessing-the-power-of-custom-class-creation-d7dff7b68de8)  



