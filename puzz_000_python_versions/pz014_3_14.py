"""
Python 3.14.0, released on 7 October 2025

Summary – Release highlights¶
Python 3.14 is the latest stable release of the Python programming language, with a mix of changes to the language,
the implementation, and the standard library. The biggest changes include template string literals, deferred evaluation
of annotations, and support for subinterpreters in the standard library.

The library changes include significantly improved capabilities for introspection in asyncio, support for Zstandard via
a new compression.zstd module, syntax highlighting in the REPL, as well as the usual deprecations and removals, and
improvements in user-friendliness and correctness.
"""

"""
PEP 649 & PEP 749: Deferred evaluation of annotations
The annotations on functions, classes, and modules are no longer evaluated eagerly. Instead, annotations are stored in 
special-purpose annotate functions and evaluated only when necessary (except if from __future__ import annotations is 
used).

The new annotationlib module provides tools for inspecting deferred annotations. Annotations may be evaluated in the 
VALUE format (which evaluates annotations to runtime values, similar to the behavior in earlier Python versions), the 
FORWARDREF format (which replaces undefined names with special markers), and the STRING format (which returns 
annotations as strings
"""
# from annotationlib import get_annotations, Format
#
#
# def func(arg: Undefined):
#     pass
#
#
# get_annotations(func, format=Format.VALUE)  # NameError: name 'Undefined' is not defined
# get_annotations(func, format=Format.FORWARDREF)
# get_annotations(func, format=Format.STRING)
