
## DataFrame 

### constructor 

```python
import pandas as pd
df = pd.DataFrame(data=data, index=index, columns=columns, dtype=dtype, copy=copy)
```
*data* - ndarray, iterable, dict, DataFrame  (could be empty)  
*index* - array or [Index](https://pandas.pydata.org/docs/reference/indexing.html), *default=None* -> [RangeIndex](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex)  
*colums* - array or [Index](https://pandas.pydata.org/docs/reference/indexing.html), *default=None* -> [RangeIndex](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex)  
*dtype* - data type to force (see [data types](#data-types)), *default=None* -> infer dtype  
*copy* - bool, *default=None*, ???  

### attributes
```python
import pandas as pd

n = [11, 22, 33, 44, 55]
l = ['a', 'b', 'c', 'd', 'e']
data = {'Numbers': n, 'Letters': l}
index = pd.RangeIndex(start=1, stop=6, step=1, name='Idx')

d = pd.DataFrame(data=data, index=index)

print(d, d.dtypes, d.index, d.columns, d.empty, d.flags,
      d.ndim, d.shape, d.size, d.values, sep='\n---\n')
```
```
     Numbers Letters
Idx                 
1         11       a
2         22       b
3         33       c
4         44       d
5         55       e
---
Numbers     int64
Letters    object
dtype: object
---
RangeIndex(start=1, stop=6, step=1, name='Idx')
---
Index(['Numbers', 'Letters'], dtype='object')
---
False
---
<Flags(allows_duplicate_labels=True)>
---
2
---
(5, 2)
---
10
---
[[11 'a']
 [22 'b']
 [33 'c']
 [44 'd']
 [55 'e']]
```

## Other constructors

### from_dict

### from_records



## data types

numpy data types for series/columns + some extensions

[Numpy types](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases)  
[Pandas extension types](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes

## from files/to files

### CSV

### JSON

### Excel

### SQL

## Indexing / selecting