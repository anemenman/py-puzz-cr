"""
3.6. Python 3.7 was released on June 27, 2018.

New syntax features:

PEP 563, postponed evaluation of type annotations.
Backwards incompatible syntax changes:

async and await are now reserved keywords.
New library modules:

contextvars: PEP 567 – Context Variables
dataclasses: PEP 557 – Data Classes
importlib.resources
New built-in features:

PEP 553, the new breakpoint() function.
"""
from dataclasses import dataclass
from typing import get_type_hints


def class_decorator(cls):
    print(cls)


def greet(name: str, age: int = 30) -> str:
    return f"Hello, {name}! You are {age} years old."


hints = get_type_hints(greet)

print(hints)

"""dataclasses"""


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0


p = Point(1.5, 2.5)
print(p)  # produces "Point(x=1.5, y=2.5, z=0.0)"
print(p.x)
