import random

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)

print(list1)

list2 = [1, 2, 3, 4, 5]

"""Chooses k unique random elements from a population sequence or set.
Returns a new list containing elements from the population while
leaving the original population unchanged."""
shuffled_list = random.sample(list2, len(list2))
print(shuffled_list)
