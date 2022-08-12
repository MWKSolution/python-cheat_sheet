# ChainMap
1. [Brief]()
2. [Mapping]()
3. [Methods and properties]()
   1. get(), items(), keys(), values()
   2. maps
   3. new_child(), parents
   4. Dict methods on ChainMap.maps[0]
4. [Managing Scopes and Contexts]()
5. [ChainMap vs dict.update()]()
---

## Brief
1. A ChainMap groups multiple dicts (or other mappings) together to create a single, updateable view - changes in chains affects Chainmap.  
2. The underlying mappings are stored in a list.  That list is public and can be accessed or updated using the *maps* attribute.  
3. Lookups search the underlying mappings successively until a key is found.  
4. In contrast, writes, updates, and deletions only operate on the first mapping.
5.  the primary use case of ChainMap is to provide an efficient way to manage multiple scopes or contexts and handle access priorities for duplicate keys.  
---

## Mapping 
```python
from collections import ChainMap
numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}
cm = ChainMap(numbers, letters)  # cm = ChainMap({'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})
l = cm.maps                      # l = [{'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'}]
```

## Methods and properties

### get(), items(), keys(), values()
Search for key in all chains. child to parent.
### maps
! list ! of mappings. Use functions and methods for lists !!!
```python
from collections import ChainMap
numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}
cm = ChainMap(numbers, letters)  # cm = ChainMap({'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})
l = cm.maps                      # l = [{'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'}]
```
### new_child(), parents
new_child Returns new mapping. Creates new context (ChaiMap.maps[0])  
parents - back to previous context
```python
from collections import ChainMap
numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}
cm = ChainMap(numbers, letters)         # cm = ChainMap({'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})
l = cm.maps                             # l = [{'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'}]
cm = cm.new_child({1: "xxx", 2: "yyy"}) # cm = ChainMap({1: 'xxx', 2: 'yyy'}, {'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})
l = cm.maps                             # l = [{1: 'xxx', 2: 'yyy'}, {'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'}]
v = cm.parents                          # v = ChainMap({'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})
l = cm.parents.maps                     # l = [{'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'}]
```
### Dict methods on ChainMap.maps[0]
**clear()**, **copy()**, **pop()**, **popitem()**, **setdefault()**, **update()**
## Managing Scopes and Contexts 
The primary use case of ChainMap is to provide an efficient way to manage multiple scopes or contexts and handle access priorities for duplicate keys.  
This feature is useful when you have several dictionaries that store duplicate keys and you want to define the order in which your code will access them.  
Search multiple dictionaries in a single view efficiently.  
Prioritizing Command-Line Apps Settings:  
```python
from collections import ChainMap
cmd_proxy = {}  # The user doesn't provide a proxy
local_proxy = {"proxy": "proxy.local.com"}
system_proxy = {"proxy": "proxy.global.com"}
config = ChainMap(cmd_proxy, local_proxy, system_proxy)
v = config["proxy"]  # v = 'proxy.local.com'
```
Managing Default Argument Values lookup chain.  
## ChainMap vs dict.update()
Regular dictionaries can’t store repeated keys.  
The most important drawback is that you’re throwing out the ability to manage and prioritize the access to repeated keys using multiple scopes or contexts.  
If you often create chains of dictionaries and only perform a few key lookups each time, then you should use ChainMap. If it’s the other way around, then use regular dictionaries unless you require duplicate keys or multiple scopes.  
