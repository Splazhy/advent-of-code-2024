INPUT_PATH = 'input/16.in'
TEST_MOD = [
    ('test/16.in', 45),
    ('test/16-1.in', 64),
    ('test/16_reddit.in', 149),
    ('test/16_reddit2.in', 413),
]


def map_facing_arrow(c):
    match c:
        case (0, -1):
            return '↑'
        case (0, 1):
            return '↓'
        case (-1, 0):
            return '←'
        case (1, 0):
            return '→'

def facing_idx(facing) -> int:
    match facing:
        case (0, -1):
            return 0
        case (0, 1):
            return 1
        case (-1, 0):
            return 2
        case (1, 0):
            return 3


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    maze = []
    for l in lines:
        maze.append([*l])

    start, end = None, None
    for y, l in enumerate(maze):
        for x, c in enumerate(l):
            if c == 'S':
                start = (x, y)
            elif c == 'E':
                end = (x, y)

    score_map = [[0xffffffff for _ in range(len(maze[0]))] for _ in range(len(maze))]
    score_map[start[1]][start[0]] = 0
    dir_map = [[(0, 0) for _ in range(len(maze[0]))] for _ in range(len(maze))]
    stack = [(start, (1, 0), 0)]
    while len(stack) > 0:
        (x, y), facing, cur_score = stack.pop()
        dx, dy = facing
        surroundings_facing = [ (0, -1), (0, 1), (-1, 0), (1, 0), ]
        next_scores = [
            cur_score + 1 if facing == (0, -1) else cur_score + 1001 if dy == 0 else cur_score + 2001,
            cur_score + 1 if facing == (0, 1) else cur_score + 1001 if dy == 0 else cur_score + 2001,
            cur_score + 1 if facing == (-1, 0) else cur_score + 1001 if dx == 0 else cur_score + 2001,
            cur_score + 1 if facing == (1, 0) else cur_score + 1001 if dx == 0 else cur_score + 2001,
        ]

        for (dx, dy), new_s in zip(surroundings_facing, next_scores):
            new_x, new_y = x+dx, y+dy
            c = maze[new_y][new_x]
            old_s = score_map[new_y][new_x]
            new_facing = (dx, dy)
            if c == '#' or old_s <= new_s:
                continue
            dir_map[new_y][new_x] = new_facing
            score_map[new_y][new_x] = new_s
            stack.append(((new_x, new_y), new_facing, new_s))

    visited = set()
    stack = [(end, (score_map[end[1]][end[0]], dir_map[end[1]][end[0]]))]
    while len(stack) > 0:
        (x, y), (prev_score, prev_facing) = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        score = score_map[y][x]
        dx, dy = dir_map[y][x]
        # print(x, y, map_facing_arrow((dx, dy)), score)
        for ddx, ddy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            old_x, old_y = x+ddx, y+ddy
            old_score = score_map[old_y][old_x]
            if (
                (score - 1 == old_score and (dx, dy) == dir_map[old_y][old_x]) or
                (score - 1001 == old_score and ((dx == ddx) ^ (dy == ddy))) or
                (prev_score - 2 == old_score and prev_facing == dir_map[old_y][old_x])
            ):
                maze[old_y][old_x] = 'O'
                stack.append(((old_x, old_y), (score, (dx, dy))))
            # print(map_facing_arrow(dir_map[old_y][old_x]), old_score, map_facing_arrow((ddx, ddy)))

    # maze[start[1]][start[0]] = 'S'
    # maze[end[1]][end[0]] = 'E'
    for l in maze:
        print(' '.join(l))
    print()

    return len(visited)

# TOO LOW
# 490

# 489

if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
