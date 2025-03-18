INPUT_PATH = 'input/17.in'
TEST_MOD = [
    ('test/17-3.in', 117440),
]

def combo(operand, a, b, c) -> int:
    if operand in range(4):
        return operand
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case 7:
            return None

def run_program(program, a, b, c) -> list:
    output = []
    idx = 0
    while idx < len(program):
        opcode = program[idx]
        operand = program[idx + 1]
        literal_op = operand
        combo_op = combo(operand, a, b, c)
        match opcode:
            case 0:
                # print(a)
                a = a >> combo_op
            case 1:
                b = b ^ literal_op
            case 2:
                b = combo_op % 8
            case 3:
                if a != 0:
                    idx = literal_op
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(combo_op % 8)
            case 6:
                b = a >> combo_op
            case 7:
                c = a >> combo_op
        idx += 2
    # print(a)
    return output

def get_ans(file_path: str):
    _, p = open(file_path).read().split("\n\n")
    # registers = {} # no need for part 2 I guess
    # for l in r.split("\n"):
    #     label, val = l.split(": ")
        # registers[label[len('register ')]] = int(val)
    program = [int(n) for n in p[len('program: '):].split(",")]

    step = 6
    section = step
    old_a = 0
    expected_output = program
    while (section // step) * 2 <= len(expected_output):
        new_a = None
        a_prefix = old_a
        for a_postfix in range(1 << section):
            a_test = (a_prefix << step) + a_postfix
            result = run_program(program, a_test, 0, 0)
            if len(result) != (section // step) * 2:
                continue
            for i in range(len(result)):
                if result[i] != program[-len(result)+i]:
                    break
            else:
                print(bin(a_test))
                print(result)
                new_a = a_test
                break
        old_a = new_a
        section += step

    return old_a

if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    ans = get_ans(INPUT_PATH)
    assert 258394985014171 == ans
    print(ans)
