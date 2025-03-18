INPUT_PATH = 'input/02.in'
TEST_PATH = 'test/02.in'
TEST_ANS = 4


def is_safe(levels: list) -> bool:
    is_increasing = False
    is_decreasing = False
    for n, next_n in zip(levels, levels[1:]):
        if n == next_n:
            return False
        if abs(n - next_n) > 3:
            return False
        if is_increasing and is_decreasing:
            return False
        if n < next_n:
            is_increasing = True
        if n > next_n:
            is_decreasing = True
    if is_increasing ^ is_decreasing:
        return True
    else:
        return False


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    reports = []
    for l in lines:
        reports.append([int(i) for i in l.split()])

    safe = 0
    for levels in reports:
        if is_safe(levels):
            safe += 1
        else:
            # bruteforce the shit out of it
            for i in range(len(levels)):
                cpy = levels[:] # deep copy the list
                del cpy[i]
                if is_safe(cpy):
                    safe += 1
                    break
    return safe


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))