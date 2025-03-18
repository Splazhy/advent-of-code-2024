from copy import deepcopy


INPUT_PATH = 'input/24.in'
TEST_MOD = [
    # ('test/24-2.in', "z00,z01,z02,z05"), # this test is for AND circuit, not addition
]

class Gate:
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.a = None
        self.b = None
        self.op = None
        self.observers = set()

    def set_op(self, gate_a, gate_b, op):
        self.a = gate_a
        self.b = gate_b
        self.a.observers.add(self)
        self.b.observers.add(self)
        self.op = op
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
        a = '___' if self.a == None else self.a.label
        b = '___' if self.b == None else self.b.label
        return f'{self.label}: {a} {self.op} {b}'


def get_gates_value(gates) -> int:
    val = 0
    for g in gates:
        val = (val << 1) + g.value
    return val


def get_ans(file_path: str):
    initials, connections = open(file_path).read().split('\n\n')
    gate_map = {}
    for i in initials.split("\n"):
        k, v = i.split(": ")
        gate_map[k] = Gate(k, bool(int(v)))

    connections_in = [(c1.split(), c2) for c1, c2 in [c.split(" -> ") for c in connections.split("\n")]]
    connections = deepcopy(connections_in)
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

    z_gates = sorted([v for v in gate_map.values() if v.label[0] == 'z'], key=lambda x: x.label, reverse=True)
    y_gates = sorted([v for v in gate_map.values() if v.label[0] == 'y'], key=lambda x: x.label, reverse=True)
    x_gates = sorted([v for v in gate_map.values() if v.label[0] == 'x'], key=lambda x: x.label, reverse=True)

    first_sum_gates = []
    first_carry_gates = []
    propagating_carry_gates = []
    for g in gate_map.values():
        if g.a and g.a.label[0] in ['x', 'y']:
            if g.op == 'AND':
                first_carry_gates.append(g)
            elif g.op == 'XOR':
                first_sum_gates.append(g)
        elif g.op == 'OR':
            propagating_carry_gates.append(g)

    print("Wrong sum gates:")
    for g in gate_map.values():
        if (
            (g.a in first_sum_gates or g.b in first_sum_gates) and
            g.op != 'AND' and
            g.label[0] != 'z'
        ):
           print(f'\t{g}')

    print("Wrong output gates:")
    for g in z_gates[1:]: # skip the z45 gate because it's the carry
        if g.op != 'XOR':
            print(f'\t{g}')


    return get_gates_value(z_gates)

# sqr: mcq OR rpj

if __name__ == '__main__':
    # for path, ans in TEST_MOD:
        # test_ans = get_ans(path)
        # assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
