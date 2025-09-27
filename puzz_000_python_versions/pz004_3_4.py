"""
Python 3.4.0, last updated Mar 16, 2014.

PEP 453: Explicit Bootstrapping of PIP in Python Installations¶
Bootstrapping pip By Default

PEP 446: Newly Created File Descriptors Are Non-Inheritable¶

"""
import gc
import weakref
from enum import Enum

"""
Improvements to Codec Handling
"""
# LookupError: 'hex' is not a text encoding; use codecs.decode() to handle arbitrary codecs
# print(b"abcdef".decode("hex"))

"""min() and max() now accept a default keyword-only argument that can be used to specify the value they return if the 
iterable they are evaluating has no elements."""

i1 = [1, 2, 3]
print(i1)
print(min(i1))
print(max(i1))

"""Module objects are now weakref‘able.

A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent 
are weak references, garbage collection is free to destroy the referent and reuse its memory for something else. 
However, until the object is actually destroyed the weak reference may return the object even if there are no strong 
references to it.
"""


class C:
    def method(self):
        print("method called!")


c = C()
r = weakref.ref(c.method)
print(r())
r = weakref.WeakMethod(c.method)
print(r())
print(r()())
del c
print(gc.collect())

print(r())

"""New Modules"""

"""asyncio PEP 3156"""

"""enum PEP 435"""


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


selected_color = Color.RED
print(selected_color)  # Color.RED
print(selected_color.name)  # RED
print(selected_color.value)  # 1

if selected_color == Color.RED:
    print("Is red!!!")

print('------------------')
for color in Color:
    print(color)
