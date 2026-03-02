import heapq


def locate(game_map, char):
    for i, row in enumerate(game_map):
        for j, val in enumerate(row):
            if val == char:
                return i, j


def three_dots(game_map):
    game_map = game_map.split('\n')

    init = tuple(locate(game_map, c) for c in 'RGY')
    goal = tuple(locate(game_map, c) for c in 'rgy')

    def heuristic(h_state):
        return max(abs(x[0] - y[0]) + abs(x[1] - y[1]) for x, y in zip(h_state, goal))

    pq = [(heuristic(init), '', init)]
    seen = set()

    while pq:
        _, path, state = heapq.heappop(pq)

        if state == goal:
            return path
        elif state in seen or len(set(list(state))) != 3:
            continue

        seen.add(state)

        for i in range(4):
            direction = "↓↑→←"[i]
            u, v = [(1, 0), (-1, 0), (0, 1), (0, -1)][i]

            copy = []
            for s, t in state:
                if game_map[s + u][t + v] in 'RGYrgy ':
                    copy.append((s + u, t + v))
                else:
                    copy.append((s, t))
            copy = tuple(copy)

            heapq.heappush(pq, (heuristic(copy), path + direction, copy))
