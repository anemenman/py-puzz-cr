import random

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1)

items_list = list(dict1.items())
print(items_list)

random.shuffle(items_list)
print(items_list)

shuffled_dict = dict(items_list)

print(shuffled_dict)
