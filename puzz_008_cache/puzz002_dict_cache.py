"""
Implement caching using a dictionary:

This example uses manual cache passing, where the results are stored in a dictionary cache. Each
function call after the result is in the cache, and if it is, it is returned, otherwise it is saved and stored
in the cache.
"""

cache = {}


def expensive_function(arg):
    if arg in cache:
        return cache[arg]
    else:
        print(f"Calculate for {arg}")
        result = arg * 2
        cache[arg] = result
        return result


result1 = expensive_function(5)
print(f"Result 1: {result1}")

result2 = expensive_function(5)
print(f"Result 2: {result2}")

result3 = expensive_function(10)
print(f"Result 3: {result3}")
