INPUT_PATH = 'input/01.in'
TEST_PATH = 'test/01.in'
TEST_ANS = 11


def get_ans(file_path: str):
    lines = [list(map(int, line.rstrip().split("   "))) for line in open(file_path)]
    left = []
    right = []
    for l, r in lines:
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()
    ans = 0
    for l, r in zip(left, right):
        ans += abs(l - r)

    return ans


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))