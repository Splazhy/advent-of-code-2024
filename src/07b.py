INPUT_PATH = 'input/07.in'
TEST_MOD = [
    ('test/07.in', 11387),
]


def get_ans(file_path: str):
    lines = list(map(lambda x: x.rstrip(), open(file_path).readlines()))
    equations = []
    for l in lines:
        eq, num = l.split(': ')
        equations.append((int(eq), list(map(lambda x: int(x), num.split()))))

    ans = 0
    # IDEA: work backwards
    for target, nums in equations:
        q = [(target, nums, '')]
        while len(q) > 0:
            cur_target, cur_nums, log = q.pop()
            if len(cur_nums) == 1:
                if cur_target == cur_nums[0]:
                    ans += target
                    # print(f'{cur_nums[0]}{log}')
                    break
                continue

            last_num = cur_nums[-1]
            if cur_target - last_num > 0:
                q.append((
                    cur_target - last_num,
                    cur_nums[:-1],
                    f'+ {last_num}{log}'
                ))
            if cur_target % last_num == 0:
                q.append((
                    cur_target // last_num,
                    cur_nums[:-1],
                    f'* {last_num}{log}'
                ))
            if str(cur_target).endswith(str(last_num)):
                try:
                    q.append((
                        int(str(cur_target)[:-len(str(last_num))]),
                        cur_nums[:-1],
                        f'|| {last_num}{log}'
                    ))
                except:
                    continue
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
