"""
When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the
process --myjinxin2015 said

Task
We have a rectangular cake with some raisins on it:

cake =
  ........
  ..o.....
  ...o....
  ........
// o is the raisins
We need to cut the cake evenly into n small rectangular pieces, so that each small cake has 1 raisin. n is not an
argument, it is the number of raisins contained inside the cake:

cake =
  ........
  ..o.....
  ...o....
  ........

result should be an array:
  [
     ........
     ..o.....
  ,
     ...o....
     ........
  ]
// In order to clearly show, we omit the quotes and "\n"
If there is no solution, return an empty array []

Note
The number of raisins is always more than 1 and less than 10.
If there are multiple solutions, select the one with the largest width of the first element of the array.
(See also the examples below.)
Evenly cut into n pieces, meaning the same area. But their shapes can be different. (See also the examples below.)
In the result array, the order of pieces is from top to bottom and from left to right (according to the location of
the upper left corner).
Each piece of cake should be rectangular.
Examples
An example of multiple solutions:
cake =
  .o......
  ......o.
  ....o...
  ..o.....

In this test case, we can found three solution:
solution 1 (horizontal cutting):
  [
    .o......  //piece 1
  ,
    ......o.  //piece 2
  ,
    ....o...  //piece 3
  ,
    ..o.....  //piece 4
  ]

solution 2 (vertical cutting):
  [
    .o  //piece 1
    ..
    ..
    ..
  ,
    ..  //piece 2
    ..
    ..
    o.
  ,
    ..  //piece 3
    ..
    o.
    ..
  ,
    ..  //piece 4
    o.
    ..
    ..
  ]

solution 3 (cross cutting):
  [
    .o..  //piece 1
    ....
  ,
    ....  //piece 2
    ..o.
  ,
    ....  //piece 3
    ..o.
  ,
    o...  //piece 4
    ....
  ]

we need choose solution 1 as result
An example of different shapes:
cake =
  .o.o....
  ........
  ....o...
  ........
  .....o..
  ........

the result should be:
  [
    .o      //pieces 1
    ..
    ..
    ..
    ..
    ..
  ,
    .o....  //pieces 2
    ......
  ,
    ..o...  //pieces 3
    ......
  ,
    ...o..  //pieces 4
    ......
  ]
Although they have different shapes,
they have the same area(2 x 6 = 12 and 6 x 2 = 12).
An example of no solution case:
cake =
  .o.o....
  .o.o....
  ........
  ........
  ........
  ........
the result should be []
"""


def cut(raw_cake):
    cake = raw_cake.split('\n')
    if not cake or not cake[0]:
        return []

    rows = len(cake)
    cols = len(cake[0])
    total_area = rows * cols

    # Find the position of all raisins
    raisins = []
    for r in range(rows):
        for c in range(cols):
            if cake[r][c] == 'o':
                raisins.append((r, c))

    n = len(raisins)
    # Checking the basic conditions
    if n <= 1 or total_area % n != 0:
        return []

    target_area = total_area // n
    if target_area <= 0:
        return []

    def get_rect_cells(r1, c1, r2, c2):
        # Return a list of all cells in the rectangle [r1,r2] x [c1,c2] inclusive
        return [(r, c) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)]

    def count_raisins_in_rect(r1, c1, r2, c2):
        # Count the number of raisins in a rectangle
        return sum(1 for rr, cc in raisins if r1 <= rr <= r2 and c1 <= cc <= c2)

    # Pre-compute all valid rectangles for each raisin
    raisin_rects = {i: [] for i in range(n)}

    for i, (rr, cc) in enumerate(raisins):
        # Try all possible sizes of rectangles with the required area
        for h in range(1, rows + 1):
            if target_area % h != 0:
                continue
            w = target_area // h
            if w < 1 or w > cols:
                continue

            # Loop through all positions for a rectangle of size h×w
            for r1 in range(rows - h + 1):
                r2 = r1 + h - 1
                for c1 in range(cols - w + 1):
                    c2 = c1 + w - 1

                    # The rectangle must contain the current highlight
                    if not (r1 <= rr <= r2 and c1 <= cc <= c2):
                        continue
                    # The rectangle must contain exactly one raisin (this one)
                    if count_raisins_in_rect(r1, c1, r2, c2) != 1:
                        continue

                    # Save rectangle: coordinates and width
                    raisin_rects[i].append((r1, c1, r2, c2, w))

        # If there are no valid rectangles for a particular feature, there is no solution
        if not raisin_rects[i]:
            return []

    solutions = []

    def backtrack(assigned, covered, current):
        # assigned: the set of indices of raisins that are already assigned a rectangle
        # covered: the set of cells covered by the assigned rectangles
        # current: a list of (raisin_index, rectangle) pairs for the current solution

        # All the raisins are assigned
        if len(assigned) == n:
            # Check if the whole cake is covered.
            if len(covered) == total_area:
                solutions.append(list(current))
            return

        # Select the next unassigned raisin
        raisin_idx = next(i for i in range(n) if i not in assigned)

        # Try every valid rectangle for this raisin
        for rect in raisin_rects[raisin_idx]:
            r1, c1, r2, c2, w = rect
            cells = set(get_rect_cells(r1, c1, r2, c2))

            # Skip if rectangle intersects with already covered cells
            if cells & covered:
                continue

            # Assign a rectangle
            assigned.add(raisin_idx)
            covered |= cells
            current.append((raisin_idx, rect))

            # Recursive call
            backtrack(assigned, covered, current)

            # Backtrack
            current.pop()
            for cell in cells:
                covered.discard(cell)
            assigned.remove(raisin_idx)

    # Run a backtracking search
    backtrack(set(), set(), [])

    if not solutions:
        return []

    def solution_to_pieces(sol):
        # Convert the solution to output format:
        # - Sort the chunks by the position of the upper-left corner
        # - Return the list of chunks and the width of the first chunk
        pieces_with_pos = []
        for raisin_idx, (r1, c1, r2, c2, w) in sol:
            # Extract substrings for this piece of cake
            piece = [cake[r][c1:c2 + 1] for r in range(r1, r2 + 1)]
            pieces_with_pos.append((r1, c1, w, piece))

        # Sorting: top to bottom, left to right, top left corner
        pieces_with_pos.sort(key=lambda x: (x[0], x[1]))
        pieces = [p[3] for p in pieces_with_pos]
        first_width = pieces_with_pos[0][2]
        return pieces, first_width

    # Find the best solution: maximum width of the first piece
    best_pieces = None
    best_width = -1

    for sol in solutions:
        pieces, first_w = solution_to_pieces(sol)
        if first_w > best_width:
            best_width = first_w
            best_pieces = pieces

    result = []
    for piece in best_pieces:
        result.append('\n'.join(piece))

    return result if result else []


cake = '''
........
..o.....
...o....
........
'''.strip()
print(cake)
result2 = cut(cake)
print(result2)
