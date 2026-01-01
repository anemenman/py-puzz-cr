"""
Total area covered by rectangles

Your task in order to complete this Kata is to write a function which calculates the area covered by a union of
rectangles.
Rectangles can have non-empty intersection, in this way simple solution: Sall = S1 + S2 + ... + Sn-1 + Sn (where n -
the quantity of rectangles) will not work.

Preconditions
each rectangle is represented as: [x0, y0, x1, y1]
(x0, y0) - coordinates of the bottom left corner
(x1, y1) - coordinates of the top right corner
xi, yi - positive integers or zeroes (0, 1, 2, 3, 4..)
sides of rectangles are parallel to coordinate axes
your input data is array of rectangles
Requirements
Number of rectangles in one test (not including simple tests) range from 3000 to 15000. There are 10 tests with such
range. So, your algorithm should be optimal.
Sizes of the rectangles can reach values like 1e6.

There are three rectangles:

R1: [3,3,8,5], with area 10
R2: [6,3,8,9], with area 12
R3: [11,6,14,12], with area 18
R1 and R2 are overlapping (2x2), the grayed area is removed from the total area
Hence the total area is 10 + 12 + 18 - 4 = 36

Note: expected time complexity: something around O(N²), but with a good enough constant factor. If you think about
using something better, try this kata instead: Total area covered by more rectangles


"""
import time


def calculate(rectangles):
    start = time.time()
    unique_sorted_x_list = sorted(set(x for (x0, y0, x1, y1) in rectangles for x in (x0, x1)))
    unique_sorted_x_dict = {x: i for i, x in enumerate(unique_sorted_x_list)}

    y_lists = [[] for _ in range(len(unique_sorted_x_list) - 1)]

    for x0, y0, x1, y1 in rectangles:
        for j in range(unique_sorted_x_dict[x0], unique_sorted_x_dict[x1]):
            y_lists[j].append((y0, y1))

    result = 0
    for i, y_list in enumerate(y_lists):
        if not y_list:
            continue
        y_list.sort()
        h, y = 0, y_list[0][0]
        for y0, y1 in y_list:
            h += max(y, y1) - max(y, y0)
            y = max(y, y1)
        result += h * (unique_sorted_x_list[i + 1] - unique_sorted_x_list[i])

    print(time.time() - start)
    return result


assert calculate([]) == 0
assert calculate([(0, 0, 1, 1)]) == 1
assert calculate([(0, 4, 11, 6)]) == 22
assert calculate([(0, 0, 1, 1), (1, 1, 2, 2)]) == 2
assert calculate([(0, 0, 1, 1), (0, 0, 2, 2)]) == 4
assert calculate([(3, 3, 8, 5), (6, 3, 8, 9), (11, 6, 14, 12)]) == 36

assert calculate([(1, 7, 3, 10), (1, 8, 3, 9)]) == 6
assert calculate([(6, 7, 9, 10), (7, 8, 8, 9)]) == 9
assert calculate([(1, 7, 4, 10), (2, 7, 4, 9), (3, 7, 4, 9)]) == 9
assert calculate([(1, 1, 4, 3), (2, 2, 3, 4)]) == 7
assert calculate([(5, 0, 7, 3), (6, 1, 8, 2)]) == 7
assert calculate([(9, 0, 11, 2), (10, 1, 12, 3)]) == 7
assert calculate([(13, 1, 16, 3), (14, 0, 15, 2)]) == 7
assert calculate([(17, 1, 19, 3), (18, 0, 20, 2)]) == 7
assert calculate([(13, 5, 15, 6), (14, 4, 16, 7)]) == 7
assert calculate([(1, 3, 4, 6), (2, 1, 5, 4), (3, 2, 6, 5)]) == 20
assert calculate(
    [(1, 1, 2, 2), (2, 1, 3, 2), (3, 1, 4, 2), (1, 2, 2, 3), (2, 2, 3, 3), (3, 2, 4, 3), (1, 3, 2, 4), (2, 3, 3, 4),
     (3, 3, 4, 4)]) == 9
assert calculate([(1, 1, 6, 6), (1, 3, 4, 6), (2, 3, 4, 6), (2, 4, 5, 6), (3, 5, 4, 6)]) == 25
assert calculate([(1, 1, 6, 6), (2, 1, 6, 6), (3, 1, 6, 6), (4, 1, 6, 6), (5, 2, 6, 5)]) == 25
assert calculate([(1, 1, 7, 6), (2, 2, 8, 7), (3, 3, 9, 8), (4, 4, 10, 9), (5, 5, 11, 10)]) == 70
assert calculate(
    [(1, 4, 5, 6), (2, 5, 6, 7), (3, 6, 7, 8), (4, 7, 8, 9), (2, 3, 6, 5), (3, 2, 7, 4), (4, 1, 8, 3)]) == 38
assert calculate([(9, 5, 12, 6), (10, 4, 11, 7)]) == 5
assert calculate([(7, 1, 11, 7), (8, 0, 12, 3), (8, 4, 13, 5), (9, 5, 14, 8), (10, 2, 15, 6)]) == 53
assert calculate([(1, 2, 6, 6), (1, 3, 5, 5), (1, 1, 7, 7)]) == 36
assert calculate([(1, 2, 3, 7), (2, 1, 7, 3), (6, 2, 8, 7), (2, 6, 7, 8), (4, 4, 5, 5)]) == 37
assert calculate([(1, 1, 2, 2), (1, 1, 2, 2), (1, 1, 2, 2), (1, 1, 2, 2), (1, 1, 2, 2), (1, 1, 2, 2)]) == 1
assert calculate(
    [(3, 3, 6, 5), (4, 4, 6, 6), (4, 3, 7, 5), (4, 2, 8, 5), (4, 3, 8, 6), (9, 0, 11, 4), (9, 1, 10, 6), (9, 0, 12, 2),
     (10, 1, 13, 5), (12, 4, 15, 6), (14, 1, 16, 5), (12, 1, 17, 2)]) == 52
assert calculate(
    [(2, 2, 17, 2), (2, 2, 17, 4), (2, 2, 17, 6), (2, 2, 17, 8), (2, 2, 17, 10), (2, 2, 17, 12), (2, 2, 17, 14),
     (2, 2, 17, 16), (2, 2, 17, 18), (2, 2, 17, 20), (2, 2, 17, 22), (2, 2, 17, 24), (2, 2, 17, 26),
     (2, 2, 17, 28)]) == 390
assert calculate([(0, 0, 3, 1), (0, 0, 10, 1)]) == 10
assert calculate([(3, 0, 10, 1), (0, 0, 10, 1)]) == 10
assert calculate([(0, 0, 3, 1), (0, 0, 3, 10)]) == 30
assert calculate([(0, 0, 3, 10), (0, 3, 3, 10)]) == 30
