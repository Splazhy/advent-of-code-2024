INPUT_PATH = 'input/05.in'
TEST_PATH = 'test/05.in'
TEST_ANS = 143


def get_ans(file_path: str):
    before_rule_dict = {}
    after_rule_dict = {}
    rules, updates = open(file_path).read().split("\n\n")

    rules = [list(map(int, l.split("|"))) for l in rules.split("\n")]
    for before, after in rules:
        if after not in before_rule_dict:
            before_rule_dict[after] = set()
        if before not in after_rule_dict:
            after_rule_dict[before] = set()
        before_rule_dict[after].add(before)
        after_rule_dict[before].add(after)

    ans = 0
    updates = [list(map(int, l.split(","))) for l in updates.split("\n")]
    for update in updates:
        for idx, page in enumerate(update):
            before = set(update[:idx])
            after = set(update[idx+1:])
            if page in before_rule_dict:
                if len(before_rule_dict[page] & before) < len(before):
                    break
            if page in after_rule_dict:
                if len(after_rule_dict[page] & after) < len(after):
                    break
        else:
            ans += update[len(update) // 2]
    return ans


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))
