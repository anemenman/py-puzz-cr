from dataclasses import dataclass

"""
Using dataclasses with frozen=True (Python 3.7+): This is the recommended and most straightforward way to 
create immutable classes.
"""


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(10, 20)
print(p)
# p.x = 30  # This will raise a FrozenInstanceError
