INPUT_PATH = 'input/13.in'
TEST_MOD = [
    # ('test/13.in', 480), # no test output, no test
]

ADDER = 10000000000000 # ah fuck

class ClawMachine:
    def __init__(self, data):
        data = data.split("\n")
        a = data[0][len("Button A: "):].split(', ')
        b = data[1][len("Button B: "):].split(', ')
        p = data[2][len("Prize: "):].split(', ')

        self.a = (int(a[0][2:]), int(a[1][2:]))
        self.b = (int(b[0][2:]), int(b[1][2:]))
        self.prize = (int(p[0][2:]) + ADDER, int(p[1][2:]) + ADDER)

    def __repr__(self):
        return f'A{self.a} B{self.b} ${self.prize}'


def det2x2(a, b, c, d) -> int:
    # beautiful, absolutely beautiful
    return a * d - b * c


def get_ans(file_path: str):
    data = open(file_path).read().split("\n\n")
    claw_machines = []
    for d in data:
        claw_machines.append(ClawMachine(d))

    tokens = 0
    for cm in claw_machines:
        x, y = cm.prize
        # Cramer's rule to the rescue
        det_d = det2x2(cm.a[0], cm.b[0], cm.a[1], cm.b[1])
        det_d1 = det2x2(x, cm.b[0], y, cm.b[1])
        det_d2 = det2x2(cm.a[0], x, cm.a[1], y)
        if det_d1 % det_d == 0 and det_d2 % det_d == 0:
            tokens += (det_d1 // det_d) * 3
            tokens += det_d2 // det_d
    return tokens


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
