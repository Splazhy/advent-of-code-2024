from functools import cache

INPUT_PATH = 'input/19.in'
TEST_MOD = [
    ('test/19.in', 16),
]


def get_ways(design: str, patterns: list) -> int:
    @cache
    def get_ways_recur(design: str) -> int:
        if len(design) == 0:
            return 1
        ways = 0
        for p in patterns:
            if design.startswith(p):
                ways += get_ways_recur(design[len(p):])
        return ways
    return get_ways_recur(design)


def get_ans(file_path: str):
    lines = open(file_path).read()
    patterns, designs = lines.split("\n\n")
    patterns = patterns.split(', ')
    designs = designs.split('\n')

    ans = 0
    for design in designs:
        ans += get_ways(design, patterns)
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
