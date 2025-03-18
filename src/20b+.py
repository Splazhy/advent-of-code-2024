INPUT_PATH = 'input/20.in'
TEST_MOD = [
    ('test/20.in', 285), # manually adding from example
]

def out_of_bounds(pos, area) -> bool:
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(area[0]) or pos[1] >= len(area)

def manhattan_dist(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    grid = []
    start = None
    for y, l in enumerate(lines):
        grid.append([*l])
        for x, c in enumerate(l):
            if c == 'S':
                start = (x, y)

    q = [(start[0], start[1], 0)]
    cost_map = {}
    path = []
    visited = set()
    while len(q) > 0:
        x, y, cost = q.pop(0)
        visited.add((x, y))
        cost_map[(x, y)] = cost
        path.append((x, y))
        for new_x, new_y in [ (x, y-1), (x, y+1), (x-1, y), (x+1, y) ]:
            if (
                out_of_bounds((new_x, new_y), grid) or
                grid[new_y][new_x] == '#' or
                (new_x, new_y) in visited
            ):
                continue
            q.append((new_x, new_y, cost+1))
            break

    max_cheat_time = 20
    time_to_save = 50 # testing example
    if file_path == INPUT_PATH:
        time_to_save = 100

    ans = 0
    path = path[time_to_save:] # skip positions that don't save more than time_to_save
    path = path[::-1] # reverse path to start from the end
    for x, y in path:
        cur_cost = cost_map[(x, y)]
        for dy in range(-max_cheat_time, max_cheat_time + 1):
            for dx in range(-max_cheat_time + abs(dy), max_cheat_time - abs(dy) + 1):
                new_x, new_y = x + dx, y + dy
                if (
                    (new_x, new_y) in cost_map and
                    cur_cost - cost_map[(new_x, new_y)] - manhattan_dist((x, y), (new_x, new_y)) >= time_to_save
                ):
                    ans += 1

    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
