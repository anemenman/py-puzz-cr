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


"""
PEP 734: Multiple interpreters in the standard library
The CPython runtime supports running multiple copies of Python in the same process simultaneously and has done so for 
over 20 years. Each of these separate copies is called an ‘interpreter’. However, the feature had been available only 
through the C-API.

That limitation is removed in Python 3.14, with the new concurrent.interpreters module.

There are at least two notable reasons why using multiple interpreters has significant benefits:

they support a new (to Python), human-friendly concurrency model

true multi-core parallelism

Using multiple interpreters is similar in many ways to multiprocessing, in that they both provide isolated logical 
“processes” that can run in parallel, with no sharing by default. However, when using multiple interpreters, an 
application will use fewer system resources and will operate more efficiently (since it stays within the same process). 
Think of multiple interpreters as having the isolation of processes with the efficiency of threads.

While the feature has been around for decades, multiple interpreters have not been used widely, due to low awareness 
and the lack of a standard library module. Consequently, they currently have several notable limitations, which will 
improve significantly now that the feature is finally going mainstream.

Also added in 3.14: concurrent.futures.InterpreterPoolExecutor.
"""

"""
PEP 750: Template string literals
Template strings are a new mechanism for custom string processing. They share the familiar syntax of f-strings but, 
unlike f-strings, return an object representing the static and interpolated parts of the string, 
instead of a simple str.
"""

# name = 'Wenslydale'
# template = t'Mister {name}'
# assert lower_upper(template) == 'mister WENSLYDALE'

# attributes = {'src': 'limburger.jpg', 'alt': 'lovely cheese'}
# template = t'<img {attributes}>'
# assert html(template) == '<img src="limburger.jpg" alt="lovely cheese" />'

"""
A new type of interpreter
A new type of interpreter has been added to CPython. It uses tail calls between small C functions that implement 
individual Python opcodes, rather than one large C case statement. For certain newer compilers, this interpreter 
provides significantly better performance. Preliminary benchmarks suggest a geometric mean of 3-5% faster on the 
standard pyperformance benchmark suite, depending on platform and architecture. The baseline is Python 3.14 built with 
Clang 19, without this new interpreter.

This interpreter currently only works with Clang 19 and newer on x86-64 and AArch64 architectures. However, a future 
release of GCC is expected will support this as well.

This feature is opt-in for now. Enabling profile-guided optimization is highly recommendeded when using the new 
interpreter as it is the only configuration that has been tested and validated for improved performance. For further 
information, see --with-tail-call-interp.
"""

"""
PEP 784: Zstandard support in the standard library
The new compression package contains modules compression.lzma, compression.bz2, compression.gzip and compression.zlib 
which re-export the lzma, bz2, gzip and zlib modules respectively.
"""

"""
PEP 758: Allow except and except* expressions without brackets
"""
# try:
#     connect_to_server()
# except TimeoutError, ConnectionRefusedError:
#     print('The network has ceased to be!')

"""
PEP 765: Control flow in finally blocks
The compiler now emits a SyntaxWarning when a return, break, or continue statement have the effect of leaving a finally 
block.
"""
