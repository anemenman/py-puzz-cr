import sys
from sys import getsizeof
from typing import Any, Container, Mapping

"""
The function recursively traverses each element of an object (e.g. list items, values in dictionaries, 
object attributes, etc.). When you understand that you need to do this, you will need to repeat the 
remembrance for your personal objects (since you have the ability to send the same question in different 
parts of the structures). As a result of showing a new message that you see all the contributions, 
which will give you an accurate idea of memory retention.
"""


def deep_getsizeof(obj: Any, ids: set[int]) -> int:
    if ids is None:
        ids = set()

    if id(obj) in ids:
        return 0

    size = getsizeof(obj)
    ids.add(id(obj))

    if isinstance(obj, str):
        return size

    if isinstance(obj, Mapping):
        return size + sum(deep_getsizeof(k, ids) + deep_getsizeof(v, ids) for k, v in obj.iteritems())
    if isinstance(obj, Container):
        return size + sum(deep_getsizeof(item, ids) for item in obj)
    return size


example = [[1, 2, 3], 4, 5, '6', '7', 8]
print('getsizeof for list:', sys.getsizeof(example))  # 104
print('deep_getsizeof for list:', deep_getsizeof(example, None))  # 492
