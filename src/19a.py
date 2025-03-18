from functools import cache

INPUT_PATH = 'input/19.in'
TEST_MOD = [
    ('test/19.in', 6),
]

patterns = None

def is_possible(design: str, patterns: list[str]) -> bool:
    @cache
    def is_possible_recur(design: str) -> bool:
        if len(design) == 0:
            return True
        for p in patterns:
            if design.startswith(p) and is_possible_recur(design[len(p):]):
                    return True
        return False
    return is_possible_recur(design)


def get_ans(file_path: str):
    global patterns
    lines = open(file_path).read()
    patterns, designs = lines.split("\n\n")
    patterns = set(patterns.split(', '))
    designs = designs.split('\n')

    possible_cnt = 0
    for design in designs:
        if is_possible(design, patterns):
            possible_cnt += 1

    return possible_cnt

# TOO HIGH
# 356

if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
