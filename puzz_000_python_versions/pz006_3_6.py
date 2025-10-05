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
from os import urandom
from random import randrange, shuffle, sample
from secrets import choice
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

"""
New Modules
secrets
The main purpose of the new secrets module is to provide an obvious way to reliably generate cryptographically strong 
pseudo-random values suitable for managing secrets, such as account authentication, tokens, and similar.
"""
print(urandom(10))
print(randrange(10))  # Integer from 0 to 9 inclusive
print(choice(['win', 'lose', 'draw']))  # Single random element from a sequence

deck = 'ace two three four'.split()
shuffle(deck)  # Shuffle a list
print(deck)

shuffled1 = sample([10, 20, 30, 40, 50], k=4)
print(shuffled1)  # Four samples without replacement
