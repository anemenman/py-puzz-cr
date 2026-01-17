"""
Python 3.13.0, released on 7 October 2024

Summary – Release Highlights
Python 3.13 is the latest stable release of the Python programming language, with a mix of changes to the language,
the implementation and the standard library. The biggest changes include a new interactive interpreter, experimental
support for running in a free-threaded mode (PEP 703), and a Just-In-Time compiler (PEP 744).

Error messages continue to improve, with tracebacks now highlighted in color by default. The locals() builtin now has
defined semantics for changing the returned mapping, and type parameters now support default values.

The library changes contain removal of deprecated APIs and modules, as well as the usual improvements in
user-friendliness and correctness. Several legacy standard library modules have now been removed following their
deprecation in Python 3.11 (PEP 594).
"""

"""
Interpreter improvements:

A greatly improved interactive interpreter and improved error messages.
PEP 667: The locals() builtin now has defined semantics when mutating the returned mapping. Python debuggers and 
similar tools may now more reliably update local variables in optimized scopes even during concurrent code execution.

PEP 703: CPython 3.13 has experimental support for running with the global interpreter lock disabled. See Free-threaded 
CPython for more details.

PEP 744: A basic JIT compiler was added. It is currently disabled by default (though we may turn it on later). 
Performance improvements are modest – we expect to improve this over the next few releases.

Color support in the new interactive interpreter, as well as in tracebacks and doctest output. This can be disabled 
through the PYTHON_COLORS and NO_COLOR environment variables.
"""

"""
Free-threaded CPython
CPython now has experimental support for running in a free-threaded mode, with the global interpreter lock (GIL) 
disabled. 
"""

"""
An experimental just-in-time (JIT) compiler
When CPython is configured and built using the --enable-experimental-jit option, a just-in-time (JIT) compiler is added 
which may speed up some Python programs. 
"""
