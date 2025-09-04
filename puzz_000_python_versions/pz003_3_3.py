"""
Python 3.3.0, documentation released on 29 September 2012.

New syntax features:

New yield from expression for generator delegation.
The u'unicode' syntax is accepted again for str objects.
New library modules:

faulthandler (helps debugging low-level crashes)
ipaddress (high-level objects representing IP addresses and masks)
lzma (compress data using the XZ / LZMA algorithm)
venv (Python virtual environments, as in the popular virtualenv package)
New built-in features:

Reworked I/O exception hierarchy.
Implementation improvements:

Rewritten import machinery based on importlib.
More compact unicode strings.
More compact attribute dictionaries.
Security improvements:

Hash randomization is switched on by default.
"""
import gc
from math import pi

print("Python 3.3.0")

"""PEP 405 - Python Virtual Environments

This PEP adds the venv module for programmatic access, and the pyvenv script for command-line access and administration.
"""

"""PEP 420: Namespace Packages

Native support for package directories that don’t require __init__.py marker files and can automatically span multiple path segments"""

"""PEP 3118: New memoryview implementation and buffer protocol documentation¶
The maximum number of dimensions is officially limited to 64.
"""

print(pi)

"""It is now possible to register callbacks invoked by the garbage collector before and after collection using the new callbacks list."""
print(gc.get_stats())

"""Optimizations
Thanks to PEP 393, some operations on Unicode strings have been optimized
UTF-8 is now 2x to 4x faster. UTF-16 encoding is now up to 10x faster.
"""
