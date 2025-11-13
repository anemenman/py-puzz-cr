"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list
with the strings filtered out.
"""


def filter_list(lst):
    # list comprehension for filter
    return [item for item in lst if isinstance(item, int) and item >= 0]


list1 = [1, 2, 'a', 'b']
print(filter_list(list1))

print(filter_list([1, 2, 'a', 'b']) == [1, 2])
print(filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15])
print(filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123])
