from itertools import combinations

INPUT_PATH = 'input/07.in'
TEST_MOD = [
    ('test/07.in', 3749),
]


# Reference:
# https://stackoverflow.com/questions/43816965/permutation-without-duplicates-in-python
def place_ones(size, count):
    for positions in combinations(range(size), count):
        p = ['+'] * size
        for i in positions:
            p[i] = '*'
        yield p


def get_ans(file_path: str):
    lines = list(map(lambda x: x.rstrip(), open(file_path).readlines()))
    equations = []
    for l in lines:
        eq, num = l.split(': ')
        equations.append((int(eq), list(map(lambda x: int(x), num.split()))))

    ans = 0
    for target, nums in equations:
        for i in range(len(nums)):
            valid = False
            for ops in list(place_ones(len(nums)-1, i)):
                to_eval = nums[0]
                for n, op in zip(nums[1:], ops):
                    match op:
                        case '+':
                            to_eval += n
                        case '*':
                            to_eval *= n
                if to_eval == target:
                    ans += target
                    # print('nice')
                    valid = True
                    break
            if valid:
                break
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
