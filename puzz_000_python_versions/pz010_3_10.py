"""
Summary – Release highlights

New syntax features:
PEP 634, Structural Pattern Matching: Specification
PEP 635, Structural Pattern Matching: Motivation and Rationale
PEP 636, Structural Pattern Matching: Tutorial
bpo-12782, Parenthesized context managers are now officially allowed.

New features in the standard library:
PEP 618, Add Optional Length-Checking To zip.

Interpreter improvements:
PEP 626, Precise line numbers for debugging and other tools.

New typing features:
PEP 604, Allow writing union types as X | Y
PEP 613, Explicit Type Aliases
PEP 612, Parameter Specification Variables

Important deprecations, removals or restrictions:
PEP 644, Require OpenSSL 1.1.1 or newer
PEP 632, Deprecate distutils module.
PEP 623, Deprecate and prepare for the removal of the wstr member in PyUnicodeObject.
PEP 624, Remove Py_UNICODE encoder APIs
PEP 597, Add optional EncodingWarning
"""
from typing import Union

"""bpo-12782, Parenthesized context managers are now officially allowed."""
# with (CtxManager() as example):
#     pass

# with (
#     CtxManager1() as example1,
#     CtxManager2() as example2,
#     CtxManager3() as example3,
# ):
#     pass

"""PEP 634: Structural Pattern Matching"""

# Simple pattern: match to a literal
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

# You can combine several literals in a single pattern using | (“or”):
# case 401 | 403 | 404:
#     return "Not allowed"

# Patterns and classes
# class Point:
#     x: int
#     y: int
#
#
# def location(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin is the point's location.")
#         case Point(x=0, y=y):
#             print(f"Y={y} and the point is on the y-axis.")
#         case Point(x=x, y=0):
#             print(f"X={x} and the point is on the x-axis.")
#         case Point():
#             print("The point is located somewhere else on the plane.")
#         case _:
#             print("Not a point")

"""PEP 604: New Type Union Operator"""


def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2

# def square(number: int | float) -> int | float:
#     return number ** 2
