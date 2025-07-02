import time

from cachetools import TTLCache, cached

"""
Third-party libraries such as cachetools provide more advanced caching capabilities, including various eviction 
strategies (e.g. LRU - Least Recently Used) and support for time-to-live caching.

To install the library: pip install cachetools.

In this example, TTLCache is used to cache data with a time-to-live (TTL) limit.

A TTL cache is a data storage mechanism in which data in a cache has a certain period of validity, 
known as Time To Live (TTL). After this time, the data is considered stale and must be
refreshed.
"""
cache = TTLCache(maxsize=100, ttl=300)  # Cache for 100 elements with a lifetime of 300 seconds (5 minutes)


@cached(cache)
def get_data_from_source(key):
    print(f"Get data by key {key} from source")
    # Simulating of long data acquisition
    time.sleep(2)
    return f"Data by key {key}"


print(get_data_from_source("item1"))
print(get_data_from_source("item1"))

time.sleep(5)
print(get_data_from_source("item1"))
