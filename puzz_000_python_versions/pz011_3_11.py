"""
Python 3.11.0, released on 24 October 2022
"""

"""
Summary – Release highlights
Python 3.11 is between 10-60% faster than Python 3.10. On average, we measured a 1.25x speedup on the standard 
benchmark suite. See Faster CPython for details.

New syntax features:
PEP 654: Exception Groups and except*

New built-in features:
PEP 678: Exceptions can be enriched with notes

New standard library modules:
PEP 680: tomllib — Support for parsing TOML in the Standard Library

Interpreter improvements:
PEP 657: Fine-grained error locations in tracebacks

New -P command line option and PYTHONSAFEPATH environment variable to disable automatically prepending potentially unsafe paths to sys.path

New typing features:
PEP 646: Variadic generics
PEP 655: Marking individual TypedDict items as required or not-required
PEP 673: Self type
PEP 675: Arbitrary literal string type
PEP 681: Data class transforms

Important deprecations, removals and restrictions:
PEP 594: Many legacy standard library modules have been deprecated and will be removed in Python 3.13
PEP 624: Py_UNICODE encoder APIs have been removed
PEP 670: Macros converted to static inline functions
"""

"""PEP 654: Exception Groups and except*"""

