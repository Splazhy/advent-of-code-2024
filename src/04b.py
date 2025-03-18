INPUT_PATH = 'input/04.in'
TEST_PATH = 'test/04.in'
TEST_ANS = 9


def get_ans(file_path: str):
    lines = open(file_path).readlines()
    count = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if (
                not (c == 'A' and
                i >= 1 and i < len(lines)-1 and
                j >= 1 and j < len(line)-1)
            ):
                continue

            if ( # MSMS
                lines[i-1][j-1] == lines[i+1][j-1] == 'M' and
                lines[i-1][j+1] == lines[i+1][j+1] == 'S'
            ):
                count += 1
            elif ( # SMSM
                lines[i-1][j-1] == lines[i+1][j-1] == 'S' and
                lines[i-1][j+1] == lines[i+1][j+1] == 'M'
            ):
                count += 1
            elif ( # MMSS
                lines[i-1][j-1] == lines[i-1][j+1] == 'M' and
                lines[i+1][j-1] == lines[i+1][j+1] == 'S'
            ):
                count += 1
            elif ( # SSMM
                lines[i-1][j-1] == lines[i-1][j+1] == 'S' and
                lines[i+1][j-1] == lines[i+1][j+1] == 'M'
            ):
                count += 1
    return count


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))
