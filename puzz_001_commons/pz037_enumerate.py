"""
The enumerate function in Python provides a convenient way to iterate over the elements of a list (or other iterable
sequence) along with their indices. It returns an iterator that generates tuples containing the index of the element
and the element itself.

The enumerate function makes code more readable and convenient when you need to work with element indices when
iterating over iterable objects.
"""
my_list = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(my_list):
    print(f"Index: {index}, Value: {fruit}")

print('--------------------------------')
"""
Starting Index: You can specify a starting value for the counter by passing it as the second argument to the enumerate 
function. For example, enumerate(my_list, 1) will start counting from 1.
"""
for index, fruit in enumerate(my_list, 1):
    print(f"Index: {index}, Value: {fruit}")

print('--------------------------------')
"""
Using with other iterables: The enumerate function works with any iterable such as strings, tuples, dictionaries, etc.
"""
my_string = "hello"
for index, char in enumerate(my_string):
    print(f"Index: {index}, Char: {char}")
