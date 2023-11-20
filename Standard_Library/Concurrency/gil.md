## The Python GIL
The mechanism used by the CPython interpreter to assure that **only one thread executes** Python bytecode at a time.  

GIL improvements:
- 3.2 : The mechanism for serializing execution of concurrently running Python threads (generally known as the GIL or Global Interpreter Lock) has been rewritten. Among the objectives were more predictable switching intervals and reduced overhead due to lock contention and the number of ensuing system calls. The notion of a “check interval” to allow thread switches has been abandoned and replaced by an absolute duration expressed in seconds. This parameter is tunable through sys.setswitchinterval(). It currently defaults to 5 milliseconds. [see](https://mail.python.org/pipermail/python-dev/2009-October/093321.html)
- 3.6 : Checking if the GIL is held
- 3.12 : A Per-Interpreter GIL. sub-interpreters may now be created with a unique GIL per interpreter. This allows Python programs to take full advantage of multiple CPU cores.
```python
import sys
sys.getswitchinterval()  # Set the interpreter’s thread switch interval (in seconds).
# default 0.005
sys.setswitchinterval()  # Get the interpreter’s thread switch interval
```
get number of logical processors
```python
os.cpu_count()
multiprocessing.cpu_count()
```
physical is about n/2 because of hyper-threading
