"""
This is a classic backtracking problem with dividing an area into rectangles.
The main challenge here is maintaining priority (maximum width of the first piece) and correctly tracking occupied
cells.

1) Area: We calculate the area of one piece (total_area / n). All pieces must be rectangular and have the same
area.
2) Enumeration: We start from the top-left free cell and try to "fit" all possible rectangles of the given area there.
3) Width Priority: In the possible_shapes list, we iterate through the width w from largest to smallest. Since the
algorithm finds the first valid solution, this automatically guarantees that the option with the largest first piece
width will be selected.
4) Validation: A rectangle is valid only if it contains exactly one raisin and does not overlap any previously cut
pieces.
5) Order: Recursion always searches for the top-leftmost free point, which guarantees the correct order of the pieces
in the resulting array.
"""


def cut(cake_str):
    cake = cake_str.split('\n')
    height = len(cake)
    width = len(cake[0])

    # Find the coordinates of all the raisins
    raisins = [(r, c) for r in range(height) for c in range(width) if cake[r][c] == 'o']
    num_raisins = len(raisins)
    total_area = height * width

    if num_raisins == 0 or total_area % num_raisins != 0:
        return []

    piece_area = total_area // num_raisins
    used = [[False] * width for _ in range(height)]

    def get_piece_str(r, c, h, w):
        return "\n".join(row[c:c + w] for row in cake[r:r + h])

    def backtrack(raisin_idx, current_pieces):
        if raisin_idx == num_raisins:
            return current_pieces

        # Find for the first free cell (the upper left corner of the next piece)
        start_r, start_c = -1, -1
        for r in range(height):
            for c in range(width):
                if not used[r][c]:
                    start_r, start_c = r, c
                    break
            if start_r != -1: break

        if start_r == -1: return None

        # Generating possible rectangle sizes (h * w = piece_area)
        # Sort by width (w) in reverse order to satisfy the problem condition
        possible_shapes = []
        for w in range(width, 0, -1):
            if piece_area % w == 0:
                h = piece_area // w
                if start_r + h <= height and start_c + w <= width:
                    possible_shapes.append((h, w))

        for h, w in possible_shapes:
            # Check if there are already occupied cells inside
            if any(used[r][c] for r in range(start_r, start_r + h) for c in range(start_c, start_c + w)):
                continue

            # Check the number of raisins in this rectangle.
            count = 0
            for r in range(start_r, start_r + h):
                for c in range(start_c, start_c + w):
                    if cake[r][c] == 'o':
                        count += 1

            if count == 1:
                # Mark the cells as occupied
                for r in range(start_r, start_r + h):
                    for c in range(start_c, start_c + w):
                        used[r][c] = True

                res = backtrack(raisin_idx + 1, current_pieces + [get_piece_str(start_r, start_c, h, w)])
                if res is not None:
                    return res

                # backtrack
                for r in range(start_r, start_r + h):
                    for c in range(start_c, start_c + w):
                        used[r][c] = False

        return None

    result = backtrack(0, [])
    return result if result else []


assert cut('''
........
..o.....
...o....
........
'''.strip()) == ['........\n..o.....', '...o....\n........']

assert cut('''
.o......
......o.
....o...
..o.....
'''.strip()) == ['.o......', '......o.', '....o...', '..o.....']

assert cut('''
.o.o....
........
....o...
........
.....o..
........
'''.strip()) == ['.o\n..\n..\n..\n..\n..', '.o....\n......', '..o...\n......', '...o..\n......']

assert cut('''
.o.o....
.o.o....
........
........
'''.strip()) == []

assert cut('''
.o....o.
.o....o.
........
o..oo..o
'''.strip()) == ['.o..', '..o.', '.o..', '..o.', '..\no.', '..\n.o', '..\no.', '..\n.o']

assert cut('''
................
.....o..........
................
...............o
................
................
................
.....o..o.....o.
................
................
...o............
................
................
...............o
................
.o..............
'''.strip()) == ['................\n.....o..........', '................\n...............o',
                 '........\n........\n........\n.....o..', '....\n....\n....\no...\n....\n....\n....\n....',
                 '....\n....\n....\n..o.\n....\n....\n....\n....', '........\n........\n...o....\n........',
                 '................\n...............o', '................\n.o..............']
