INPUT_PATH = 'input/03.in'
TEST_PATH = 'test/03.in'
TEST_ANS = 48


def get_ans(file_path: str):
    program = open(file_path).read()
    ans = 0
    disabled = False
    idx = 0
    while idx < len(program):
        if program[idx:idx+4] == "do()":
            disabled = False
            idx += 4
            continue
        if program[idx:idx+7] == "don't()":
            disabled = True
            idx += 7
            continue
        if not disabled and program[idx:idx+4] == "mul(":
            idx += 4
            a, b = 0, 0
            invalid = False
            cur_num = ""
            while True:
                if program[idx].isdigit():
                    cur_num += program[idx]
                    idx += 1
                    continue
                if program[idx] == ',':
                    if cur_num == "":
                        invalid = True
                        break
                    a = int(cur_num)
                    cur_num = ""
                    idx += 1
                    continue
                if program[idx] == ')':
                    if cur_num == "":
                        invalid = True
                        break
                    b = int(cur_num)
                    cur_num = ""
                    break
                else:
                    invalid = True
                    break
            if not invalid:
                ans += a * b
        idx += 1
    return ans


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))