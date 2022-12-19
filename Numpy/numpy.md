# NumPy
1. [Brief](#Brief)
   1. Numpy
   2. Axes
   3. Data types
2. [ndarray](#ndarray)
   1. array
   2. asarray
   3. arange
   4. linespace
   5. meshgrid
   6. fromfunction
   7. other creation methods
3. [attributes](#attributes)
4. [methods](#methods)
   1. reshape
   2. flatten
   3. unique
   4. diag
   5. transpose
   6. vectorize
   7. nonzero
   8. astype
   9. where
5. [Operations](#operations)
   1. simple math
   2. bool
   3. copy
   4. manipulating
   5. expand
   6. mask
   7. math and statistics
   8. sort
   9. reverse
   10. Universal functions
6. [print options](#print-options)
7. [Structured arrays](#structured-arrays)
8. [Files](#files)
9. [Modules](#Modules)
   1. numpy.fft
   2. numpy.linalg
   3. numpy.matlib
   4. numpy.polynomial
   5. numpy.testing
   6. numpy.typing


--- 

## Brief
### Numpy  
+ more speed
+ fewer loops
+ ndarrays are fixed size - change size - new array
+ all elements are of the same type
+ vectorization - same operation for each element - removes 'for' loops
+ broadcasting - way of treating arrays of different sizes during operations 
+ vector - 1D ndarray, matrix - 2D ndarray, tensor - nD ndarray

### Axes
```
axis=0  |   ,   axis=1 --------
        |  
        |  
```

### Data types
**NumPy data types:** 
(depends on platform!)  
[Table...](/Numpy/numpy_types.md)  

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
### asarray
**asarray** is like array - doesn't make copy - view 

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
logspace, geomspace
### meshgrid
```python
numpy.meshgrid(*xi, copy=True, sparse=False, indexing='xy')
```
```python
x = np.linspace(-2, 2, 5)  # x = array([-2., -1.,  0.,  1.,  2.])
y = np.linspace(-2, 2, 5)  # y = array([-2., -1.,  0.,  1.,  2.])
xx, yy = np.meshgrid(x, y, indexing='xy')
# xx = array([[-2., -1.,  0.,  1.,  2.],
#             [-2., -1.,  0.,  1.,  2.],
#             [-2., -1.,  0.,  1.,  2.],
#             [-2., -1.,  0.,  1.,  2.],
#             [-2., -1.,  0.,  1.,  2.]])
# yy = array([[-2., -2., -2., -2., -2.],
#             [-1., -1., -1., -1., -1.],
#             [ 0.,  0.,  0.,  0.,  0.],
#             [ 1.,  1.,  1.,  1.,  1.],
#             [ 2.,  2.,  2.,  2.,  2.]])
zz = xx + yy
# zz = array([[-4., -3., -2., -1.,  0.],
#             [-3., -2., -1.,  0.,  1.],
#             [-2., -1.,  0.,  1.,  2.],
#             [-1.,  0.,  1.,  2.,  3.],
#             [ 0.,  1.,  2.,  3.,  4.]])
#
# indexing='xy' (cartesian indexing)-> xx=xx, yy=yy; indexing='ij' (matrix indexing) xx=yy yy=xx
# sparse = True - reduce space for use with broadcasting
```

### fromfunction
```python
a = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
# a = array([[0, 1, 2],
#            [1, 2, 3],
#            [2, 3, 4]])
```
### other creation methods
```python
np.empty(shape, dtype) # faster than zeros
np.zeros(shape, dtype) # filled with zeros
np.ones(shape, dtype)  # filled with ones
np.full(shape, dtype, value)  # filled with value
np.eye(n, m, k, dtype)  # diagonal of shape (n,m) starting from index k with values '1'
np.identity(n, dtype) # like np.eye(n)
np.diag(a)            # make diag 2d matrix from 1d 'a'
np...._like(a, dtype)  # return ... array with the same shape as 'a'
```

## attributes
**ndim** - number of axes  
**shape** - dimensions of array  
**size** - number of elements  
**dtype** - type of elements  
**itemsize** - size of each element  
**data** - data in memory  
**T** - transposed array  
**base** - *None* - array or copy, *object* - view  

## methods

### reshape
```python
a = np.arange(1, 13)
b = a.reshape(3, 4)
c = a.reshape((3, 4))
d = np.reshape(a, (3, 4))
# a = array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
# b = c = d = array([[ 1,  2,  3,  4],
#                    [ 5,  6,  7,  8],
#                    [ 9, 10, 11, 12]])
```
### flatten
```python
a = np.arange(1, 5).reshape(2, 2)
# a = array([[1, 2],
#            [3, 4]])
b = a.flatten()
# b = array([1, 2, 3, 4]) ! new array, copy
c = a.ravel()
# c = array([1, 2, 3, 4]) ! changes to 'c' will affect 'a', view
```

### unique
Unique elements of array
```python
import numpy as np

a = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
b = np.unique(a)
#a = array([1, 2, 3, 4])
```
intersect1d, union1d, in1d
### diag
```python
a = np.arange(1,4)
# a = array([1, 2, 3])
b = np.diag(a)
# b = array([[1, 0, 0],
#            [0, 2, 0],
#            [0, 0, 3]])
```
### transpose
```python
b = a.transpose()
b = a.T
```
transpose is like **a.swapaxes(0, -1)** - swaping first and last axis
 
### vectorize
Vectorize function

```python
import numpy as np

def fun(a):
   return a ** 2

vfun = np.vectorize(fun)
a = vfun([1, 2, 3])  # a = array([1, 4, 9])
```
### nonzero
Returns (tuple!!!) indices of non-zero elements - for use with fancy indexing
```python
a = np.arange(4).reshape(2,2)
# a = array([[0, 1],
#            [2, 3]])
b = np.nonzero(a)  # b = (array([0, 1, 1], dtype=int64), array([1, 0, 1], dtype=int64))
c = type(b)        # c =  <class 'tuple'>
# to get 'coordinates' in the array:
z = list(zip(b[0], b[1]))  # z = [(0, 1), (1, 0), (1, 1)]
```

### astype  
Change dtype of an array (copy)
```python
a = np.array([1,0,1])  # a = array([1, 0, 1])
t = a.dtype            # t = dtype('int32')
b = a.astype('bool')   # b = array([ True, False,  True])
t = b.dtype            # t = dtype('bool')
# a == b,  !(a is b)
```
### where
vectorized conditional
```python
a = np.arange(4).reshape(2,2)
b = np.where(a >=2, -1, 1)
# b = array([[ 1,  1],
#            [-1, -1]])
```
## operations
### simple math
+, -, *, ** .... (with broadcasting)
### bool
**all()** - if all elements are True  
**any()** - if any element is True  
Counting True's and False's or positive and negative values:
```python
(a > 0).sum() # number of positive/True values
(a <= 0).sum() # number of negative/False values
```
### copy
view
```python
a = np.arange(4).reshape(2,2)
b = a.view()   # b is view of a, changes to b affect a 
``` 
copy will make deep copy of an array or...
```python
a = np.arange(4).reshape(2,2)
b = a.copy()  # a.copy() is like np.array(a, copy=True) 
```
use **base** to check  
```python
x = np.array([1,2,3,4])
x.base is None   # True - copy or array
y = x[2:]
y.base is x   # True - view
```
The numpy.reshape function creates a view where possible or a copy otherwise  
Slicing creates a view  
### manipulating
**indexing**
```python
a[0, 2] == a[0][2]  # first is more efficient !
```
**slicing** will give view instead of copy
```python
a = np.arange(4).reshape(2,2)
b = a[:,:]            # view (shallow copy)
c = a[:,:].copy()     # deep copy
# a = b = c = array([[0, 1],
#                   [2, 3]])
b[0, 2] = 66
# a = b = array([[ 0, 66],
#                [ 2,  3]])
```
**fancy indexing** - choosing elements by index
```python
# just indices
a = np.arange(4)  # a = array([0, 1, 2, 3])
b = a[[1,2]]      # b = array([1, 2])
# lists of 'coordinates' !!!
a = np.arange(4).reshape(2,2)
# a = array([[0, 1],
#            [2, 3]])
b = a[[1],[1]]  # b = array([3])
```
**concatenate**
concatenate or use:  
hstack, vstack, row_stack, column_stack, dstack  

**splitting**  
hsplit, vsplit, split

**helpers**  
r_, c_  

### expand
np.expand_dims() or with np.newaxis (=None) -  with slices

### mask
```python
a = np.array([[1, 5],[3, 6]])
# a = array([[1, 5],
#            [3, 6]])
m = a > 1
# m = array([[False,  True],
#            [ True,  True]])
b = a[a > 1]
# b = array([5, 3, 6])
```
```python
a = np.array([[0, 5],[3, 6]])
b = a[np.nonzero(a)]
# b = array([5, 3, 6])
```
### math and statistics
**sum** -  Sum of all the elements in the array or along an axis; zero-length arrays have sum 0  
**mean** -  Arithmetic mean; invalid (returns NaN) on zero-length arrays  
**std**, **var** -  Standard deviation and variance, respectively
**min**, **max** -  Minimum and maximum
**argmin**, **argmax** -  Indices of minimum and maximum elements, respectively
**cumsum** -  Cumulative sum of elements starting from 0  
**cumprod** -  Cumulative product of elements starting from 1

### sort
```python
import numpy as np
from numpy.random import default_rng
np.set_printoptions(precision=2)
rng = default_rng()
v = rng.standard_normal(10)
# v = array([ 0.82,  0.43,  0.81,  1.2 ,  1.78, -0.59,  0.85, -0.74, -1.12,
#             0.84])
v.sort()  # in-place!
# v = array([-1.12, -0.74, -0.59,  0.43,  0.81,  0.82,  0.84,  0.85,  1.2 ,
#             1.78]) 
```
```python
ndarray.sort(axis=-1, kind=None, order=None)

numpy.sort(a, axis=-1, kind=None, order=None)
# axis - None: flatten, -1: last axis or axis index
# kind - ‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’, default is quickrort = None
```
argsort, lexsort, partition, argpartition, searchsort

### reverse
```python
b = np.flip(a)
```
flipud, flipr

### universal functions
vectorizing wrapper for simple functions  
[ufunc](vectorizing wrapper for simple functions)  
[Defined functions](https://numpy.org/doc/stable/reference/ufuncs.html?highlight=universal#available-ufuncs)  

## print options
These [options](https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html#numpy-set-printoptions) determine the way floating point numbers, arrays and other NumPy objects are displayed.  
```python
numpy.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, suppress=None, nanstr=None, infstr=None, formatter=None, sign=None, floatmode=None, *, legacy=None)
```
Other [formatting options](https://numpy.org/doc/stable/reference/routines.io.html#text-formatting-options)...  
## structured arrays
Generally rather use Pandas... unless some special cases...

## files
[files...](https://numpy.org/doc/stable/reference/routines.io.html?highlight=file#numpy-binary-files-npy-npz)  
np.save, np.savez, np.savetxt, np.load, np.loadtxt

## Modules
### numpy.fft
Discrete Fourier Transform - [numpy.fft](https://numpy.org/doc/stable/reference/routines.fft.html)  
Use [scipy.fft](https://docs.scipy.org/doc/scipy/reference/fft.html#module-scipy.fft). It is more comprehensive.  
### numpy.linalg
Linear algebra - [numpy.linalg](https://numpy.org/doc/stable/reference/routines.linalg.html)  
Matrices and vectors operations.   
@ - numpy.matmul

### numpy.matlib
Matrix library [numpy.matlib](https://numpy.org/doc/stable/reference/routines.matlib.html) - 2D array !!!    
[*numpy.matrix*](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#) - ***It is no longer recommended to use this class, even for linear algebra. Instead, use regular arrays. The class may be removed in the future.***  

matrix vs array:  
1. matrix is 2D, always !!!
2. \* for matrices is product, for array is an element-wise operation, for array use @ etc...

### numpy.polynomial
Polynomials: power series and other... - [numpy.polynomial](https://numpy.org/doc/stable/reference/routines.polynomials.html)  
Power series - [numpy.polynomial.polynomial](https://numpy.org/doc/stable/reference/routines.polynomials.polynomial.html) - adding, multiplying, ...,differentiate, integrate, roots, ...  

*Legacy: numpy.poly1d*  
### numpy.random
Random sampling [numpy.random](https://numpy.org/doc/stable/reference/random/index.html)  
**random generator** - numpy.random.default_rng() - returns new Generator with the default BitGenerator (PCG64)
```python
from numpy.random import default_rng
rng = default_rng()
vals = rng.standard_normal(10)
# this is equivalent for
from numpy.random import Generator, PCG64
rng = Generator(PCG64())  # PCG64DXSM is better for heavily-parallel use cases.
vals = rng.standard_normal(10)
# with seed
rng = default_rng(seed=12345)
```
Default seed is generated using entropy (128-bit) gathered from the OS. Also could be used:
```python
SeedSequence(entropy)  # entropy -> 128bit  
secrets.randbits(128)
```
simple
```python
rng.integers(low[, high, size, dtype, endpoint])  # array of integers, high is exclusive
```
```python
rng.random([size, dtype, out])  # array of floats, interval [0.0, 1.0)
```
```python
rng.choice(a[, size, replace, p, axis, shuffle])  # random sample from array
```
```python
rng.bytes(length)  # random sequence of bytes
```

permutations
```python
rng.shuffle(x[, axis])  # shuffle given sequence, in-place !!!
```
```python
rng.permutation(x[, axis])  # permuted sequence or range    , copy !!!
```
```python
rng.permuted(x[, axis, out])  # permuted sequence, each row or column(axis) independently, either(out)
```  
axis?

[Distributions](https://numpy.org/doc/stable/reference/random/generator.html#distributions)  
```python
rngstandard_normal([size, dtype, out])  # normal dist. mean=0, stdev=1
...
```

### numpy.testing
Test support [numpy.testing](https://numpy.org/doc/stable/reference/routines.testing.html)  

for example:  
```python
numpy.testing.assert_allclose(actual, desired, rtol=1e-07, atol=0, equal_nan=True, err_msg='', verbose=True)
```

[Testing guidlines](https://numpy.org/doc/stable/reference/testing.html)  

### numpy.typing
Type annotations - [numpy.typing](https://numpy.org/doc/stable/reference/typing.html)  
