INPUT_PATH = 'input/19.in'
TEST_MOD = [
    ('test/19.in', 6),
]

class State:
    def __init__(self, label):
        self.label = label
        self.transitions = {}

    def to(self, key: str):
        return self.transitions.get(key)

    def to_or_add(self, key: str):
        target = self.transitions.get(key)
        if target == None:
            new_state = State(self.label + key)
            self.transitions[key] = new_state
            target = new_state
        return target

    def connect_to(self, state):
        self.transitions[state.label] = state

    def __repr__(self):
        return f'{self.label}: {[k for k in self.transitions.keys()]}'

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.label == other.label

    def __hash__(self):
        return hash(self.label)


def get_ans(file_path: str):
    lines = open(file_path).read()
    patterns, designs = lines.split("\n\n")
    patterns = patterns.split(', ')
    designs = designs.split('\n')

    start_state = State('_')
    for p in patterns:
        cur_state = start_state
        for c in p:
            cur_state = cur_state.to_or_add(c)
        cur_state.connect_to(start_state)

    possible_cnt = 0
    for design in designs:
        q = set([start_state])
        print(design)
        pass
        for i, c in enumerate(design):
            next_q = set()
            for cur_state in q:
                for next_state in [cur_state.to(c), cur_state.to('_')]:
                    if next_state != None:
                        next_q.add(next_state)
            q = next_q
        if len(q) > 0:
            print(q)
            possible_cnt += 1
        else:
            print("IMPOSSIBLE")

    return possible_cnt

# TOO HIGH
# 356



if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
