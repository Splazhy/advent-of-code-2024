INPUT_PATH = 'input/01.in'
TEST_PATH = 'test/01.in'
TEST_ANS = 31


def get_ans(file_path: str):
    lines = [list(map(int, line.rstrip().split("   "))) for line in open(file_path)]
    left = []
    right_appearance = {}
    for l, r in lines:
        left.append(l)
        right_appearance[r] = right_appearance.get(r, 0) + 1
    ans = 0
    for l in left:
        ans += l * right_appearance.get(l, 0)

    return ans


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))