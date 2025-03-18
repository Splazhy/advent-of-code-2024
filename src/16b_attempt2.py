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
    q = [(start, (1, 0), 0)]
    merging_paths = {}
    while len(q) > 0:
        (x, y), facing, cur_score = q.pop(0)
        dx, dy = facing
        sf = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        next_scores = [
            cur_score + 1 if facing == (0, -1) else cur_score + 1001 if dy == 0 else cur_score + 2001,
            cur_score + 1 if facing == (0, 1) else cur_score + 1001 if dy == 0 else cur_score + 2001,
            cur_score + 1 if facing == (-1, 0) else cur_score + 1001 if dx == 0 else cur_score + 2001,
            cur_score + 1 if facing == (1, 0) else cur_score + 1001 if dx == 0 else cur_score + 2001,
        ]

        for (dx, dy), new_s in zip(sf, next_scores):
            new_x, new_y = x+dx, y+dy
            c = maze[new_y][new_x]
            old_s = score_map[new_y][new_x]
            new_facing = (dx, dy)
            if (
                (old_s == new_s - 1000 and maze[new_y][new_x] != 'E') or
                (old_s == new_s + 1000 and maze[new_y][new_x] != 'E')
            ):
                merging_paths[(new_x, new_y)] = [new_facing, dir_map[new_y][new_x]]
                # print(new_x, new_y, merging_paths[(new_x, new_y)])
                continue
            if c == '#' or old_s <= new_s:
                continue
            dir_map[new_y][new_x] = new_facing
            score_map[new_y][new_x] = new_s
            q.append(((new_x, new_y), new_facing, new_s))

    # for k, v in merging_paths.items():
    #     print(k, v)
    q = [end]
    visited = set()
    while len(q) > 0:
        # for l in maze:
        #     print(" ".join(l))
        # print()
        x, y = q.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) in merging_paths:
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if maze[y+dy][x+dx] == '#':
                    continue
                ddx, ddy = dir_map[y+dy][x+dx]
                if (-ddx, -ddy) == (dx, dy):
                    q.append((x+dx,y+dy))
        else:
            dx, dy = dir_map[y][x]
            q.append((x-dx,y-dy))
        maze[y][x] = 'O'


    # for y in range(len(maze)):
    #     for x in range(len(maze[0])):
    #         if maze[y][x] == '.':
    #             maze[y][x] = map_facing_arrow(dir_map[y][x])
    maze[end[1]][end[0]] = 'E'
    maze[start[1]][start[0]] = 'S'
    for l in maze:
        print(' '.join(l))
    print()

    return len(visited)

# TOO LOW
# 490
# 491


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
