INPUT_PATH = 'input/02.in'
TEST_PATH = 'test/02.in'
TEST_ANS = 2


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    reports = []
    for l in lines:
        reports.append([int(i) for i in l.split()])

    safe = 0
    for levels in reports:
        is_decreasing = False
        is_increasing = False
        for n, next_n in zip(levels, levels[1:]):
            if n == next_n:
                break
            if abs(n - next_n) > 3:
                break
            if is_increasing and is_decreasing:
                break
            if n < next_n:
                is_increasing = True
            if n > next_n:
                is_decreasing = True
        else:
            if is_increasing ^ is_decreasing:
                safe += 1

    return safe




if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))