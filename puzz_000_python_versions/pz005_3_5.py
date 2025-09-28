"""
Python 3.5.0, last updated Nov 22, 2015.

New syntax features:

PEP 492, coroutines with async and await syntax.
PEP 465, a new matrix multiplication operator: a @ b.
PEP 448, additional unpacking generalizations.

New library modules:

typing: PEP 484 – Type Hints.
zipapp: PEP 441 Improving Python ZIP Application Support.
"""

"""PEP 484 - Type Hints"""


def greeting(name: str) -> str:
    return 'Hello ' + name


print(greeting('John'))
# print(greeting(1)) #TypeError: can only concatenate str (not "int") to str
