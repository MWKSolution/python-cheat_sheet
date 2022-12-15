# NumPy data types 
(depends on platform!)

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
