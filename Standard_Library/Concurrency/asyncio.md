# asyncio

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
asynchronous iterator, asynchronous generator
queue

## 
[A Curious Course on Coroutines and Concurrency](https://www.dabeaz.com/coroutines/)