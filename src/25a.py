INPUT_PATH = 'input/25.in'
TEST_MOD = [
    ('test/25.in', 3),
]

def get_heights(grid, is_key: bool) -> tuple:
    filtered_grid = grid[:-1] if is_key else grid[1:]
    cnt = [0 for _ in range(5)]
    for g in filtered_grid:
        for i, c in enumerate(g):
            if c == '#':
                cnt[i] += 1
    return tuple(cnt)


def is_fit(key, lock) -> bool:
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True


def get_ans(file_path: str):
    lines = [line.split("\n") for line in open(file_path).read().split("\n\n")]
    keys = set()
    locks = set()
    for l in lines:
        if l[0] == '#####':
            locks.add(get_heights(l, False))
        else:
            keys.add(get_heights(l, True))
    ans = 0
    for lock in locks:
        for key in keys:
            if is_fit(key, lock):
                ans += 1
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
