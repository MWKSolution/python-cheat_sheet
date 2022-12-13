
Numpy:
more speed
fewer loops


NumPy ndarrays are fixed size
All elements are of the same type

vectorization - same operation for each element - removes for loops

Axes
```
 | axis=0                         axis=1 ------>
 |  
 |  
\ /
```

### data types
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
|                 |                                        |                                              |      |
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




object_
void
str_
unicode_


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