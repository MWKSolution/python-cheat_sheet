# pytest

---

pytest.ini

conftest.py - shared fixtures across directory

monkeypatch - fixture to replace values and behaviors


monkeypatch.setattr modyfiing behaviour of function


[docs.pytest.org](https://docs.pytest.org/en/7.2.x/how-to/index.html)

## Invoke pytest
```shell
pytest test_mod.py                  # run module
pytest testing/                     # run from directory
pytest -k "MyClass and not method"  # by keyword
pytest test_mod.py::test_func       # specific test
pytest -m slow                      # by set marker
pytest -x                           # stop after first failure
pytest -v                           # verbosity -v -vv
```
```shell
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
```
```shell
pytest --durations=10 --durations-min=1.0   # To get a list of the slowest 10 test durations over 1.0s long
pytest --maxfail=2                          # stop after two failures
```
## Basic
```python
def f():
    return 3

def test_function():
    assert f() == 4
```
## Expected errors
```python
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()
        f()
    assert "maximum recursion" in str(excinfo.value)
```
```python
def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
```
## Fixture
```python
@pytest.fixture
def fixture():
    return 1

def test_with_fixture(fixture):
    assert fixture == 1
```
Fixtures can request other fixtures  
Fixtures are reusable  
A test/fixture can request more than one fixture at a time  
Fixtures can be requested more than once per test (return values are cached)  
Autouse fixtures (fixtures you don’t have to request):  
```python
@pytest.fixture(autouse=True)
def fixture():
    return 1

def test_with_fixture():
    assert fixture ==1
```
scope - create fixture once per scope:
```python
@pytest.fixture(scope='module')  # scope= function (default!!!), class, module, package, session - could set dynamically
def fixture():
    return 1
```
Adding terar down code - yield
```python
@pytest.fixture()
def fixture():
    yield 1
    ...
```
## Marks
### usefixtures
### filterwarnings
```python
def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1

@pytest.mark.filterwarnings("ignore:api v1")
def test_one():
    assert api_v1() == 1
```
### skip
skips a test unconditionally   
```python
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    ...
```
```python
...
if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)
...
```
### skipif
skips a test if the expression passed to it evaluates to True
```python
@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_function():
```
### xfail
indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.  
### parametrize
creates multiple variants of a test with different values as arguments. You’ll learn more about this mark shortly.  
```python
import pytest

@pytest.mark.parametrize('value1, value2, result', [(1 ,2, 3), (2, 2, 4), (3, 2, 5)])
def test_function(value1, value2, result):
    assert value1 + value2 == result
```
## Temporary dirs and files
...
## Monkeypatch
### monkeypatch.setattr
monkeypatch.setattr(obj, name, value, raising=True)  
monkeypatch.delattr(obj, name, raising=True)  
Modifying the behavior of a function or the property of a class for a test e.g. there is an API call or database connection you will not make for a test but you know what the expected output should be. Use monkeypatch.setattr to patch the function or property with your desired testing behavior. This can include your own functions. Use monkeypatch.delattr to remove the function or property for the test.  

### monkeypatch.setitem
monkeypatch.setitem(mapping, name, value)  
monkeypatch.delitem(obj, name, raising=True)  
Modifying the values of dictionaries e.g. you have a global configuration that you want to modify for certain test cases. Use monkeypatch.setitem to patch the dictionary for the test. monkeypatch.delitem can be used to remove items.  


### monkeypatch.setenv
monkeypatch.setenv(name, value, prepend=None)  
monkeypatch.delenv(name, raising=True)  
Modifying environment variables for a test e.g. to test program behavior if an environment variable is missing, or to set multiple values to a known variable. monkeypatch.setenv and monkeypatch.delenv can be used for these patches.  
Use monkeypatch.setenv("PATH", value, prepend=os.pathsep) to modify $PATH  


### monkeypatch.syspath_prepend
monkeypatch.syspath_prepend(path)  
Use monkeypatch.syspath_prepend to modify sys.path which will also call pkg_resources.fixup_namespace_packages and importlib.invalidate_caches().  


### monkeypatch.chdir
monkeypatch.chdir(path)
Use monkeypatch.chdir to change the context of the current working directory during a test.  


### monkeypatch
monkeypatch.context()  
Use monkeypatch.context to apply patches only in a specific scope, which can help control teardown of complex fixtures or patches to the stdlib.  


## Plugins
pytest-randomly  forces your tests to run in a random order  
pytest-cov integrates coverage into pytest use pytest --cov=project tests/  
pytest-django  
pytest-bdd   helps you use Gherkin to write feature tests for your code  
## Output
```shell
pytest --showlocals     # show local variables in tracebacks
pytest -l               # show local variables (shortcut)
pytest --no-showlocals  # hide local variables (if addopts enables them)

pytest --tb=auto    # (default) 'long' tracebacks for the first and last
                     # entry, but 'short' style for the other entries
pytest --tb=long    # exhaustive, informative traceback formatting
pytest --tb=short   # shorter traceback format
pytest --tb=line    # only one line per failure
pytest --tb=native  # Python standard library formatting
pytest --tb=no      # no traceback at all
```



