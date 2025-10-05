"""
Python 3.6.0, last updated Dec 22, 2016.

New syntax features:

PEP 498, formatted string literals.
PEP 515, underscores in numeric literals.
PEP 526, syntax for variable annotations.
PEP 525, asynchronous generators.
PEP 530: asynchronous comprehensions.

New library modules:

secrets: PEP 506 – Adding A Secrets Module To The Standard Library.
"""
import asyncio
from typing import Dict

"""PEP 498: Formatted string literals"""
name = "Fred"
print(f"He said his name is {name}.")

"""PEP 526: Syntax for variable annotations"""


class Starship:
    stats: Dict[str, int] = {}


"""PEP 515: Underscores in Numeric Literals"""
v1 = 1_000_000_000_000_000
print(v1)

"""PEP 525: Asynchronous Generators"""


async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


"""PEP 530: Asynchronous Comprehensions"""
# result = [i async for i in aiter() if i % 2]
# print(result)
# result = [await fun() for fun in funcs if await condition()]
