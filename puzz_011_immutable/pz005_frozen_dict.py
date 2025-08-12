"""
frozendict in Python is an immutable version of a dictionary. It provides the interface of a dictionary, but its
elements cannot be changed once the object is created. This is useful when you need a dictionary that should not be
changed, such as as a key in another dictionary or as an element of a frozenset
"""
from frozendict import frozendict

my_frozendict = frozendict({'a': 1, 'b': 2})

try:
    my_frozendict['a'] = 3  # TypeError: 'frozendict.frozendict' object does not support item assignment
except TypeError as e:
    print(f"TypeError: {e}")

# frozendict can be used as a key in another dictionary
my_dict = {my_frozendict: 'value'}

print(my_dict[my_frozendict])

# frozendict can be used as an element of frozenset
my_frozenset = frozenset([my_frozendict, frozendict({'c': 3})])

print(my_frozenset)
