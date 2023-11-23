# asyncio
<!-- TOC -->
* [asyncio](#asyncio)
  * [awaitable](#awaitable)
  * [asyncio methods](#asyncio-methods)
    * [high level](#high-level)
    * [low level](#low-level)
  * [example](#example)
  * [asynchronous iterator, asynchronous generator](#asynchronous-iterator-asynchronous-generator)
  * [queue](#queue)
  * [links](#links)
<!-- TOC -->
---

## awaitable

Running task concurrently:  

```python
import asyncio

async def task1():
    result =await awaitable1()

async def task2():
    result =await awaitable2()

async def main():
    results = asyncio.gather(task1(), task2())

if __name__ == '__main__':
    results = asyncio.run(main())
```

Three types of *awaitable* :  
- coroutines
```python
async def foo()
    result = await some_awaitable()
```
- tasks

```python
import asyncio

async def foo()
    task = asyncio.create_task(some_awaitable())
    result = await task
```
- futures
```python
import asyncio
import concurrent.futures

pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

def foo():
    return None

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(pool, foo)
```

As awaitable use objects that con be awaited -> methods from modules or futures
```python
aiohttp
anyio
aioredis
aiofiles
...
```


## asyncio methods
### high level
```python
import asyncio

asyncio.sleep(delay)
asyncio.gather(*aws)
asyncio.to_thread(func, *args, **kwargs)  # run func in separate thread
asyncio.run(coro)  # creates event loop and runs coro in it is equivalent to low level: 

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(coro)
finally:
    loop.close()
```
### low level

```python
import asyncio

asyncio.get_running_loop()  
asyncio.get_event_loop()
```
##  example
```python
import asyncio
import concurrent.futures
import os
import time
from functools import wraps, partial

NN = 10


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop = time.perf_counter()
        print(stop-start)
        return result
    return wrapper


def blocking_io(id):
    print(f'starting blocking-io {id}...', end='')
    time.sleep(3.4)  # simulating no blocking io
    print(f'...finishing blocking-io {id}.')
    result = f'done io {id}'
    return result



def cpu_bound(id):
    print(f'starting cpu-bound {id}...', end='')
    for i in range(10 ** 8):  # cpu bound task
        x = i
    print(f'...finishing cpu-bound {id}.')
    result = f'done cpu {id}'
    return result


async def task_cpu(pool, id):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(pool, partial(cpu_bound, id))
    return result


async  def task_io(pool, id):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(pool, partial(blocking_io, id))
    return result


async def cpu_tasks(pool):
    results = await asyncio.gather(*(task_cpu(pool, i) for i in range(NN)))
    return results


async def io_tasks(pool):
    results = await asyncio.gather(*(task_io(pool, i) for i in range(NN)))
    # results = await asyncio.gather(*(asyncio.to_thread(blocking_io, i) for i in range(NN)))
    return results

@timer
def cpu_bound_con(pool):
    results = asyncio.run(cpu_tasks(pool))
    return results

@timer
def cpu_bound_seq():
    results = [cpu_bound(i) for i in range(NN)]
    return results

@timer
def blocking_io_con(pool):
    results = asyncio.run(io_tasks(pool))
    return results

@timer
def blocking_io_seq():
    results = [blocking_io(i) for i in range(NN)]
    return results


if __name__ == '__main__':
    cpu = os.cpu_count()
    process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=cpu)
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=cpu)

    print('>> sequential cpu:')
    print(cpu_bound_seq())

    print('>> concurrent cpu:')
    print(cpu_bound_con(process_pool))

    print('>> sequential io:')
    print(blocking_io_seq())

    print('>> concurrent io:')
    print(blocking_io_con(thread_pool))

```

## asynchronous iterator, asynchronous generator
...
## queue
...
## links
[A Curious Course on Coroutines and Concurrency](https://www.dabeaz.com/coroutines/)