# Pandas
1. [Basics](#Basics)
   1. Data types
   2. Indexes
   3. Series
2. [DataFrame](#DataFrame)
   1. Constructor
   2. Attributes
   3. Methods
   4. Other constructors
3. [Simple operations](#Simple-operations)
   1. Accessing
   2. Setting
   3. Inserting
   4. Deleting
4. [Sorting](#Sorting)
5. [Filtering](#Filtering)
6. [Iteration](#Iteration)
   1. items
   2. iteritems
   3. iterrows
   4. itertuple
7. [Combining](#Combining)
   1. merge
   2. join
   3. concat
8. [Input Output](#Input-Output)


---
## Basics
### Data types

Valid data types for series/columns:  
- [Numpy types](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases)  
- [Pandas extension types](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)

### Indexes
Indexes are immutable - cannot be changed by simple assigning  
set_index()
multiindex !!!

### Series
One dim array with index.  
```python
s = pd.Series(np.arange(3), dtype='float64')
# s = 0    0.0
#     1    1.0
#     2    2.0
#     dtype: float64
a = s.array
# a = <PandasArray>
#     [0.0, 1.0, 2.0]
#     Length: 3, dtype: float64
i = s.index
# i = RangeIndex(start=0, stop=3, step=1)
s = pd.Series([1, 5, 13], index=['a', 'f', 'x'])
# s = a     1
#     f     5
#     x    13
#     dtype: int64
i = s.index  # i = Index(['a', 'f', 'x'], dtype='object')
v = s['x']   # v = 13
```
from dictionary
```python
d = {'a':10, 'b':9, 'c':3}
s = pd.Series(d)
# s = a    10
#     b     9
#     c     3
#     dtype: int64
td = s.to_dict()  # back to dictionary
s2 = pd.Series(d, index=['c', 'b', 'x'], name='data')
# s2 = c    3.0
#      b    9.0
#      x    NaN
#      dtype: float64
n = s2.name  # n = 'data'
```
series are aligned to index in operations (arithmetic)   
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
*copy* - bool, *default=None*, False - use original data, True - use copy 

```python
import pandas as pd

n = [11, 22, 33, 44, 55]
l = ['a', 'b', 'c', 'd', 'e']
data = {'Numbers': n, 'Letters': l}
index = pd.RangeIndex(start=1, stop=6, step=1, name='Idx')

d = pd.DataFrame(data=data, index=index)
#      Numbers Letters
# Idx                 
# 1         11       a
# 2         22       b
# 3         33       c
# 4         44       d
# 5         55       e
dd = pd.DataFrame(data=d, columns=['Numbers'])
#  Numbers
# Idx	
# 1	11
# 2	22
# 3	33
# 4	44
# 5	55
```
nested dictionary
```python
data = {'col1':{'a':1, 'b':2}, 'col2':{'a':11, 'c':33}}
d = pd.DataFrame(data=data)
#       col1	col2
# a	1.0	11.0
# b	2.0	NaN
# c	NaN	33.0
d.T  #  view !!!
#       a	b	c
# col1	1.0	2.0	NaN
# col2	11.0	NaN	33.0
```

### attributes
```python
d.dtypes,     # columns data types
# Numbers     int64
# Letters    object
# dtype: object
d.index,      # index column
# RangeIndex(start=1, stop=6, step=1, name='Idx')
d.index.name
d.columns,    # column names (as index!)
# Index(['Numbers', 'Letters'], dtype='object')
d.columns.name
d.empty,      # if df is empty
# False
d.flags,      # only one flag for now
# <Flags(allows_duplicate_labels=True)>
d.ndim,       # df dimension
# 2
d.shape,      # df shape
# (5, 2)
d.size,       # number of elements (excluding index and columns names)
# 10
d.values,     # df as list(array) of rows (lists/arrays), same as d.to_numpy()
# array[[11 'a']
#       [22 'b']
#       [33 'c']
#       [44 'd']
#       [55 'e']]
```
### methods
**reindex** [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html?highlight=reindex#pandas.DataFrame.reindex), Series or Index  
```python
DataFrame.reindex(labels=None, index=None, columns=None, axis=None, method=None, copy=None, level=None, fill_value=nan, limit=None, tolerance=None)
```
```python
data = np.arange(4).reshape(2,2)
d = pd.DataFrame(data=data, columns=['col1', 'col2'], index=[1,3])
#       col1	col2
# 1	0	1
# 3	2	3
d.reindex(index=np.arange(4), columns=['col1', 'x', 'col2'], fill_value=-999)
#       col1    x	col2
# 0	-999	-999     -999
# 1	0.0	-999     1.0
# 2	-999	-999     -999
# 3	2.0	-999     3.0
```
**tail()** - last rows...  

**head()** - first rows...

T transpose - view !!!!

memory_usage()
to_numpy() = df.values

modify type  df.astype(dtype={'age': np.int32, 'py-score': np.float32})

### Other constructors

[from_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html)  
[from_records](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records)  

## Simple operations

### accessing
**accessors**  
```python
d
#      Numbers Letters
# Idx                 
# 1         11       a
# 2         22       b
# 3         33       c
# 4         44       d
# 5         55       e
d.Numbers,            # 
d['Numbers'],         # column/columns
# Idx
# 1    11
# 2    22
# 3    33
# 4    44
# 5    55
# Name: Numbers, dtype: int64
d.loc[4],             # row by name in index
d.iloc[3],            # row by index
# Numbers    44
# Letters     d
# Name: 4, dtype: object
d.at[4, 'Numbers'],   # value by names of row and column or...
d.Numbers[4]
d[Numbers][4]
d.iat[3, 0],          # value by indexes
# 44
``` 
**with slicing**  
```python
data = np.arange(9).reshape(3,3)
df = pd.DataFrame(data=data, columns=['c1', 'c2', 'c3'], index=['i1','i2','i3'])
#       c1	c2	c3
# i1	0	1	2
# i2	3	4	5
# i3	6	7	8
```
```python
df['c1']                  # column - pd.series
df[['c1', 'c2']]          # two columns - passing list or single element
df[0:-1]                  # rows minus last row - select rows with slicing

df.loc['i1']
df.iloc[0]                # one row
df.loc[:,'c2']            
df.iloc[:,1]              # one column
df.loc[['i1','i3'], 'c1':'c2']
df.iloc[1:3,[0,1]]
df.loc[d.c2 > 1]
```
Avoid chained indexing! Use [,] instead of [][]  
**mask**  
```python
df > 4
#       c1	c2	c3
# i1	False	False	False
# i2	False	False	True
# i3	True	True	True
df[df > 4]
#       c1	c2	c3
# i1	NaN	NaN	NaN
# i2	NaN	NaN	5.0
# i3	6.0	7.0	8.0
df[df > 4] = 0
#       c1	c2	c3
# i1	0	1	2
# i2	3	4	0 <-
# i3	0	0	0
df['c1'] > 4
# i1    False
# i2    False
# i3     True
# Name: c1, dtype: bool
df[df['c1'] > 4]
#       c1	c2	c3
# i3	6	7	8
df[df['c1'] > 4] = 0
#       c1	c2	c3
# i1	0	1	2
# i2	3	4	5 <-
# i3	0	0	0
```
### setting values
Use accessors (with slices
```python
d['Numbers'] = 1  # whole column
...
```

### inserting
Row 
```python
df.append(DataFrame_or_Series/dict-like_object_or_list_of_these)
``` 
Column
```python 
df['column-name'] = array_or_value
```
Column with location
```python
df.insert(loc, 'column-name', data)
```
Series
```python
s = pd.Series(data=[1, 1, 1])
# 0    1
# 1    1
# 2    1
# dtype: int64
d['new'] = s
# Numbers	Letters	new
# Idx			
# 1	11	a	1.0
# 2	22	b	1.0
# 3	33	c	NaN
# 4	44	d	NaN
# 5	55	e	NaN
```
### deleting
Column
```python
del df['column-name'] 
sr = df.pop('column-name')
```
Column or row
```python
df.drop(index)
df.drop(index=[index,...])
df.drop(columns=[column,...])
df.drop([column,...], axis=1)
```

### math
Aligning indexes and columns, inserts *NaN* or *fill_value*  
With broadcasting  
add +, sub -, div /, floordiv //, mul *, pow **, + r___ - reversed  

NumPy ufunc work with Pandas.  
**df.apply(func, axis)** - for user defined functions  
## Sorting
[by values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)  
```python
df.sort_values(by=[columns], ascending=[True, False, ...], kind='sorting-algorithm', axis=1, inplace=True, na_position='first')
#  kind : {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’
```
[by index or columns_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html?highlight=sort_index#pandas.DataFrame.sort_index)  
```python
df.sort_index()  # sort by index
df.sort_index(axis=1)  # sort by column names
```
## Filtering
general
```python
conditon = df['column'] > v
df[condition]
#  combining conditions: NOT (~), AND (&), OR (|), XOR (^)
```
where
```python
df.where(cond=condition, other=value)
```
## Iteration
### items
over columns as tuple (label, series)
```python
for label, series in df.items():
    print(f'label: {label}')
    print(f'content: {series}', sep='\n')
```
### iteritems
deprecated - same as items
### iterrows
over rows as tuple (index, series)
```python
for index, row in df.items():
    print(f'index: {index}')
    print(f'content: {row}', sep='\n')
```
### itertuples
over rows as namedtuples
```python
for row in df.itertuples(index=True, name='Row'):
    print(row)  # row = Row(Index='...', col1='...', col2='...', ...)
```
## Combining
### merge
on common columns or indices
### join
on key column or an index
### concat
across rows and columns

## Input Output


### Creating DF from files
[Reading from files](https://pandas.pydata.org/docs/user_guide/io.html#)

### CSV and TXT

```python
pd.read_csv(file)
pd.read_fwf(file)
```
[CSV](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)   
***sep/delimiter***, fields delimiter, default=','  
***skiprows***, list of 0-indexed rows to skip, default=None (skip row with units: skiprows=1)

[Fixed width](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html)

### JSON

```python
pd.read_json(file)
```
[JSON](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html)

### Excel and ODF

```python
pd.read_excel(file, sheet_name=0)
pd.read_excel(file, engine='odf') # only reading
```
[Excel/ODF](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
### SQL

```python
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///:memory:")

with engine.connect() as conn, conn.begin():
    df1 = pd.read_sql(sqlquerry_tablename, conn)
    df2 = pd.read_sql_table(table_name, conn)
    df3 = pd.read_sql_query(query, conn)
```
[sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas.read_sql)  
[table](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#pandas.read_sql_table)  
[query](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html#pandas.read_sql_query)


### Other types
XML, cliboard, HDF5 (.h5), Feather , Parquet, ORC, Stata (.dta),  SAS (.xpt, .sas7bdat), SPSS (.sav, .zsav), pickle

