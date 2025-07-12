"""
Search for a number k in a two-dimensional array (matrix) of size n × m, where each row and each column are sorted in
ascending order:

We start either from the lower left corner or from the upper right corner (the most popular way).

If the current element A[i][j] < k, we move to the right (increase j);
If A[i][j] > k, we go down (increase i);
If found, we return the coordinates; if we go beyond the matrix, there is no such number.
Complexity: O(n + m)

Start from the upper right corner
"""


def search_matrix(matrix, k):
    if not matrix or not matrix[0]:
        return False

    n = len(matrix)
    m = len(matrix[0])
    i, j = 0, m - 1

    while i < n and j >= 0:
        if matrix[i][j] == k:
            return (i, j)  # or True if only a presence check is needed
        elif matrix[i][j] > k:
            j -= 1  # to left
        else:
            i += 1  # to down

    return False


matrix = [
    [1, 3, 5],
    [2, 4, 7],
    [5, 8, 10]
]
k = 7
print(search_matrix(matrix, k))  # find (i, j)
