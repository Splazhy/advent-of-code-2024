INPUT_PATH = 'input/06.in'
TEST_PATH = 'test/06.in'
TEST_ANS = 41


def get_ans(file_path: str):
    lines = list(map(lambda x: x.rstrip(), open(file_path).readlines()))
    map_ = []
    cur_pos = (0, 0)
    facing = (0, -1) # up right down left
    for y, line in enumerate(lines):
        map_.append([])
        for x, c in enumerate(line):
            if c == '^':
                cur_pos = (x, y)
                map_[-1].append('.')
            else:
                map_[-1].append(c)

    visited = set()
    while True:
        next_pos = (cur_pos[0] + facing[0], cur_pos[1] + facing[1])
        if next_pos[0] < 0 or next_pos[0] > len(map_[0])-1 or next_pos[1] < 0 or next_pos[1] > len(map_)-1:
            break
        elif map_[next_pos[1]][next_pos[0]] == '#':
            facing = (-facing[1], facing[0])
            next_pos = (cur_pos[0] + facing[0], cur_pos[1] + facing[1])
        map_[cur_pos[1]][cur_pos[0]] = 'X'
        visited.add(cur_pos)
        cur_pos = next_pos
    visited.add(cur_pos)

    return len(visited)


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))
