
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

## Other constructors

### from_dict

### from_records

## Accessors

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

## data types

Valid data types for series/columns:  
- [Numpy types](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases)  
- [Pandas extension types](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)

## Creating DF from files
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



## Indexing / selecting

## viewing

tail, head

## setting values
d[1,1] = x

## slicing