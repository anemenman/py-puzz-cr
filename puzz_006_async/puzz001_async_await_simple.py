import asyncio

"""
https://peps.python.org/pep-0492/
"""


async def async_await_simple():
    print('async_await_simple')
    await asyncio.sleep(1)
    return "Ok"


res1 = async_await_simple()  # sys:1: RuntimeWarning: coroutine 'async_await_simple' was never awaited
print('res1---->' + str(res1))  # <coroutine object async_await_simple at 0x10a4eebc0>

res2 = asyncio.run(async_await_simple())
print('res2---->' + str(res2))  # Ok
