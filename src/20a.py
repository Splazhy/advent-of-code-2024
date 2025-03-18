INPUT_PATH = 'input/20.in'
TEST_MOD = [
    ('test/20.in', 0), # bad test
]

def out_of_bounds(pos, area) -> bool:
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(area[0]) or pos[1] >= len(area)

def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    grid = []
    start, end = None, None
    for y, l in enumerate(lines):
        grid.append([*l])
        for x, c in enumerate(l):
            if c == 'S':
                start = (x, y)
            elif c == 'E':
                end = (x, y)

    q = [(start[0], start[1], 0)]
    cost_map = [[0xffffffff for _ in range(len(grid[0]))] for _ in range(len(grid))]
    cost_map[start[1]][start[0]] = 0
    while len(q) > 0:
        x, y, cost = q.pop(0)
        for new_x, new_y in [ (x, y-1), (x, y+1), (x-1, y), (x+1, y) ]:
            if (
                out_of_bounds((new_x, new_y), grid) or
                grid[new_y][new_x] == '#' or
                cost_map[new_y][new_x] <= cost+1
            ):
                continue
            cost_map[new_y][new_x] = cost+1
            q.append((new_x, new_y, cost+1))

    q = [(end[0], end[1])]
    save_map = {}
    while len(q) > 0:
        x, y = q.pop(0)
        cur_cost = cost_map[y][x]
        for jump_x, jump_y in [ (x, y-2), (x, y+2), (x-2, y), (x+2, y) ]:
            if (
                not out_of_bounds((jump_x, jump_y), grid) and
                grid[jump_y][jump_x] != '#' and
                cur_cost - cost_map[jump_y][jump_x] - 2 > 0
            ):
                # -2 because the extra 2 moves to cheat
                cost_saved = cur_cost - cost_map[jump_y][jump_x] - 2
                save_map[cost_saved] = save_map.get(cost_saved, 0) + 1
        for new_x, new_y in [ (x, y-1), (x, y+1), (x-1, y), (x+1, y) ]:
            if (
                not out_of_bounds((new_x, new_y), grid) and
                grid[new_y][new_x] != '#' and
                cost_map[new_y][new_x] == cur_cost-1
            ):
                q.append((new_x, new_y))
                break

    ans = 0
    for k, v in save_map.items():
        if k >= 100:
            ans += v
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
