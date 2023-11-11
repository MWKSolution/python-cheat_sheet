# Collections  
I. In detail
1. [Counter](collections/Counter.md)  
2. [namedtuple](collections/namedtuple.md)  
3. [defaultdict](collections/defaultdict.md)  
4. [ChainMap](collections/ChainMap.md)  
5. [abc](collections/abc.md)
  
II. In general

1. [OrderedDict](#OrderedDict)
2. [UserDict, UserList, UserString](#)
3. [deque](#deque-)  

---

## OrderedDict  
Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations. They have become less important now that the built-in dict class gained the ability to remember insertion order (this new behavior became guaranteed in Python 3.7).  
Some differences from dict still remain...  
## UserDict, UserList, UserString  
Classes for user subclassing:  Dict, List or String.  
Subclassing built-ins Dict, List or String types can be error-prone because the C code of the built-ins doesn’t seem to consistently call special methods overridden by the user!  
## deque  
Double ended queue.  
It is the optimized list for quicker append and pop operations from both sides of the list.
In Python, append and pop operations on the beginning or left side of list objects are inefficient.  
If you’re working with queues, then favor using high-level **queue** module over deque unless you’re implementing your own data structure.  


