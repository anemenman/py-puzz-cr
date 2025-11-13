"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""


def find_outlier(integers):
    even_count = 0
    odd_count = 0

    for i in range(3):
        if integers[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    is_even = even_count > odd_count

    for num in integers:
        if (num % 2 == 0) != is_even:
            return num


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # 11 (the only odd number)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))  # 160 (the only even number)
