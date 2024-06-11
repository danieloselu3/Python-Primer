import asyncio

# Python 3.4 coroutine example
@asyncio.coroutine
def my_coro():
    yield from func()

# Python 3.5 >> coroutine example
async def my_coro():
    await func()

