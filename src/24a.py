INPUT_PATH = 'input/24.in'
TEST_MOD = [
    ('test/24.in', 4),
    ('test/24-1.in', 2024),
]

class Gate:
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.observers = set()
        self.fn = None

    def set_op(self, gate_a, gate_b, op):
        self.a = gate_a
        self.b = gate_b
        self.a.observers.add(self)
        self.b.observers.add(self)
        match op:
            case "AND":
                self.fn = lambda a,b: a and b
            case "OR":
                self.fn = lambda a,b: a or b
            case "XOR":
                self.fn = lambda a,b: a ^ b

    def update(self):
        old_val = self.value
        self.value = self.fn(self.a.value, self.b.value)
        if self.value != old_val:
            for observer in self.observers:
                observer.update()

    def __repr__(self):
        return f'{self.label}={self.value}'


def get_ans(file_path: str):
    initials, connections = open(file_path).read().split('\n\n')
    gate_map = {}
    for i in initials.split("\n"):
        k, v = i.split(": ")
        gate_map[k] = Gate(k, bool(int(v)))

    connections = [(c1.split(), c2) for c1, c2 in [c.split(" -> ") for c in connections.split("\n")]]
    while True:
        retry_connections = []
        for c in connections:
            (a, op, b), out = c
            if a in gate_map and b in gate_map:
                gate = gate_map.get(out, Gate(out, False)) # False is just placeholder
                gate.set_op(gate_map[a], gate_map[b], op)
                gate.update()
                if out not in gate_map:
                    gate_map[out] = gate
            else:
                retry_connections.append(((a, op, b), out))
        if len(retry_connections) == 0:
            break
        connections = retry_connections

    ans = 0
    for g in sorted([v for v in gate_map.values() if v.label.startswith('z')], key=lambda x: x.label, reverse=True):
        ans = (ans << 1) + g.value
    print(bin(ans))
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
