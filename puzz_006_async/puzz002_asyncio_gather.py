import asyncio

"""
asyncio.gather in Python is a function that allows you to run multiple coroutines (or tasks) in parallel and wait for 
them to complete. It takes coroutines or Task objects as arguments and returns a Future that will complete when all the 
coroutines passed in have completed. The results of the coroutines are returned as a list, in the same order in which 
the coroutines were passed to gather.
"""


async def task_1():
    await asyncio.sleep(1)
    return "Result from task 1"


async def task_2():
    await asyncio.sleep(2)
    return "Result from task 2"


async def main():
    results = await asyncio.gather(task_1(), task_2())
    print(results)  # ['Result from task 1', 'Result from task 2']

    # Without await:
    # results = asyncio.gather(task_1(), task_2())  # asyncio.exceptions.CancelledError
    # print(results)  # <_GatheringFuture pending>


if __name__ == "__main__":
    asyncio.run(main())
