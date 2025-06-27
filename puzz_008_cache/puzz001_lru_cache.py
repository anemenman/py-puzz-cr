from functools import lru_cache

"""
LRU - Least Recently Used

There are several ways to implement caching in Python to improve performance.
The most common methods include using the lru_cache decorator from the functools module,
implementing a cache in a video dictionary, or using library components such as cachetools.

In this regard, expensive_function is cached, which avoids re-executing the circuit.
for the same arguments. maxsize=128 specifies the maximum number of items to be
stored in the cache. If this value is exceeded, old entries will be discarded.
"""


@lru_cache(maxsize=128)
def expensive_function(arg1, arg2):
    """
    expensive calculations
    """
    print(f"Calculate-----------> {arg1}, {arg2}")
    return arg1 * arg2


result1 = expensive_function(2, 3)
print(f"Result 1: {result1}")

result2 = expensive_function(2, 3)
print(f"Result 2: {result2}")

result3 = expensive_function(4, 5)
print(f"Result 3: {result3}")

result4 = expensive_function(4, 5)
print(f"Result 4: {result4}")
