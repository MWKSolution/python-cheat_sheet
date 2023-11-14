# Exceptions
<!-- TOC -->
* [Exceptions](#exceptions)
  * [Raising exceptions](#raising-exceptions)
  * [Catching exceptions](#catching-exceptions)
  * [Traceback](#traceback)
    * [frame, linecache](#frame-linecache)
    * [excepthook](#excepthook)
  * [Warnings](#warnings)
  * [Base Exception Classes](#base-exception-classes)
  * [Links](#links)
<!-- TOC -->

## Raising exceptions
```python
raise Exception
raise Exception from None           # same as previous       
raise Exception from e              # set cause
raise Exception.with_traceback(tb)  # use given traceback
# Exception.add_note() 3.11
sys.exit([arg])
raise SystemExit(arg)
```
## Catching exceptions
```python
try:
    raise Exception('error') from err
except Exception as exc:
    # attributes of exc:
    exc.__cause__ # <class 'Exception'> | exception if from err was specified or None None
    exc.__class__ # <class 'type'> | <class 'Exception'> ; error class with __name__
    exc.__context__ # <class 'Exception'> | exception if error was rised during handling other exception or None None
    exc.__doc__ # <class 'str'> | Common base class for all non-exit exceptions - additional description
    exc._traceback__ # <class 'traceback'> | <traceback object at 0x00000...........>
    exc.args # <class 'tuple'> | ('error',)
    # referring directly to err
    str(err) # -> str(err.args[0]) if one argument, str(tuple) if more; this informatio is shown when not caought
    # __notes__ 3.11
```

## Traceback
```python
import traceback as tbm
import sys
...
except Exception as exc:
    ...
    exc_tb = exc.__traceback__ # traceback from exception
    exc_type_i, exc_i, exc_tb_i = sys.exc_info() # information on exc type exc and traceback
    
    tbm.print_exc(limit=None, file=None, chain=True) # print last exception as interpreter does
    # or...
    tbm.print_exception(type(exc), exc, exc_tb, file=sys.stderr, chain=True)
    tbm.print_exception(exc_type_i, exc_i, exc_tb_i)  # these three have the same effect
    tbm.print_exception(*sys.exc_info())
    # sys.exception() - 3.11
```

### frame, linecache
```python
import linecache
tb = exc.__traceback__ # or sys.exc.info()
file_name = tb.tb_frame.f_code.co_filename  # python file name wher exception occured
func_name = tb.tb_frame.f_code.co_name  # name of the function where exception occured or <module>
line_no = tb.tb_lineno  # line number in file
line = linecache.getline(file_name, line_no)  # get line of code at line_no
tb = tb.tb_next  # get next frame in stack
```


### excepthook
Alternative way to handle/print exception info...
```python
import sys
 def exception_hook(exc_type: type, exc_value: BaseException, trace_back: TracebackType) -> None:
    pass
sys.excepthook = exception_hook
```

## Warnings
Issue warning:
```python
import warnings

warnings.warn('message',DeprecationWarning)
```
Formatting warnings:
```python
import warnings
import pathlib as ptb

def warning_format(message, category, filename, lineno, line=None):
    return f'{ptb.Path(filename).stem}:{lineno} >> {category.__name__}: {message}\n'

warnings.formatwarning = warning_format
```
Custom warning:
```python
class CustomWarning(Warning):
    pass
```
Filtering warnings:

```python
import warnings

warnings.simplefilter("ignore", DeprecationWarning)
# "default", "error", "ignore", "always", "module", "once"
```

## Base Exception Classes
```text
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```
## Links
[Example](../.examples/traceback/test_tb.py)

[Creating Beautiful Tracebacks with Python's Exception Hooks](https://martinheinz.dev/blog/66)
