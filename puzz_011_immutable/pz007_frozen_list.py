"""
A frozenlist in Python is a mutable sequence (like a list), but with the additional property of being immutable once it
is created, like a frozenset. This means that the elements in a frozenlist can be modified, but once the frozenlist is
created, its contents can no longer be changed. It implements collections.abc.MutableSequence, which means it has
methods for working with lists, but with the restriction of being immutable once initialized.
"""
from frozenlist import FrozenList

my_frozen_list = FrozenList([1, 2, 3])

print(my_frozen_list[0])  # 1

# Changing an element (works until frozenlist is "frozen")
my_frozen_list[0] = 10
print(my_frozen_list)  # [10, 2, 3]

# "Freeze" frozenlist (after this change is impossible)
my_frozen_list.freeze()

# Attempting to modify frozenlist will throw an exception
try:
    my_frozen_list[0] = 20
except Exception as e:
    print(f'Exception while change: {e}')  # Cannot modify frozen list.

#  After "freezing" elements can still be read
print(my_frozen_list[0])  # 10

#  Some operations, such as deleting or inserting, will also be unavailable.
try:
    del my_frozen_list[0]
except Exception as e:
    print(f'Exception while delete: {e}')  # Cannot modify frozen list.

#  Create new frozenlist% This is possible because a copy is being created, not a change.
new_frozen_list = FrozenList(my_frozen_list)
print(new_frozen_list)  # [10, 2, 3]
