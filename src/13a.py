INPUT_PATH = 'input/13.in'
TEST_MOD = [
    ('test/13.in', 480),
]


class ClawMachine:
    def __init__(self, data):
        data = data.split("\n")
        a = data[0][len("Button A: "):].split(', ')
        b = data[1][len("Button B: "):].split(', ')
        p = data[2][len("Prize: "):].split(', ')

        self.a = (int(a[0][2:]), int(a[1][2:]))
        self.b = (int(b[0][2:]), int(b[1][2:]))
        self.prize = (int(p[0][2:]), int(p[1][2:]))

    def __repr__(self):
        return f'A{self.a} B{self.b} ${self.prize}'


def get_pos(cm, a_press, b_press) -> tuple:
    return (cm.a[0] * a_press + cm.b[0] * b_press, cm.a[1] * a_press + cm.b[1] * b_press)


def is_reachable(pos, dest) -> bool:
    return dest[0] % pos[0] == 0 and dest[1] % pos[1] == 0 and dest[0] // pos[0] == dest[1] // pos[1]


def get_ans(file_path: str):
    data = open(file_path).read().split("\n\n")
    claw_machines = []
    for d in data:
        claw_machines.append(ClawMachine(d))

    tokens = 0
    for cm in claw_machines:
        i, j = 0, 1
        cur_pos = get_pos(cm, i, j)
        while (i <= 100 and j <= 100) and (cur_pos[0] <= cm.prize[0] and cur_pos[1] <= cm.prize[1]):
            while (i <= 100 and j <= 100) and (cur_pos[0] <= cm.prize[0] and cur_pos[1] <= cm.prize[1]):
                if is_reachable(cur_pos, cm.prize):
                    # print(i, j)
                    multiplier = cm.prize[0] // cur_pos[0]
                    tokens += (i * multiplier * 3) + j * multiplier
                    break
                j += 1
                cur_pos = get_pos(cm, i, j)
            else:
                i += 1
                j = 0
                cur_pos = get_pos(cm, i, j)
                continue
            break
    return tokens


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
