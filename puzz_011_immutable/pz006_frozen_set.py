"""
A frozenset in Python is an immutable counterpart to a regular set. This means that once a frozenset is created, its
contents cannot be changed. Examples of use include as keys in dictionaries or as elements of other sets where
immutability is required.
"""
my_frozenset = frozenset([1, 2, 3, 2, 4])
print(my_frozenset)

# as key in dict
my_dict = {my_frozenset: "value"}
print(my_dict)

# as set element
my_set = {1, 2, frozenset({3, 4})}
print(my_set)

# try to change frozenset
try:
    my_frozenset.add(5)
except AttributeError as e:
    print(f"AttributeError: {e}")  # 'frozenset' object has no attribute 'add'

# demo immutable:
my_frozenset = frozenset({1, 2, 3})
try:
    my_frozenset.remove(2)
except AttributeError as e:
    print(f"AttributeError: {e}")  # 'frozenset' object has no attribute 'remove'

print("------------------")
# Operations:
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])

# union
union_set = set1 | set2
print(union_set)  # frozenset({1, 2, 3, 4, 5})

# intersection
intersection_set = set1 & set2
print(intersection_set)  # frozenset({3})

# difference
difference_set = set1 - set2
print(difference_set)  # frozenset({1, 2})
