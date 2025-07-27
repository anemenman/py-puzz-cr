"""
Отсортировать массив (время: O(n log n)).
Использовать то же решение с двойным указателем, что выше.(pz002)
"""
from puzz_010_algorithms.pz002_k_is_sum_of_2_in_sorted_array import find_closest_pair


def find_closest_pair_unsorted(arr, k):
    arr = sorted(arr)  # сортируем
    return find_closest_pair(arr, k)  # используем предыдущую функцию


arr = [3, 1, 4, 14, 10, 7, 23, 18]
k = 20
print(find_closest_pair_unsorted(arr, k))  # (1, 18) или (7, 14) -> 21, ближайшая к 20 сумма

k = 27
print(find_closest_pair_unsorted(arr, k))  # (4, 23) -> 27, ровно

k = 50
print(find_closest_pair_unsorted(arr, k))  # (23, 18) -> 41, максимально близкая к 50
