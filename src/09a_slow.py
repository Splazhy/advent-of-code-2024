INPUT_PATH = 'input/09.in'
TEST_MOD = [
    ('test/09.in', 1928),
]

def find_last_alloc_idx(line) -> int:
    for idx, id in enumerate(line[::-1]):
        if id != -1:
            return len(line)-idx-1


def get_ans(file_path: str):
    disk = [int(c) for c in [*open(file_path).read()]]
    line = []
    for id, (i, j) in enumerate(zip(disk[::2], disk[1::2] + [0])):
        line += [id for _ in range(i)]
        line += [-1 for _ in range(j)]

    idx = 0
    # print(len(line))
    while idx < len(line):
        print(idx)
        id = line[idx]
        if id == -1:
            to_move = find_last_alloc_idx(line)
            if to_move <= idx:
                break
            line[to_move], line[idx] = line[idx], line[to_move]
        idx += 1

    # print(line)
    checksum = 0
    for idx, id in enumerate(line):
        if id != -1:
            checksum += id * idx

    return checksum


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
