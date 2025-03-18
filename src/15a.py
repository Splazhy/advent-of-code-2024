INPUT_PATH = 'input/15.in'
TEST_MOD = [
    ('test/15.in', 2028),
    ('test/15-1.in', 10092),
]


def map_dir_char(c) -> tuple:
    match c:
        case '^':
            return (0, -1)
        case 'v':
            return (0, 1)
        case '<':
            return (-1, 0)
        case '>':
            return (1, 0)


# Returns robot new position
def try_move(cur, warehouse, direction) -> tuple:
    x, y = cur
    dx, dy = direction
    new_x, new_y = x + dx, y + dy
    target = (new_x, new_y)
    start_tile = warehouse[y][x]
    target_tile = warehouse[new_y][new_x]
    if target_tile == '#':
        return cur
    elif target_tile == '.':
        warehouse[new_y][new_x] = start_tile
        warehouse[y][x] = '.'
        return (new_x, new_y)
    elif target_tile == 'O':
        next_next = try_move(target, warehouse, direction)
        if next_next != target:
            return try_move(cur, warehouse, direction)
        else:
            return cur
    else:
        assert False, "undefined"



def get_ans(file_path: str):
    map_, moveset = open(file_path).read().split("\n\n")
    warehouse = [[*l] for l in map_.split("\n")]
    robot = None
    for y, l in enumerate(warehouse):
        for x, c in enumerate(l):
            if c == '@':
                robot = (x, y)

    moveset = [map_dir_char(m) for m in ''.join(moveset.split("\n"))]
    for move in moveset:
        robot = try_move(robot, warehouse, move)
        # for l in warehouse:
        #     print(l)
        # print(move)
        # print()

    ans = 0
    for y, l in enumerate(warehouse):
        for x, c in enumerate(l):
            if c == 'O':
                ans += (y * 100) + x
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
