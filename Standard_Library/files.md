# Files and paths

1. Paths and files operations
   1. List directories - iterdir()
   2. file stats - stat()
   3. Create dir - mkdir()
   4. Pattern matching - glob()
   5. Traversing directories - rglob()
   6. Temporary files - tempfile
   7. Deleting - unlink(), rmdir(), shutil.rmtree()
   8. Copy - shutil.copy(), shutil.copy2, shutil.copytree
   9. Move - shutil.move(), replace()
   10. Rename - rename()
   11. Change current dir
2. Pathlib
   1. properties
   2. methods
3. Read and write
   1. Built-in open()
   2. File methods
   3. Custom context manager
   4. pathlib methods
4. Memory streams/files
   1. text
   2. binary
5. Useful stuff
6. High level file handling

---

## Paths and files operations

### List directories - iterdir()
Old:
```python
import os
os.listdir() # - list
os.scandir() # - iterator
```
Pathlib:
```python

import pathlib as plb

pth = plb.Path('Standard_Library') / 'collections'
i = pth.iterdir()  # generator
l = list(i)
# l = [WindowsPath('Standard_Library/collections/ChainMap.md'), WindowsPath('Standard_Library/collections/Counter.md'), WindowsPath('Standard_Library/collections/defaultdict.md'), WindowsPath('Standard_Library/collections/namedtuple.md')]
i = pth.iterdir()  # generator
ll = [p.name for p in i]
# ll = ['ChainMap.md', 'Counter.md', 'defaultdict.md', 'namedtuple.md']
```
```python
# only files
i = pth.iterdir()  # generator
ll = [p.name for p in i if p.is_file()]
# same result
```
only directories:
```python
pth = plb.Path('Standard_Library')
i = pth.iterdir()
l = [p.name for p in i if p.is_dir()]
# l = ['built_ins', 'collections', 'types']
```
### File stats - stat()
Old:
```python
os.stat()
```
Pathlib:
```python
import pathlib as plb
from  datetime import datetime

pth = plb.Path('Standard_Library') / 'files.md'

st = pth.stat()  
# st = os.stat_result(st_mode=33206, st_ino=18577348463954686, st_dev=1423301669, st_nlink=1, st_uid=0, st_gid=0, st_size=2994, st_atime=1662907784, st_mtime=1662986825, st_ctime=1662907784)
sz = st.st_size
# sz = 2994
tm = str(datetime.fromtimestamp(st.st_mtime))
tm = '2022-09-12 14:47:05.405970'
```
### Create dir - mkdir()
Old:
```python
os.mkdir()
os.makedirs()
```
Pathlib:
```python
import pathlib as plb

new = plb.Path('new_directory')
try:
    new.mkdir()
except FileExistsError as exc:
    print(exc)

# or: no errors and  multiple dirs
new = plb.Path('new_parent/new_directory')
new.mkdir(parents=True, exist_ok=True)
```
### Pattern matching - glob()
Old:

```python
fnmatch.fnmatch()
glog.glob()
```
Pathlib:
```python
import pathlib as plb

pth = plb.Path('Standard_Library')
g = pth.glob('*.md')
l = [p.name for p in g]
# l = ['built_ins.md', 'collections.md', 'context_manager.md', 'decorator.md', 'files.md', 'functools.md', 'iterator.md', 'itertools.md', 'math.md', 'operator.md', 'string.md', 'types.md']
```
Some like re + **(dirs):
wildcards: *, ?, [seg], [!seq], ** for dirs
```python
import pathlib as plb

pth = plb.Path('Standard_Library')
g = pth.glob('**/*o*r*.md')
l = [p.name for p in g]
# l = ['context_manager.md', 'decorator.md', 'iterator.md', 'operator.md', 'iterators.md', 'Counter.md', 'dictionary.md']
```

### Traversing directories - rglob()
Old:
```python
os.walk()
```
Pathlib:
```python
import pathlib as plb

pth = plb.Path('Standard_Library')
g = pth.rglob('**/*')
l = [p.name for p in g]
# l = ['built_ins', 'built_ins.md', 'collections', 'collections.md', 'context_manager.md', 'decorator.md', 'files.md', 'functools.md', 'iterator.md', 'itertools.md', 'math.md', 'operator.md', 'string.md', 'types', 'types.md', 'boolean.md', 'class.md', 'code.md', 'general.md', 'iterators.md', 'objects.md', 'scope.md', 'ChainMap.md', 'Counter.md', 'defaultdict.md', 'namedtuple.md', 'bytes.md', 'dictionary.md', 'list.md', 'set.md', 'tuple.md']
```

### Temporary files - tempfile
```python
from tempfile import TemporaryFile, gettempdir

td = gettempdir()      # td = 'C:\\Users\\PC\\AppData\\Local\\Temp' - dir for temps
tmp = TemporaryFile()
tmp.write(b'xxx')
tmp.seek(0)
data = tmp.read()      # data = b'xxx'
tmp.close() # or use context manager
# file will be deleted after that !!!
```
```python
from tempfile import TemporaryDirectory
import pathlib as plb

with TemporaryDirectory() as tmpdir:
    tmppth = plb.Path(tmpdir)  
    # tmppth = WindowsPath('C:/Users/PC/AppData/Local/Temp/tmps_q8kvfg')
# Now temporary dir is deleted !
```
### Deleting - unlink(), rmdir(), shutil.rmtree()
Old:
```python
os.remove()
os.unlink()
os.rmdir()
```
Pathlib:
```python
import pathlib as plb
pth = plb.Path('something')
try: 
    pth.unlink(missing_ok=False)
except IsADirectoryError as e:
    pth.rmdir()  # dir must be empty
except  FileNotFoundError as e:
    pass   # file not found
```
Whole dir:
```python
import pathlib as plb
import shutil
pth = plb.Path('something')
shutil.rmtree(pth)
```
Recursively:  
Use **rglob()**  

### Copy - shutil.copy(), shutil.copy2, shutil.copytree
```python
import shutil as sht
sht.copy('src', 'dst')
```
Preserve metadata  
```python
import shutil as sht
sht.copy2('src', 'dst')
```
copy directory
```python
import shutil as sht
sht.copytree('srcdir', 'dstdir')
```
### Move - shutil.move(), replace()
for safe move use shutil.move !
```python
import shutil as sht
sht.move('srcordir', 'dstordir')
```
```python
if not destination.exists():
    source.replace(destination)
# or safer:
with destination.open(mode='xb') as fid:
    fid.write(source.read_bytes())
```
### Rename - rename(), (with_suffix(), with_name())
Old:
```python
os.rename()
```
Pathlib:
```python
import pathlib as plb
pth = plb.Path('old.name')
pth.rename('new.name')
```

### Archiving - shutil.make_archive(), shutil_unpack_archive()
Old:
```python
zipfile
tarfile
```
Shutil:
```python
import shutil as sht
a = [f[0] for f in shutil.et_archive_formats()]
# a = ['bztar', 'gztar', 'tar', 'xztar', 'zip']
b = [f[1] for f in shutil.get_unpack_formats()]
# b = [['.tar.bz2', '.tbz2'], ['.tar.gz', '.tgz'], ['.tar'], ['.tar.xz', '.txz'], ['.zip']]
import shutil as sht
sht.make_archive('arch', 'tar', 'Standard_Library')
sht.unpack_archive('arch.tar', 'somedir')
```
### Change current dir
```python
os.chdir(dir)
```


---

## Pathlib
[pathlib...](https://docs.python.org/3/library/pathlib.html)

```python
import pathlib

current_dir = pathlib.Path.cwd()
# current_dir = WindowsPath('C:/.../cheat_sheet')
home_dir = pathlib.Path.home()
# home_dir = WindowsPath('C:/Users/PC')
p = str(current_dir)
# p = 'C:\\PYTHON_ORG\\Projects\\cheat_sheet'
```

### properties
**drive**:  
a string that represents the drive name. For example, PureWindowsPath('c:/Program Files/CSV').drive returns "C:"  
**parts**:  
returns a tuple that provides access to the path's components  
**name**:  
the path component without any directory  
**parent**:  
sequence providing access to the logical ancestors of the path  
**stem**:  
final path component without its suffix  
**suffix**:  
the file extension of the final component  
**anchor**:  
the part of a path before the directory. / is used to create child paths and mimics the behavior of os.path.join.  

**root**, **parents**, **suffixes**,
### methods
**cwd()**:  
Return path object representing the current working directory  
**home()**:  
Return path object representing the home directory  
**stat()**:  
return info about the path  
**chmod()**:  
change file mode and permissions  
**glob(pattern)**:  
Glob the pattern given in the directory that is represented by the path, yielding matching files of any kind
**mkdir()**:  
to create a new directory at the given path  
**open()**:  
To open the file created by the path  
**rename()**:  
Rename a file or directory to the given target  
**rmdir()**:  
Remove the empty directory  
**unlink()**:  Remove the file or symbolic link  
**joinpath(\*other)**: combines the path with the arguments provided    
**match(pattern)**:  
returns True/False, based on matching the path with the glob-style pattern provided  

**exists()**, **expanduser()**,  **group()**, is_dir(), is_file(), is_mount(), is_symlink(), is_socket(), is_fifo(), is_block_device(), is_char_device(), iterdir(), lchmod(), lstat(), owner(), read_bytes(), read_text(), readlink(), rename(), replace(), resolve(), rglob(), rmdir(), samefile(other_path), symlink_to(), hardlink_to(), link_to(), touch(), unlink(), write_bytes(), write_text()   

**as_posix()**, **as_uri()**, **is_absolute()**, **is_relative_to()**, **is_reserved()**,  **relative_to()**, **with_name()**, **with_stem()**, **with_suffix()**  

---

## Read and write
### Built-in open()
Buit-in **open()** calls **io.open()**  
**open**(*file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None*)  
File type:  
**t - text** - encoding must be specified, by default: None - got from locale.getpreferredencoding.  
**b - binary**  - no coding, decoding  
*mode:*  
```
r:
r, rt, rb     only for reading, file must exists – pointer at the beginning. This is the default mode.
r+, rt+, rb+  for both reading and writing. pointer at the beginning of the file.
w:
w, wt, wb     writing only. Overwrites if the file exists. If does not exist, creates a new file for writing.
w+, wt+, wb+  for both writing and reading. Overwrites if the file exists. If does not exist, it creates a new file for reading and writing.
a, at, ab     for writing - like w. pointer is at the end if the file exists. If does not exist, it creates a new file for writing.
a+, at+, ab+  for both writing and reading - like w+. pointer is at the end if file exists. If does not exist, it creates a new file for reading and writing.
x, xt, xb     open for writing, -  like w - if file exists - error.
x+, xt+, xb+  open for reading and writing, -  like w+ - if file exists - error.
```
*encodng:*  
[Standard encodings...](https://docs.python.org/3/library/codecs.html#standard-encodings)  
```python
import locale
e = locale.getpreferredencoding()  # e = 'cp1250'
```
*errors:*  
strict, ignore, replace,xmlcharrefreplace, backslashreplace, namereplace  

*newline:*
```
None   - reading - universal newline, return translated to '\n' 
       - writing - '\n' - translated to system default newline,  
''     - reading - universal newline, return untranslated
       - writing - no translation
'\n'   - reading - '\n' newline, return untranslated
       - writing - no translation
'\r'   - reading - '\r' newline, return untranslated
       - writing - '\n' translated to '\r'
'\r\n' - reading - '\r\n' newline, return untranslated
       - writing - '\n' translated to '\r\n'
```
```python
import os
s = os.linesep  # s = '\r\n'
```
Universal newlines:
```
\n          Line Feed                     Unix
\r          Carriage Return               Macintosh
\r\n        Carriage Return + Line Feed   Windows
\v or \x0b  Line Tabulation
\f or \x0c  Form Feed
\x1c        File Separator
\x1d        Group Separator
\x1e        Record Separator
\x85        Next Line (C1 Control Code)
\u2028      Line Separator
\u2029      Paragraph Separator
```
*buffering:*  
```
0  - buffering switched off, only binary
1  - line buffering, only text
>1 - size of buffer, only for binary
-1 - binary:  io.DEFAULT_BUFFER_SIZE - device blocksize
   - text: like binary, isatty() = True - linebuffer
```
### File Methods
io inherited types: 
```python
with open('text.txt', 'r') as f:
    t = type(f)  # t = <class '_io.TextIOWrapper'> - it is random and buffered
with open('bin.bin', 'rb') as f:
    t = type(f)  # t = <class '_io.BufferedReader'>
with open('bin.bin', 'wb') as f:
    t = type(f)  # t = <class '_io.BufferedWriter'>
with open('bin.bin', 'rb+') as f:
    t = type(f)  # t = <class '_io.BufferedRandom'>
```
Text methods inherited from *<class '_io.TextIOWrapper'>*  
```python
f = open('text.txt', 'r')
f.close()          # Closes an opened file. It has no effect if the file is already closed.
f.detach()         # Separates the underlying binary buffer from the TextIOBase and returns it.
f.fileno()         # Returns an integer number (file descriptor) of the file.
f.flush()          # Flushes the write buffer of the file stream.
f.isatty()         # Returns True if the file stream is interactive.
f.read(n)          # Reads at most n characters from the file. Reads till end of file if it is negative or None.
f.readable()       # Returns True if the file stream can be read from.
f.readline(n=-1)   # Reads and returns one line from the file. Reads in at most n bytes if specified.
f.readlines(n=-1)  # Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
f.seek(offset, whence=SEEK_SET)
# Changes the file position to offset bytes, in reference to from (start, current, end).
# SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive
# SEEK_CUR or 1 – current stream position; offset may be negative
# SEEK_END or 2 – end of the stream; offset is usually negative
f.seekable()       # Returns True if the file stream supports random access.
f.tell()           # Returns an integer that represents the current position of the file's object.
f.truncate(size=None)  # Resizes the file stream to size bytes. If size is not specified, resizes to current location.
f.writable()       # Returns True if the file stream can be written to.
f.write(s)         # Writes the string s to the file and returns the number of characters written.
f.writelines(lines)# Writes a list of lines to the file.
```
Rest of the text attributes and methods:  
```python
f = open('text.txt', 'r')
f.encoding
f.errors
f.newlines
f.buffer
f.closed
f.__del__()
f.line_buffering
f.write_through
f.reconfigure()
```
Binary methods:  
Methods inherited from:  
<class '_io.BufferedReader'>, 
<class '_io.BufferedWriter'>, 
<class '_io.BufferedRandom'>
```python
f = open('text.txt', 'rb+')
f.close()
f.closed
f.fileno()
f.flush()
f.isatty()
f.readable()
f.readline(size=- 1, /)
f.readlines(hint=- 1, /)
f.seek(offset, whence=SEEK_SET, /)
f.seekable()
f.tell()
f.truncate(size=None, /)
f.writable()
f.writelines(lines, /)
f.__del__()
f.raw
f.detach()
f.readinto(b, /)
f.readinto1(b, /)
f.write(b, /)
f.peek(size=0, /)
f.read(size=- 1, /)
f.read1(size=- 1, /)
f.flush()
f.write(b, /)
```
Reading all lines, iterating:  
```python
with open('text.txt', 'r') as f:
    # 1
    l1 = f.readlines()  # l1 - list of lines
    # 2
    l2 = list(f)        # same
    # 3
    l3 = []
    for line in f:
        l3.append(line) # l3 - list of lines
```
### Custom context manager
Custom context manager for opening png file with iterator...  
```python
class PngReader():
    # Every .png file contains this in the header.  Use it to verify
    # the file is indeed a .png.
    _expected_magic = b'\x89PNG\r\n\x1a\n'

    def __init__(self, file_path):
        # Ensure the file has the right extension
        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' extension")
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')

        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError("The File is not a properly formatted .png file!")

        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    def __iter__(self):
        # This and __next__() are used to create a custom iterator
        # See https://dbader.org/blog/python-iterators
        return self

    def __next__(self):
        # Read the file in "Chunks"
        # See https://en.wikipedia.org/wiki/Portable_Network_Graphics#%22Chunks%22_within_the_file

        initial_data = self.__file_object.read(4)

        # The file hasn't been opened or reached EOF.  This means we
        # can't go any further so stop the iteration by raising the
        # StopIteration.
        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            # Each chunk has a len, type, data (based on len) and crc
            # Grab these values and return them as a tuple
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc
```


### pathlib methods
```python
import pathlib
pth = pathlib.Path('text.txt')
with pth.open(mode='r') as f:
    pass
```
simple:
```python
import pathlib as plb
tpth = plb.Path('tetx.tx')
bpth = plb.Path('bin.bin')

tpth.write_text('text')   # 'wt' opens writes and closes
s = tpth.read_text()      # 'rt' opens reads and closes

bpth.write_bytes(b'bin')  # 'wb' opens writes and closes
b = bpth.read_bytes()     # 'rb' opens reads and closes
# encoding, error for text files, newlines for text writing
```

---
## Memory streams/files
### text
**StringIO**(*initial_value=''*, *newline='\n'*)  
A text stream using an in-memory text buffer.  
Methods:  
'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'getvalue', 'isatty', 'line_buffering', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'  

**getvalue()** - returns entire buffer - string.  
### binary
**BytesIO**(*initial_bytes=b''*)  
A binary stream using an in-memory bytes buffer.  
Methods:  
'close', 'closed', 'detach', 'fileno', 'flush', 'getbuffer', 'getvalue', 'isatty', 'read', 'read1', 'readable', 'readinto', 'readinto1', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'  

**getbuffer()** - returns buffer as a !!! **memoryview**  !!! for manipulating:  
```python
b = io.BytesIO(b"abcdef")
view = b.getbuffer()
view[2:4] = b"56"
x = b.getvalue()  # x = b'ab56ef'   
```
**getvalue()** - returns entire buffer - bytes.  

---

## Useful stuff
```python
import shutil
import sys

du = shutil.disk_usage(path)

_PYTHONPATH = sys.path

module_path = **\_\_file\_\_**
```

---

## High level file handling
```
csv                 - csv, pandas
json                - json
yaml                - PyYAML
configuration files - configparser
Excel               - xlwings
images              - Pillow
```
---
