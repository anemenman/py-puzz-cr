import sys

from decimal import Decimal

"""
Return the size of an object in bytes. The object can be any type of object. All built-in objects will return correct 
results, but this does not have to hold true for third-party extensions as it is implementation specific.

Only the memory consumption directly attributed to the object is accounted for, not the memory consumption of objects 
it refers to.

https://docs.python.org/3/library/sys.html#sys.getsizeof
"""

print(sys.getsizeof(42))  # 28
print(sys.getsizeof(Decimal(5.3)))  # 104
print(sys.getsizeof([1, 2, 3, 4, 5]))  # 120
print(sys.getsizeof('Hello, World!'))  # 62
