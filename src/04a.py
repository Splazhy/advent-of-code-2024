INPUT_PATH = 'input/04.in'
TEST_PATH = 'test/04.in'
TEST_ANS = 18


def get_ans(file_path: str):
    lines = open(file_path).readlines()
    count = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'X':
                if ( # up
                    i >= 3 and
                    lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S'
                ):
                    count += 1
                if ( # down
                    i < len(lines)-3 and
                    lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S'
                ):
                    count += 1
                if ( # left
                    j >= 3 and
                    line[j-1] == 'M' and line[j-2] == 'A' and line[j-3] == 'S'
                ):
                    count += 1
                if ( # right
                    j < len(line)-3 and
                    line[j+1] == 'M' and line[j+2] == 'A' and line[j+3] == 'S'
                ):
                    count += 1
                if ( # diagonal up left
                    i >= 3 and j >= 3 and
                    lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S'
                ):
                    count += 1
                if ( # diagonal up right
                    i >= 3 and j < len(line)-3 and
                    lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S'
                ):
                    count += 1
                if ( # diagonal down left
                    i < len(lines)-3 and j >= 3 and
                    lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S'
                ):
                    count += 1
                if ( # diagonal down right
                    i < len(lines)-3 and j < len(line)-3 and
                    lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S'
                ):
                    count += 1
    return count


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))
