# Itertools

1. Infinite
2. Terminating
3. Combinatoric
4. More-Itertools

[All itertools - python.org](https://docs.python.org/3/library/itertools.html)

---

## Infinite
Could be used with **next()**
### count()
Infinite counting  
```python
import itertools as it

i = it.count()
j = it.count(10, 2)
k = it.count(2.5, 0.5)

ii = list(zip(range(10), i))  
# ii = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
jj = list(zip(range(10), j))  
# jj = [(0, 10), (1, 12), (2, 14), (3, 16), (4, 18), (5, 20), (6, 22), (7, 24), (8, 26), (9, 28)]
kk = list(zip(range(10), k))  
# kk = [(0, 2.5), (1, 3.0), (2, 3.5), (3, 4.0), (4, 4.5), (5, 5.0), (6, 5.5), (7, 6.0), (8, 6.5), (9, 7.0)]
```
Use with **map()** or **zip()**  
When counting with floating point numbers, better accuracy can sometimes be achieved by substituting multiplicative code such as: (start + step * i for i in count()).  
### cycle()
### repeat()

---

## Terminating
### accumulate()
### chain()
### chain.from_iterable()
### compress()
### dropwhile()
### filterfalse()
### groupby()
### islice()
### pairwise()
### starmap()
### takewhile()
### tee()
### zip_longest()

---

## Combinatoric
### product()
Cartesian product  
```python

```
### permutations()
### combinations()
### combinations_with_replacement()

---

## More-Itertools
```
pip install more-itertools
```
For details see:  
[Itertools Recipes - python.org](https://docs.python.org/3/library/itertools.html#itertools-recipes)  
[more-itertools - pypi.org](https://pypi.org/project/more-itertools/)  
[API documentation - readthedocs.io](https://more-itertools.readthedocs.io/en/stable/api.html)  

[itertools as decorators](https://www.bbayles.com/index/decorator_factory)  
[itertools tour](https://martinheinz.dev/blog/16)  
[More itertools](https://www.gidware.com/real-world-more-itertools/)  

---
