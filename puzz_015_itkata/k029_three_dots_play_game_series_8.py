"""
Play game Series #8: Three Dots
Welcome
In this kata, we'll be playing with three dots.

Task
You are given a game map, like this:

+------------+
|RGY         | +,-,| --> The boundaries of the map
|            | *     --> An obstacle
|     **     | R,G,Y --> Three dots with different colors (red, green, yellow)
|     **     | r,g,y --> The target position of the three dots
|            |           You should move R to r, G to g and Y to y
|         rgy|
+------------+

Your task is to calculate a path to move three dots from their initial positions to their target positions. The result
should be returned as a string. Use ↑↓←→ to represent the four directions (up, down, left and right).

Moving Rules
When the move command(↑↓←→) is executed, the three dots move in the same direction at the same time unless a boundary
or barrier is in front of them.
Only the dot blocked by the obstacle will stop moving, and any dots that do not encounter obstacles will continue
to move.
For the example above, you can return a path like this:

"→→→→→→→→→↓↓↓↓↓"
"""
import heapq


def three_dots(map_str):
    # 1. Быстрый парсинг в одномерный массив
    lines = [l.strip() for l in map_str.strip().split('\n') if '|' in l]
    grid = "".join(l[1:l.rfind('|')] for l in lines)
    rows, cols = len(lines), len(grid) // len(lines)
    size = len(grid)

    walls = {i for i, c in enumerate(grid) if c == '*'}
    starts = tuple(grid.find(c) for c in "RGY")
    targets = tuple(grid.find(c) for c in "rgy")

    # 2. Предварительный расчет идеальных расстояний (BFS от целей)
    # Это позволит эвристике быть абсолютно точной
    dist_maps = []
    for target_idx in targets:
        d_map = [1000] * size
        d_map[target_idx] = 0
        q = [target_idx]
        head = 0
        while head < len(q):
            curr = q[head];
            head += 1
            r, c = curr // cols, curr % cols
            d = d_map[curr]
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    ni = nr * cols + nc
                    if grid[ni] != '*' and d_map[ni] == 1000:
                        d_map[ni] = d + 1
                        q.append(ni)
        dist_maps.append(d_map)

    # 3. Алгоритм A*
    # Упаковываем состояние в один int для мгновенного сравнения
    def pack(p):
        return (p[0] << 20) | (p[1] << 10) | p[2]

    start_packed = pack(starts)
    target_packed = pack(targets)

    # (f_score, g_score, packed_pos, path)
    # f_score = g_score + h (сумма расстояний всех точек)
    h_start = sum(dist_maps[i][starts[i]] for i in range(3))
    queue = [(h_start, 0, start_packed, "")]
    visited = {start_packed: 0}

    moves = [(-cols, '↑'), (cols, '↓'), (-1, '←'), (1, '→')]

    while queue:
        f, g, curr_packed, path = heapq.heappop(queue)

        if curr_packed == target_packed:
            return path

        if g > visited.get(curr_packed, 1000):
            continue

        # Распаковка
        p1, p2, p3 = curr_packed >> 20, (curr_packed >> 10) & 1023, curr_packed & 1023
        curr_pos = (p1, p2, p3)

        for offset, char in moves:
            nxt = []
            for i in range(3):
                p = curr_pos[i]
                # Проверка границ для колонок
                if offset == -1 and p % cols == 0:
                    nxt.append(p)
                elif offset == 1 and p % cols == cols - 1:
                    nxt.append(p)
                else:
                    ni = p + offset
                    if 0 <= ni < size and ni not in walls:
                        nxt.append(ni)
                    else:
                        nxt.append(p)

            nxt_t = tuple(nxt)
            nxt_packed = pack(nxt_t)
            new_g = g + 1

            if new_g < visited.get(nxt_packed, 1000):
                visited[nxt_packed] = new_g
                h = dist_maps[0][nxt_t[0]] + dist_maps[1][nxt_t[1]] + dist_maps[2][nxt_t[2]]
                heapq.heappush(queue, (new_g + h, new_g, nxt_packed, path + char))

    return ""


print(three_dots("""
+------------+
|RGY         |
|            |
|     **     |
|     **     |
|            |
|         rgy|
+------------+"""))
assert three_dots("""
+------------+
|RGY         |
|            |
|     **     |
|     **     |
|            |
|         rgy|
+------------+""") == "↓↓↓↓↓→→→→→→→→→"

assert three_dots("""
+------------+
|RGY         |
|            |
|     **     |
|     **     |
|            |
|         rgy|
+------------+""") == "↓↓↓↓↓→→→→→→→→→"
