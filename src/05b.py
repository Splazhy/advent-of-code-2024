INPUT_PATH = 'input/05.in'
TEST_PATH = 'test/05.in'
TEST_ANS = 123


# before_rule_dict = {}
# after_rule_dict = {}

def get_ans(file_path: str):

    # yep, this took me 4 hours to find
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
        fixed = [0 for _ in range(len(update))]
        cycles = set()
        update_set = set(update)
        for page in update:
            before_rule = (before_rule_dict[page] if page in before_rule_dict else set()) & update_set
            after_rule = (after_rule_dict[page] if page in after_rule_dict else set()) & update_set
            if len(before_rule & after_rule) > 0:
                cycles |= (before_rule & after_rule)
            else:
                fixed[len(before_rule)] = page

        if fixed != update:
            ans += fixed[len(fixed) // 2]

    return ans


if __name__ == '__main__':
    test_ans = get_ans(TEST_PATH)
    assert test_ans == TEST_ANS, f"Test failed (got {test_ans}, expected {TEST_ANS})"
    print(get_ans(INPUT_PATH))
