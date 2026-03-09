"""
Break the pieces

You are given a ASCII diagram, comprised of minus signs -, plus signs +, vertical bars | and whitespaces   .
Your task is to write a function which breaks the diagram in the minimal pieces it is made of.
For example, if the input for your function is this diagram:

+------------+
|            |
|            |
|            |
+------+-----+
|      |     |
|      |     |
+------+-----+
the returned value should be the list of:

+------------+
|            |
|            |
|            |
+------------+
(note how it lost a + sign in the extraction)

as well as

+------+
|      |
|      |
+------+
and

+-----+
|     |
|     |
+-----+
The diagram is given as an ordinary multiline string. There are no borders touching each others.
The pieces should not have trailing spaces at the end of the lines. However, it could have leading spaces if the figure
is not a rectangle. For instance:

    +---+
    |   |
+---+   |
|       |
+-------+
However, it is not allowed to use more leading spaces than necessary. It is to say, the first character of some of the
lines should be different than a space.
Finally, note that only the explicitly closed pieces are considered. Spaces "outside" of the shape are part of the background . Therefore the diagram above has a single piece.

Have fun!

Note : in C++ you are provided with two utility functions :

std::string join(const std::string &sep, const std::vector<std::string> &to_join); // Returns the concatenation of all
the strings in the vector, separated with sep

std::vector<std::string> split_lines(const std::string &to_split); // Splits a string, using separator '\n'
"""


def break_pieces(shape):
    shape = shape.split("\n")
    empties, pieces = set(), []
    for i, row in enumerate(shape):
        for j, x in enumerate(row):
            if x == " ":
                empties.add((i, j))
    dr = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]
    while empties:
        start = empties.pop()
        queue, area = [start], {start}
        borders, outside = set(), False
        while queue:
            x, y = queue.pop(0)
            for dx, dy in dr:
                tx, ty = x + dx, y + dy
                if tx < 0 or tx >= len(shape):
                    outside = True
                    continue
                if ty < 0 or ty >= len(shape[tx]):
                    outside = True
                    continue
                if (tx, ty) in area: continue
                if (tx, ty) in empties:
                    queue.append((tx, ty))
                    area.add((tx, ty))
                else:
                    borders.add((tx, ty))
        empties -= area
        if not outside:
            pieces.append(extract_piece(borders, shape))
    return pieces


def extract_piece(borders, shape):
    min_x = min(x for x, y in borders)
    max_x = max(x for x, y in borders)
    min_y = min(y for x, y in borders)
    max_y = max(y for x, y in borders)
    piece = [[" "] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
    for x, y in borders:
        border = shape[x][y]
        if border == "+":
            if not {(x - 1, y), (x + 1, y)} & borders: border = "-"
            if not {(x, y - 1), (x, y + 1)} & borders: border = "|"
        piece[x - min_x][y - min_y] = border
    return "\n".join("".join(row).rstrip() for row in piece)


def print_pieces(piece):
    for i, p in enumerate(piece):
        print(f"Piece {i + 1}:\n{p}\n---")


assert break_pieces("""
+------------+
|            |
|            |
|            |
+------+-----+
|      |     |
|      |     |
+------+-----+""") == ["""+-----+
|     |
|     |
+-----+""", """+------------+
|            |
|            |
|            |
+------------+""", """+------+
|      |
|      |
+------+"""]

assert break_pieces("""
           +-+
           | |
         +-+-+-+
         |     |
      +--+-----+--+
      |           |
   +--+-----------+--+
   |                 |
   +-----------------+
""") == ["""+-----------------+
|                 |
+-----------------+""", """+-----------+
|           |
+-----------+""", """+-----+
|     |
+-----+""", """+-+
| |
+-+"""]

assert break_pieces("""
+-------------------+--+
|                   |  |
|                   |  |
|  +----------------+  |
|  |                   |
|  |                   |
+--+-------------------+""") == ["""                 +--+
                 |  |
                 |  |
+----------------+  |
|                   |
|                   |
+-------------------+""", """+-------------------+
|                   |
|                   |
|  +----------------+
|  |
|  |
+--+"""]

assert break_pieces("""+-------+ +----------+
|       | |          |
| +-+ +-+ +-+    +-+ |
+-+ | |     |  +-+ +-+
    | +-----+--+
+-+ |          +-+ +-+
| +-+  +----+    | | |
| |    |    |    +-+ |
| +----++ +-+        |
|       | |          |
+-------+ +----------+""") == ["""+----------+
|          |
+-+    +-+ |
  |  +-+ +-+
  +--+""", """+-------+
|       |
| +-+ +-+
+-+ | |
    | +--------+
    |          +-+ +-+
  +-+  +----+    | | |
  |    |    |    +-+ |
  +----+  +-+        |
          |          |
          +----------+""", """+-+
| |
| |
| +-----+
|       |
+-------+"""]
