# NumPy
1. [Brief](#Brief)
   1. [Numpy]()
   2. Axes
   3. Data types
2. [ndarray]()
--- 

## Brief
### Numpy  
+ more speed
+ fewer loops
+ ndarrays are fixed size - change size - new array
+ all elements are of the same type
+ vectorization - same operation for each element - removes 'for' loops
+ broadcasting - way of treating arrays of different sizes during operations 

### Axes
```
axis=0  |   ,   axis=1 --------
        |  
        |  
```

### Data types
**NumPy data types:** (depends on platform!)

| alias           | type, other alias                      | range                                        | code |
|-----------------|----------------------------------------|----------------------------------------------|------|
|                 | BOOL TYPES                             |                                              |      |
| **bool8**       | bool_                                  | True, False                                  | ?    |
|                 | INT TYPES                              |                                              |
| **int8**        | byte                                   | -128...127                                   | b    |
| **int16**       | short                                  | -32_768...32_767                             | h    |
| **int32**       | intc, int_                             | -2_147_483_648...2_147_483_647               | i, l |
| **int64**       | intp, longlong                         | ...9_223_372_036_854_775_807                 | q    |
|                 |                                        |                                              |      |
| **uint8**       | ubyte                                  | 0...255                                      | B    |
| **uint16**      | ushort                                 | 0...65535                                    | H    |
| **uint32**      | uintc, uint                            | 0...4_294_967_295                            | I, L |
| **uint64**      | ulonglong                              | 0...18_446_744_073_709_551_615               | Q    |
|                 | FLOAT TYPES                            |                                              |      |
| **float16**     | half                                   | sign bit, 5 bits exponent, 10 bits mantissa  | e    |
| **float32**     | single                                 | sign bit, 8 bits exponent, 23 bits mantissa  | f    |
| **float64**     | double, float_, longdouble, longfloat  | sign bit, 11 bits exponent, 52 bits mantissa | d, g |
|                 | COMPLEX TYPES                          |                                              |      |
| **complex64**   | csingle, singlecomplex                 | 2 * float32                                  | F    |
| **complex128**  | cdouble, cfloat, complex_, clongfloat, | 2 * float64                                  | D    |
|                 | TIME TYPES                             |                                              |      |
| **datetime64**  |                                        | uint64 from  1970-01-01                      | M    |
| **timedelta64** |                                        | uint64                                       | m    |
|                 | OTHER TYPES                            |                                              |      |
| **bytes_**      | string_                                | byte string b'...'                           | S    |
| **unicode_**    | str_                                   | unicode string b'...'                        | U    |
| **void**        |                                        | sequence of bytes                            | V    |
| **object_**     |                                        | Python objects                               | O    |

## ndarray
### array
```python
numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
```
```python
a = np.array([[1, 2], [3, 4]], dtype=np.int8)
# a = array([[1, 2],
#            [3, 4]], dtype=int8)
```

### arange
```python
numpy.arange([start, ]stop, [step, ], dtype=None)
```
```python
a = np.arange(5)                 # a = array([0, 1, 2, 3, 4])
b = np.arange(1, 10, 2)          # b = array([1, 3, 5, 7, 9])
c = np.arange(-5,-1)             # c = array([-5, -4, -3, -2])
d = np.arange(7, 0, -3)[::-1]    # d = array([1, 4, 7])
e = np.flip(np.arange(7, 0, -3)) # e = d
f = np.arange(1,1)               # empty array, f = array([], dtype=int32)
```
### linespace
```python
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
```
```python
a = np.linspace(1, 2, num=5)
# a = array([1.  , 1.25, 1.5 , 1.75, 2.  ])
a = np.linspace([0,1], [2, 3], num=5)
# a = array([[0. , 1. ],
#            [0.5, 1.5],
#            [1. , 2. ],
#            [1.5, 2.5],
#            [2. , 3. ]])
```
### meshgrid

### fromfuntion
```python
a = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
# a = array([[0, 1, 2],
#            [1, 2, 3],
#            [2, 3, 4]])
```
logspace, geomspace
### other creation methods
```python
np.empty(shape, dtype) # faster than zeros
np.zeros(shape, dtype) # filled with zeros
np.ones(shape, dtype)  # filled with ones
np.full(shape, dtype, value)  # filled with value
np.eye(n, m, k, dtype)  # diagonal of shape (n,m) starting from index k
np.identity(n, dtype) # like np.eye(n)
np.diag(a)            # make diag 2d matrix from 1d 'a'
np...._like(a, dtype)  # return ... array with the same shape as 'a'
```

## attributes
ndim - number of axes
shape - dimensions of array
size - number of elements
dtype - type of elements
itemsize - size of each element
data

reshape
unique
diag
copy(a) - np.array(a, copy=True) 

files

print, np.set_printoptions(threshold=sys.maxsize)