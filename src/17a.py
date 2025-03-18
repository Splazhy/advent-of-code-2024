INPUT_PATH = 'input/17.in'
TEST_MOD = [
    ('test/17-1.in', "0,1,2"),
    ('test/17-2.in', "4,2,5,6,7,7,7,7,3,1,0"),
    ('test/17.in', "4,6,3,5,6,3,5,2,1,0"),
]


def combo(operand, registers) -> int:
    if operand in range(4):
        return operand
    match operand:
        case 4:
            return registers['A']
        case 5:
            return registers['B']
        case 6:
            return registers['C']
        case 7:
            return None


def get_ans(file_path: str):
    r, p = open(file_path).read().split("\n\n")
    registers = {}
    for l in r.split("\n"):
        label, val = l.split(": ")
        registers[label[len('register ')]] = int(val)
    program = [int(n) for n in p[len('program: '):].split(",")]

    output = []
    idx = 0
    while idx < len(program):
        # print(output)
        opcode = program[idx]
        operand = program[idx + 1]
        literal_op = operand
        combo_op = combo(operand, registers)
        match opcode:
            case 0:
                registers['A'] = registers['A'] >> combo_op
            case 1:
                registers['B'] = registers['B'] ^ literal_op
            case 2:
                registers['B'] = combo_op % 8
            case 3:
                if registers['A'] != 0:
                    idx = literal_op
                    continue
            case 4:
                registers['B'] = registers['B'] ^ registers['C']
            case 5:
                output.append(combo_op % 8)
            case 6:
                registers['B'] = registers['A'] >> combo_op
            case 7:
                registers['C'] = registers['A'] >> combo_op
        idx += 2
    # print(','.join([str(n) for n in output]))
    return ','.join([str(n) for n in output])

# WRONG
# 6,5,7,6,4,0,6,2,2


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
