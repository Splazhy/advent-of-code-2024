INPUT_PATH = 'input/02.in'
TEST_PATH = 'test/02.in'
TEST_ANS = 4


def is_safe(levels: list) -> bool:
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
            return True
    return False


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    reports = []
    for l in lines:
        reports.append([int(i) for i in l.split()])

    safe = 0
    for levels in reports:
        is_decreasing = 0
        is_increasing = 0
        old_n: int
        bad_num = 0
        request_old_n = False
        for n, next_n in zip(levels, levels[1:]):
            if bad_num > 1:
                break
            if request_old_n:
                request_old_n = False
                n = old_n
            is_bad = False
            if n == next_n:
                is_bad = True
            if abs(n - next_n) > 3:
                if abs(old_n - next_n) < 3:
                    is_bad = True
                else:
                    break
            if n < next_n:
                is_increasing += 1
            if n > next_n:
                is_decreasing += 1
            if is_increasing > 0 and is_decreasing > 0:
                if 1 == is_decreasing == is_increasing:
                    if abs(old_n - next_n) < 3 and old_n != next_n:
                        request_old_n = True
                        if old_n > n < next_n and old_n > next_n:
                            print("de", old_n, n, next_n)
                            is_increasing -= 1
                        elif old_n < n > next_n and old_n < next_n:
                            print("in", old_n, n, next_n)
                            is_decreasing -= 1
                        is_bad = True
                    else:
                        break
                if is_increasing > 1 and (old_n < n > next_n):
                    if abs(old_n - next_n) < 3 and old_n != next_n:
                        request_old_n = True
                        is_bad = True
                        is_decreasing -= 1
                    else:
                        break
                elif is_decreasing > 1 and (old_n > n < next_n):
                    if abs(old_n - next_n) < 3 and old_n != next_n:
                        request_old_n = True
                        is_bad = True
                        is_increasing -= 1
                    else:
                        break
            if is_bad:
                bad_num += 1
            else:
                old_n = n
        else:
            if bad_num <= 1:
                safe += 1
                print(bad_num, '\t', levels)

    return safe

# WRONG
# 719
# 651
# 623
# 622

# TO TRY
# 621

if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))