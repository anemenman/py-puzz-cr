"""
The Celebrity Problem

A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some
people. A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row
i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the
party, if the celebrity does not exist, return -1.
"""


def find_celebrity(mat):
    n = len(mat)
    if n == 0:
        return -1

    left, right = 0, n - 1

    while left < right:
        if mat[left][right] == 1:
            left += 1
        else:
            right -= 1

    candidate = left

    for i in range(n):
        if i == candidate:
            continue

        if mat[candidate][i] == 1 or mat[i][candidate] == 0:
            return -1

    return candidate


assert find_celebrity([
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]) == 2

assert find_celebrity([
    [0, 1],
    [1, 0]
]) == -1

assert find_celebrity([
    [0, 0, 0],
    [1, 0, 1],
    [1, 1, 0]
]) == 0
