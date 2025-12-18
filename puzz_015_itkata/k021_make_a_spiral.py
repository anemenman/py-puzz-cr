"""
Your task, is to create a NxN spiral with a given size.

Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given
size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""


def spiralize(size):
    if size <= 0:
        return []

    grid = [[0] * size for _ in range(size)]

    top = 0
    bottom = size - 1
    left = 0
    right = size - 1

    while top < bottom and left < right:

        if bottom - top < 1:
            break

        for i in range(left, right + 1):
            grid[top][i] = 1
            right = i
            if i + 2 < size and grid[top][i + 2] == 1:
                break

        top += 1

        if bottom - top < 1:
            break

        for i in range(top, bottom + 1):
            grid[i][right] = 1
            bottom = i
            if i + 2 < size and grid[i + 2][right] == 1:
                break

        right -= 1

        if bottom - top < 1:
            break

        for i in range(right, left - 1, -1):
            grid[bottom][i] = 1
            left = i
            if i - 2 >= 0 and grid[bottom][i - 2] == 1:
                break

        bottom -= 1

        if bottom - top < 1:
            break

        for i in range(bottom, top - 1, -1):
            grid[i][left] = 1
            top = i
            if i - 2 >= 0 and grid[i - 2][left] == 1:
                break

        left += 1

    return grid


assert spiralize(5) == [[1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 1],
                        [1, 1, 1, 0, 1],
                        [1, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1]]

assert spiralize(8) == [[1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 0, 1, 0, 0, 1, 0, 1],
                        [1, 0, 1, 1, 1, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1]]

assert spiralize(10) == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                         [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                         [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                         [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                         [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
