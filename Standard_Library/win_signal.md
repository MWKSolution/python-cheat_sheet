## Sending CTRL_C_EVENT and CTRL_BREAK_EVENT signals in Windows 10

---

# Subprocess code
Dummy server code bundled with PyInstaller to **server.exe**
```python
import time
import os
import signal
import sys

def handler_int(sig, frame):
    print('Terminated by SIGINT', file=sys.stderr)
    sys.exit(101)

def handler_break(sig, frame):
    print('Terminated by SIGBREAK', file=sys.stderr)
    sys.exit(102)

def handler_term(sig, frame):
    print('Terminated by SIGTERM', file=sys.stderr)
    sys.exit(103)

signal.signal(signal.SIGINT, handler_int)
signal.signal(signal.SIGBREAK, handler_break)
signal.signal(signal.SIGTERM, handler_term)

def server():
    while True:
        time.sleep(0.5)
        print('logging...', os.getpid())
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == '__main__':
    server()
```
---
# 1. Console app and server

_MEI tmp files cleaned!

---
# CTRL_BREAK_EVENT
In Popen **process group** should be used!!!
```python
import subprocess as sp
import sys
import time
import signal
import os

po_object = sp.Popen(['dist/server.exe'], creationflags=sp.CREATE_NEW_PROCESS_GROUP)  # <-----
print('server started')
pid = po_object.pid
print(f'server.exe (pyinstaller) pid: {pid}')
time.sleep(3)
os.kill(pid, signal.CTRL_BREAK_EVENT)  # <----------------------------------------------------
po_object.wait(timeout=5)
print(f'Popen return code: {po_object.poll()}, pid={po_object.pid}' )
print('Stopped')
```
Output:
```commandline
server started
server.exe (pyinstaller) pid: 10588
logging...  server pid= 4088
logging...  server pid= 4088
logging...  server pid= 4088
Terminated by SIGBREAK
Popen return code: 102, pid=10588
Stopped
```
If...
```python
os.kill(0,signal.CTRL_BREAK_EVENT))
```
...is used it interrupts **parent process as well** !!!

# CTRL_C_EVENT
Use 0 (current process group) in os.kill
```python
import subprocess as sp
import sys
import time
import signal
import os

po_object = sp.Popen(['dist/server.exe'])  # <--- don't create process group
print('server started')
pid = po_object.pid
print(f'server.exe (pyinstaller) pid: {pid}')
time.sleep(3)
os.kill(0, signal.CTRL_C_EVENT)  # <---- kill with pid 0
try:
    po_object.wait(timeout=5)
except KeyboardInterrupt:
    print('hit ctrl-c', file=sys.stderr, flush=True)
print(f'Popen return code: {po_object.poll()}, pid={po_object.pid}' )
print('Stopped')
```
Output:
```commandline
server started
server.exe (pyinstaller) pid: 13692
logging...  server pid= 14964
logging...  server pid= 14964
logging...  server pid= 14964
Terminated by SIGINT
hit ctrl-c
Popen return code: 101, pid=13692
Stopped
```
