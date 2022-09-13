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
4. Useful stuff

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
### Change current dir
```python
os.chdir(dir)
```

## Archiving - shutil.make_archive(), shutil_unpack_archive()
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
open()
.read_text(): open the path in text mode and return the contents as a string.
.read_bytes(): open the path in binary/bytes mode and return the contents as a bytestring.
.write_text(): open the path and write string data to it.
.write_bytes(): open the path in binary/bytes mode and write data to it.
Each of these methods handles the opening and closing of the file, making them trivial to

---

## Useful stuff
shutil.disk_usage(path)

PYTHONPATH:
sys.path


module path : **\_\_file\_\_**

---
