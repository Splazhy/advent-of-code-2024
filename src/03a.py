INPUT_PATH = 'input/03.in'
TEST_PATH = 'test/03.in'
TEST_ANS = 161


def get_ans(file_path: str):
    program = open(file_path).read()
    ans = 0
    for token in program.split("mul("):
        invalid = False
        a, b = 0, 0
        cur_num = ""
        for c in token:
            if c.isdigit():
                cur_num += c
            elif c == ',':
                a = int(cur_num)
                cur_num = ""
            elif c == ')':
                b = int(cur_num)
                break
            else:
                invalid = True
                break
        if not invalid:
            ans += a * b
    return ans


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))