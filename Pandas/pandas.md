# Pandas
1. [Basics](#Basics)
   1. Data types
   2. Axis
   3. Indexes
   4. Series
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
   5. math
4. [Data cleaning](#Data-cleaning)
   1. Missing data
   2. Data transformation
5. [String operations](#String-operations)
6. [Operations](#Operations)
   1. Sorting
   2. Ranking
   3. Filtering
   4. Statistics
7. [Iteration](#Iteration)
   1. items
   2. iteritems
   3. iterrows
   4. itertuple
8. [Combining](#Combining)
   1. merge
   2. join
   3. concat
9. [categorical data](#Categorical-data)
10. [Input Output](#Input-Output)
    1. Creating DF from files
    2. CSV and TXT
    3. JSON
    4. Excel and ODF
    5. SQL
    6. Other types
11. [Options](#Options)
12. [Extensions](#Extensions)


---
## Basics
### Data types

Valid data types for series/columns:  
- [Numpy types](../Numpy/numpy_types.md)  
```python
dtype = np.int64
dtype = 'int64'
```
- [Pandas extension types](extension_types.md)

```python
dtype = pd.Int64Dtype()  # brackets !!!
dtype = 'Int64'  # not int32 - pd.Int32Dtype
```
### Axis
```python
axis=0, axis='index'
axis=1, axis='columns'
```

### Indexes
Indexes are immutable - cannot be changed by simple assigning  
**set_index(col)** - set new index as col 
**reset_index(drop=True)**  
Duplicate indexes  
```python
df.index.is_unique
df.index.unique
```
Index().get_indexer() - return index pos (integer) or -1 if not present

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

**sample(n)** - random sample of n rows or columns (axis)

**count()** - count non-NA cells

**get_dummies** - 

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
```python
df1 = pd.DataFrame(np.arange(4).reshape(2,2), columns=['A', 'B'], index=['a', 'b'])
df2 = pd.DataFrame(np.arange(4).reshape(2,2), columns=['B', 'C'], index=['a', 'c'])
df = df1 + df2
#       A       B	C
# a	NaN	1.0	NaN
# b	NaN	NaN	NaN
# c	NaN	NaN	NaN00000
# b	0.5	0.333333
df = df1.add(df2, fill_value=-1)
#       A	B	C
# a	-1.0	1.0	0.0
# b	1.0	2.0	NaN
# c	NaN	1.0	2.0
df = np.multiply(df1, 5)
#       A	B
# a	0	5
# b	10	15
```
NumPy ufunc work with Pandas.   
```python
df1.apply(np.sum, axis=0) # function could be applied acress axis
# A    2
# B    4
# dtype: int64
f= lambda x: x**2
df1.applymap(f)  # apply scalar function
#       A	B
# a	0	1
# b	4	9
```

## Data cleaning

### Missing data
float NaN : **np.nan**, **None**  
int  \< NA \>  : **pd.NA**
```python
df = pd.DataFrame([[np.nan,2, 3, 4], [1, 2, pd.NA, None],[1, 2, 3, 4]])
#       0	1	2	3
# 0	NaN	2	3	4.0
# 1	1.0	2	<NA>	NaN
# 2	1.0	2	3	4.0
b = df.isna()
#       0	1	2	3
# 0	True	False	False	False
# 1	False	False	True	True
# 2	False	False	False	False
```
**notna()** - opposite of **isna()**
```python
b = df.dropna()
# 
#       0	1	2	3
# 2	1.0	2	3	4.0
b = df.dropna(axis=1, how='any')  # or how='all' - drop only if all row or column in NaN
# axis: 0 or index, 1 or columns; thresh - how many NaNs to be dropped
#       1
# 0	2
# 1	2
# 2	2
```
```python
b = df.fillna(666)
#       0	1	2	3
# 0	666.0	2	3	4.0
# 1	1.0	2	666	666.0
# 2	1.0	2	3	4.0
d = {0:-1, 1:999, 2:'c'}
b = df.fillna(d)
#        0	1	2	3
# 0	-1.0	2	3	4.0
# 1	1.0	2	c	999.0
# 2	1.0	2	3	4.0
# method - ffil, bfil, None
```
### Data transformation
**duplicates** 
```python
df.duplicated()  ?  
df.drop_duplicates(subset=...)
```
**mapping**  
```python
df['new_column'] = df['column'].map(mapping)  # mapping could be function  
```
**replacing**  
```python
df.replace(-999, np.nan)
df.replace({-999: 0, -999.25: -1})
```
**renaming**  
```python
df.index = df.index.map(transform)
df.rename(index=tr1, columns=tr2)
df.rename(index=dict1, columns=dict2)
```
**bins**  
```python
rng = np.random.default_rng()
a = rng.standard_normal(100)
bins = [-100, 0, 100]
pd_bins = pd.cut(a, bins)
c = pd_bins.categories
# c = IntervalIndex([(-100, 0], (0, 100]], dtype='interval[int64, right]')')
d = pd.value_counts(pd_bins)
# (0, 100]     53
# (-100, 0]    47
# dtype: int64
c = pd_bins = pd.cut(a, bins, labels =['negative', 'positive'] )
# c = Index(['negative', 'positive'], dtype='object')
d = pd.value_counts(pd_bins)
# positive    53
# negative    47
# dtype: int64
```
qut with number instead of bins cut in (number)  bins of equal length  
qcut - cuts for quantiles (equal probability)  

**outliers**   
```python
rng = np.random.default_rng()
a = rng.standard_normal((1000,4))
df = pd.DataFrame(a)
df.describe()
#        0                  1      	2       	3
# count	1000.000000	1000.000000	1000.000000	1000.000000
# mean	-0.051248	0.059981	0.041690	-0.015677
# std	0.993138	1.025045	1.016295	0.995514
# min	-2.970296	-3.553033	-3.227038	-3.145625
# 25%	-0.716895	-0.615683	-0.703306	-0.663732
# 50%	-0.058155	0.055179	0.066547	-0.013794
# 75%	0.622315	0.723527	0.705924	0.645226
# max	3.900632	3.043639	3.466084	3.117405
# abs > 3 :
df[(df.abs() > 3).any(axis='columns')]
#            0  	1       	2       	3
# 15	-1.221766	0.062596	-0.951186	3.117405
# 48	0.673354	3.043639	-1.171271	0.523487
# 212	-0.717276	-1.070818	-3.227038	0.494111
# 304	1.725815	-0.623826	3.466084	-0.552276
# 368	3.060529	-0.240531	0.312437	-1.059358
# 372	-0.998372	-3.553033	-0.316823	-1.088046
# 632	-0.646031	0.180089	3.310936	-2.984301
# 667	0.782512	1.112181	0.288309	-3.145625
# 781	-0.056040	-0.604476	1.466349	3.023612
# 848	3.900632	0.574898	-1.129511	0.804713
# do something with outliers - change to NaN
df[(df.abs() > 3)] = np.nan
# count them by column
df.isna().sum()
# 0    2
# 1    2
# 2    3
# 3    3
# dtype: int64
```

## String operations

[String methods](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html?highlight=string#method-summary)  

Methods:
- python string methods
- regex methods

## Operations
### Sorting
[by values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)  
```python
df.sort_values(by=[columns], ascending=[True, False, ...], kind='sorting-algorithm', axis=1, inplace=True, na_position='first')
#  kind : {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’
```
[by index or columns_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html?highlight=sort_index#pandas.DataFrame.sort_index)  
```python
DataFrame.sort_index(*, axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)
```
```python
df.sort_values('column')
df.sort_values(['column_1', 'column_2'])
```
```python
df.sort_index()  # sort by index
df.sort_index(axis=1)  # sort columns by names
```
### Ranking
```python
DataFrame.rank(axis=0, method='average', numeric_only=_NoDefault.no_default, na_option='keep', ascending=True, pct=False)
```
```python
df = pd.DataFrame({'a':[1, 2, 2, 5], 'b':[1, 2, 7, 9]})
#       a	b
# 0	1.0	1.0
# 1	2.5	2.0
# 2	2.5	3.0
# 3	4.0	4.0
dfr = df.rank(axis='index')
#       a	b
# 0	1.0	1.0
# 1	2.5	2.0
# 2	2.5	3.0
# 3	4.0	4.0
```
### Filtering
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
### Statistics
Get a single value from series or dataframe.  Built-in handling for missing data.  
```python
df.sum(axis='columns', skipna=True)
df.mean()
df.idxmax(), df.idxmin()    # return index of max/min val in columns or rows
df.cumsum()    # cumulative sum over columns or rows
df.describe()  # statistics summary

df.corr()       #  pairwise correlation of columns: pearson, kendall, spearman
df.cov()        #   pairwise covariance of columns
df.corrwith()   # corr for different dataframes
df.pct_change() # Percentage change between the current and a prior element.

pd.unique()        # unique values 
df.value_counts()  # counts of unique rows
df.isin(values)    # if each element of df is in list of 'values'
```
count, argmin, argmax, quantile, median, mad, prod, var, std, skew, kurt, cummin, cummax, cumprod, diff
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
Use to JOIN on specified key columns, rest of columns could have the same names, default 'inner'  
[merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html?highlight=merge#pandas.merge)  
```python
pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
```
**left, right** - *dataframes or series*  
**how** - *'left', right’, ‘outer’, ‘inner’, ‘cross’(cartesian product)* -  default ‘inner’  
**on** - *list*, default None - if not on indexes - intersection of columns because key is all common columns  
**left_on=None, right_on=None, left_index=False, right_index=False** instead of on, on columns or inices!!!   
the most general method - join and concat are the cases of merge
### join
Use to JOIN on indices with different columns, default 'left'  
[join](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html?highlight=join#pandas.DataFrame.join)  
By default ON INDICES !!!  or left on key column and right (other) on index  
--- If not on indices new df index won't be range, **reset_index(drop=True)** may be necessary... !!!! ---    

```python
DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False, validate=None)[source]
```
### concat
```python
pandas.concat(objs, *, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)  
```

### Pandas vs SQL
```python
d1 = {'key':[1, 1, 3, 4, 5, 7], 'value':['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'x']}
df1 = pd.DataFrame(d1)
d2 = {'key':[2, 3, 3, 4, 6, 7], 'value':['gg', 'hh', 'kk', 'nn', 'oo', 'x']}
df2 = pd.DataFrame(d2)
# df1:
#       key	value
# 0	1	aaa
# 1	1	bbb
# 2	3	ccc
# 3	4	ddd
# 4	5	eee
# 5	7	x
# df2:
#       key	value
# 0	2	gg
# 1	3	hh
# 2	3	kk
# 3	4	nn
# 4	6	oo
# 5	7	x
```

*----------------joins----------------*

**INNER**
```python
pd.merge(df1, df2, on='key')  # how = 'inner'
df1.join(df2.set_index('key'), on='key', how='inner', lsuffix='_x', rsuffix='_y').reset_index(drop=True)
#       key	value_x	value_y
# 0	3	ccc	hh
# 1	3	ccc	kk
# 2	4	ddd	nn
# 3	7	x	x
```
If keys are indices, columns are different  
```python
df1.join(df2, how='inner')  # on indices!
pd.merge(df1, df2, left_index=True, right_index=True) # on indices
```
On column (df1) and index (df2), columns are different   
```python
df1.join(df2, on='key', how='inner')
pd.merge(df1, df2, left_on='key', right_index=True) # on column and index
```

**LEFT**  
```python
pd.merge(df1, df2, on='key', how='left')
df1.join(df2.set_index('key'), on='key', lsuffix='_x', rsuffix='_y').reset_index(drop=True)
#       key	value_x	value_y
# 0	1	aaa	NaN
# 1	1	bbb	NaN
# 2	3	ccc	hh
# 3	3	ccc	kk
# 4	4	ddd	nn
# 5	5	eee	NaN
# 6	7	x	x
```
**RIGHT**  
```python
pd.merge(df1, df2, on='key', how='right')
df1.join(df2.set_index('key'), on='key', how='right', lsuffix='_x', rsuffix='_y').reset_index(drop=True)
#       key	value_x	value_y
# 0	2	NaN	gg
# 1	3	ccc	hh
# 2	3	ccc	kk
# 3	4	ddd	nn
# 4	6	NaN	oo
# 5	7	x	x
```
**OUTER**  
```python
pd.merge(df1, df2, on='key', how='outer')
df1.join(df2.set_index('key'), on='key', how='outer', lsuffix='_x', rsuffix='_y').reset_index(drop=True)
#       key	value_x	value_y
# 0	1	aaa	NaN
# 1	1	bbb	NaN
# 2	3	ccc	hh
# 3	3	ccc	kk
# 4	4	ddd	nn
# 5	5	eee	NaN
# 6	7	x	x
# 7	2	NaN	gg
# 8	6	NaN	oo
```
**CROSS**  
Cartesian product  
```python
pd.merge(df1, df2, how='cross')
#       key_x	value_x	key_y	value_y
# 0	1	aaa	2	gg
# 1	1	aaa	3	hh
# 2	1	aaa	3	kk
# . .    .  .    .
# . .    .  .    .   each row with each row etc...
```
**self**  
INNER or LEFT  
```python
pd.merge(df1, df1, on='key', how='inner')
df1.join(df1.set_index('key'), on='key', how='inner', lsuffix='_x', rsuffix='_y').reset_index(drop=True)
#       key 	value_x	value_y
# 0	1	aaa	aaa
# 1	1	aaa	bbb
# 2	1	bbb	aaa
# 3	1	bbb	bbb
# 4	3	ccc	ccc
# 5	4	ddd	ddd
# 6	5	eee	eee
# 7	7	x	x
```
*---------------sets--------------*  
**UNION**  
```python
# UNION ALL
pd.concat([df1, df2]).reset_index(drop=True)                
# UNION
pd.merge(df1, df2, how='outer')
pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)
#       key	value
# 0	1	aaa
# 1	1	bbb
# 2	3	ccc
# 3	4	ddd
# 4	5	eee
# 5	7	x
# 6	2	gg
# 7	3	hh
# 8	3	kk
# 9	4	nn
# 10	6	oo
```
**EXCEPT**  
```python
df1[~(df1.isin(df2).all(axis=1))]
#       key	value
# 0	1	aaa
# 1	1	bbb
# 2	3	ccc
# 3	4	ddd
# 4	5	eee
```

**INTERSECT**  
```python
pd.merge(df1, df2) # on = None, by default (key is all common columns!)
#       key	value
# 0	7	x
```
## Categorical data
dimension tables...   
improving performance and memory use

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

## Options
pd.options.display.max_rows = 10


## Extensions

[Pandas extensions](https://pandas.pydata.org/docs/ecosystem.html#text-extensions-for-pandas)  
