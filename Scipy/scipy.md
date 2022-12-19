# SciPy

1. [cluster](#cluster)
2. [constants](#constants)
3. [fft](#fft)
4. [integrate](#integrate)
5. [interpolate](#interpolate)
6. [io](#io)
7. [linalg](#linalg)
   1. [scipy.linalg vs numpy.linalg](#scipylinalg-vs-numpylinalg)
8. [ndimage](#ndimage)
9. [odr](#odr)
10. [optimize](#optimize)
    1. [root finding](#root-finding)
11. [signal](#signal)
12. [sparse](#sparse)
13. [spatial](#spatial)
    1. [spatial transformations](#spatial-transformations)
14. [special](#special)
15. [stats](#stats)

---

## cluster
Clustering algorithms, scipy.cluster  
[scipy.cluster.vq](scipy.cluster.hierarchy)  
[scipy.cluster.hierarchy](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html#module-scipy.cluster.hierarchy)  
## constants
Physical and mathematical constants  
[scipy.constans](https://docs.scipy.org/doc/scipy/reference/constants.html#module-scipy.constants)
## fft
Fast Fourier Transform routines  
[scipy.fft](https://docs.scipy.org/doc/scipy/reference/fftpack.html#module-scipy.fftpack)
## integrate
Integration and ordinary differential equation solvers  
[scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate)
## interpolate
Interpolation and smoothing splines  
[scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/interpolate.html#module-scipy.interpolate)  
## io
Input and Output
[scipy.io](https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io)  
## linalg
Linear algebra.  
numpy.linalg for more linear algebra functions. Note that although scipy.linalg imports most of them, identically named functions from scipy.linalg may offer more or slightly differing functionality.  
### scipy.linalg vs numpy.linalg
scipy.linalg contains all the functions in numpy.linalg. plus some other more advanced ones not contained in numpy.linalg.  
Another advantage of using scipy.linalg over numpy.linalg is that it is always compiled with BLAS/LAPACK support, while for numpy this is optional.  
Therefore, the scipy version might be faster depending on how numpy was installed. Therefore, unless you don’t want to add scipy as a dependency to your numpy program, use scipy.linalg instead of numpy.linalg.  
[scipy.linalg guide](https://docs.scipy.org/doc/scipy/tutorial/linalg.html)  
[scipy.linalg_API](https://docs.scipy.org/doc/scipy/reference/linalg.html#module-scipy.linalg)
## ndimage
N-dimensional image processing  
[scipy.ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html#module-scipy.ndimage)  
## odr
Orthogonal distance regression  
[scipy.odr](https://docs.scipy.org/doc/scipy/reference/odr.html#module-scipy.odr)  
## optimize
Optimization and root-finding routines  
SciPy optimize provides functions for minimizing (or maximizing) objective functions, possibly subject to constraints. It includes solvers for nonlinear problems (with support for both local and global optimization algorithms), linear programing, constrained and nonlinear least-squares, root finding, and curve fitting.  
[scipy.optimize_guide](https://docs.scipy.org/doc/scipy/tutorial/optimize.html)  
[scipy.optimize_API](https://docs.scipy.org/doc/scipy/reference/optimize.html)  
### root finding
[refrence](https://docs.scipy.org/doc/scipy/reference/optimize.html#root-finding)    
[tutorial](https://docs.scipy.org/doc/scipy/tutorial/optimize.html#root-finding)  
## signal
Signal processing  
[scipy.signal](https://docs.scipy.org/doc/scipy/reference/signal.html#module-scipy.signal)  
## sparse
Sparse matrices and associated routines  
[scipy.sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse)  
## spatial
Spatial data structures and algorithms  
[scipy.spatial](https://docs.scipy.org/doc/scipy/tutorial/spatial.html)  
### spatial transformations
This package implements various spatial transformations. For now, only **rotations** are supported.  
[scipy.spatial.transform](https://docs.scipy.org/doc/scipy/reference/spatial.transform.html#module-scipy.spatial.transform)  
## special
Special functions  
[scipy.special](https://docs.scipy.org/doc/scipy/reference/special.html#module-scipy.special)  
## stats
Statistical distributions and functions  
[scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats)  
This module contains a large number of probability distributions, summary and frequency statistics, correlation functions and statistical tests, masked statistics, kernel density estimation, quasi-Monte Carlo functionality, and more.  
Statistics is a very large area, and there are topics that are out of scope for SciPy and are covered by other packages. Some of the most important ones are:
+ [statsmodels](https://www.statsmodels.org/stable/index.html): regression, linear models, time series analysis, extensions to topics also covered by scipy.stats.
+ [Pandas](https://pandas.pydata.org/): tabular data, time series functionality, interfaces to other statistical languages.
+ [PyMC](https://www.pymc.io/projects/docs/en/stable/learn.html): Bayesian statistical modeling, probabilistic machine learning.
+ [scikit-learn](https://scikit-learn.org/stable/): classification, regression, model selection.
+ [Seaborn](https://seaborn.pydata.org/): statistical data visualization.
+ [rpy2](https://rpy2.github.io/): Python to R bridge.


---