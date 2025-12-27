"""
Python 3.12.0, released on 2 October 2023

New syntax features:
PEP 695, type parameter syntax and the type statement

New grammar features:
PEP 701, f-strings in the grammar

Interpreter improvements:
PEP 684, a unique per-interpreter GIL
PEP 669, low impact monitoring
Improved ‘Did you mean …’ suggestions for NameError, ImportError, and SyntaxError exceptions

Python data model improvements:
PEP 688, using the buffer protocol from Python

Significant improvements in the standard library:
The pathlib.Path class now supports subclassing
The os module received several improvements for Windows support
A command-line interface has been added to the sqlite3 module
isinstance() checks against runtime-checkable protocols enjoy a speed up of between two and 20 times
The asyncio package has had a number of performance improvements, with some benchmarks showing a 75% speed up.
A command-line interface has been added to the uuid module
Due to the changes in PEP 701, producing tokens via the tokenize module is up to up to 64% faster.

Security improvements:
Replace the builtin hashlib implementations of SHA1, SHA3, SHA2-384, SHA2-512, and MD5 with formally verified code from
the HACL* project. These builtin implementations remain as fallbacks that are only used when OpenSSL does not provide
them.

C API improvements:
PEP 697, unstable C API tier
PEP 683, immortal objects

CPython implementation improvements:
PEP 709, comprehension inlining
CPython support for the Linux perf profiler
Implement stack overflow protection on supported platforms

New typing features:
PEP 692, using TypedDict to annotate **kwargs
PEP 698, typing.override() decorator
"""

"""PEP 695: Type Parameter Syntax"""

# def max[T](args: Iterable[T]) -> T:
#     pass
#
#
# def append(self, element: T) -> None:
#     pass
#
#
# # In addition, the PEP introduces a new way to declare type aliases using the type statement, which creates an
# instance
# # of TypeAliasType:
# type Point = tuple[float, float]

"""PEP 701: Syntactic formalization of f-strings
lifts some restrictions on the usage of f-strings. Expression components inside f-strings can now be any valid Python 
expression, including strings reusing the same quote as the containing f-string, multi-line expressions, comments, 
backslashes, and unicode escape sequences."""
# songs = ['Take me back to Eden', 'Alkaline', 'Ascensionism']
# f"This is the playlist: {", ".join(songs)}"
# 'This is the playlist: Take me back to Eden, Alkaline, Ascensionism'

# f"{f"{f"{f"{f"{f"{1+1}"}"}"}"}"}"
# '2'
