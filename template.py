INPUT_PATH = 'input/00.in'
TEST_MOD = [
    ('test/00.in', 69),
]


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
