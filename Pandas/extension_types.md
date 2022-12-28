# Pandas extension types

- [Pandas extension types](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)  

All types are nullable: use **pd.NA** for None, np.nan, ...  
!!! np dtypes are inferred if extension types are not given explicit  !!!

### nullable integer types
could be used with None, np.nan, ***pd.NA*** - and **would not** be inferred as float !!!:
```python
dtype = pd.Int64Dtype()  # or
dtype = 'Int64'          # not nullable NumPy dtypes: np.int64, 'int64'
...
```

### nullable float types
same as numpy dtypes but use pd.NA instead of np.nan

```python
dtype = pd.Float64Dtype()
dtype = 'Float64'          # numpy: float64
```
### string  
nullable  
use less memory and is more efficient for computation than NumPy np.object   
```python
dtype = pd.StringDtype()
dtype = 'string'
```
### boolean
nullable boolean

```python
dtype = pd.BooleanDtype
dtype = 'boolean'        # numpy: bool, bool8
```

### categorical


### datetime with time zone


### other types
period, sparse, interval