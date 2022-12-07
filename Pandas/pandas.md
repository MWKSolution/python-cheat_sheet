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
3. [Simple operations](#Simple operations)
   1. Accessing
   2. Setting
   3. Inserting
   4. Deleting
4. [Sorting](#Sorting)
5. [Filtering](#Filtering)
6. ffgdfg
7. [Input Output](#Input Output)


---
## Basics
### Data types

Valid data types for series/columns:  
- [Numpy types](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases)  
- [Pandas extension types](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)

### Indexes

set_index()
multiindex !!!

### Series


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
```

### attributes
```python
print(d,
      d.dtypes,     # columns data types
      d.index,      # index column
      d.columns,    # column names (as index!)
      d.empty,      # if df is empty
      d.flags,      # only one flag for now
      d.ndim,       # df dimension
      d.shape,      # df shape
      d.size,       # number of elements (excluding index and columns names)
      d.values,     # df as list(array) of rows (lists/arrays)
      sep='\n---\n')
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

### methods

memory_usage()
to_numpy() = df.values

modify type  df.astype(dtype={'age': np.int32, 'py-score': np.float32})
tail, head

### Other constructors

[from_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html)  
[from_records](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records)  



## Simple operations

### accessing
accessors
```python
print(d,
      d.Numbers,            # column
      d['Numbers'],         # column/columns
      d.loc[4],             # row by name in index
      d.iloc[3],            # row by index
      d.at[4, 'Numbers'],   # value by names of row and column or...
      d.Numbers[4],
      d.iat[3, 0],          # value by indexes
      sep='\n---\n')
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
Idx
1    11
2    22
3    33
4    44
5    55
Name: Numbers, dtype: int64
---
Idx
1    11
2    22
3    33
4    44
5    55
Name: Numbers, dtype: int64
---
Numbers    44
Letters     d
Name: 4, dtype: object
---
Numbers    44
Letters     d
Name: 4, dtype: object
---
44
---
44
---
44
``` 
with slicing  
```python
df.loc[:,'column-name']
df.iloc[:,1]
df.loc['i':'j',['c-n1','c-n2']]
df.iloc[1:3,[0,1]]
```
### setting values
Use accessors (with slices)

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
### deleting
Column
```python
del df['column-name'] 
sr = df.pop('column-name')
```
Column or row
```python
df.drop(index=[index,...])
df.drop(columns=[column,...])
df.drop([column,...], axis=1)
```
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




## Input Output


### Creating DF from files
[Reading from files](https://pandas.pydata.org/docs/user_guide/io.html#)

### CSV and TXT

```python
pd.read_csv(file)
pd.read_fwf(file)
```
[CSV](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)  
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

