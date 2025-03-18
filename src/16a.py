INPUT_PATH = 'input/16.in'
TEST_MOD = [
    ('test/16.in', 7036),
    ('test/16-1.in', 11048),
]

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

    start, end, deer = None, None, None
    for y, l in enumerate(maze):
        for x, c in enumerate(l):
            if c == 'S':
                start = (x, y)
            elif c == 'E':
                end = (x, y)

    score_map = [[0xffffffff for _ in range(len(maze))] for _ in range(len(maze[0]))]
    q = [(start, (1, 0), 0)]
    while len(q) > 0:
        (x, y), facing, cur_score = q.pop()
        dx, dy = facing
        surroundings_pos = [
            (x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y),
        ]
        surroundings_facing = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        ]
        surroundings_char = [
            maze[y-1][x],
            maze[y+1][x],
            maze[y][x-1],
            maze[y][x+1],
        ]
        surroundings_score = [
            score_map[y-1][x],
            score_map[y+1][x],
            score_map[y][x-1],
            score_map[y][x+1],
        ]
        next_scores = [
            cur_score + 1 if facing == (0, -1) else cur_score + 1001 if dy == 0 else cur_score + 2001,
            cur_score + 1 if facing == (0, 1) else cur_score + 1001 if dy == 0 else cur_score + 2001,
            cur_score + 1 if facing == (-1, 0) else cur_score + 1001 if dx == 0 else cur_score + 2001,
            cur_score + 1 if facing == (1, 0) else cur_score + 1001 if dx == 0 else cur_score + 2001,
        ]

        for (x, y), facing, c, old_s, new_s in zip(surroundings_pos, surroundings_facing, surroundings_char, surroundings_score, next_scores):
            if c == '#' or old_s < new_s:
                continue
            score_map[y][x] = new_s
            q.append(((x, y), facing, new_s))

    return score_map[end[1]][end[0]]



if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
