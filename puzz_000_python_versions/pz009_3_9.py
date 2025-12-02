"""Python 3.9 was released on October 5th, 2020."""

"""
New syntax features:

PEP 584, union operators added to dict;
PEP 585, type hinting generics in standard collections;
PEP 614, relaxed grammar restrictions on decorators.

New built-in features:

PEP 616, string methods to remove prefixes and suffixes.
"""

"""PEP 584, union operators added to dict;
Merge (|) and update (|=) operators have been added to the built-in dict class. Those complement the existing 
dict.update and {**d1, **d2} methods of merging dictionaries.
"""
x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}

xy = x | y
print(xy)

yx = y | x
print(yx)

x |= y
print(x)
print(y)

"""PEP 585 Type Hinting Generics in Standard Collections"""


def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)


greet_all(['A', 'B'])
greet_all([1, 2])
