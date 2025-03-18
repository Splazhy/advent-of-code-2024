INPUT_PATH = 'input/17.in'
TEST_MOD = [
    ('test/17-3.in', 117440),
]

len_record = 0

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


def run_program(program, registers) -> bool:
    global len_record
    start_a = registers['A']
    output = []
    idx = 0
    while idx < len(program):
        opcode = program[idx]
        operand = program[idx + 1]
        literal_op = operand
        combo_op = combo(operand, registers)
        match opcode:
            case 0:
                registers['A'] = registers['A'] // (2 ** combo_op)
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
                last = len(output) - 1
                if output[last] != program[last]:
                    return False
                if len_record < len(output):
                    print(start_a, len_record)
                    len_record = len(output)
                if output == program:
                    return True
            case 6:
                registers['B'] = registers['A'] // (2 ** combo_op)
            case 7:
                registers['C'] = registers['A'] // (2 ** combo_op)
        idx += 2
    return output == program


def get_ans(file_path: str):
    global len_record
    len_record = 0

    r, p = open(file_path).read().split("\n\n")
    registers = {}
    for l in r.split("\n"):
        label, val = l.split(": ")
        registers[label[len('register ')]] = int(val)
    program = [int(n) for n in p[len('program: '):].split(",")]

    a, b, c = registers.values() # starting values
    brute_a = 0
    while True:
        # print(brute_a)
        registers['A'] = brute_a
        registers['B'] = b
        registers['C'] = c
        if run_program(program, registers):
            print(brute_a)
            return brute_a
        brute_a += 1


# WRONG
# 6,5,7,6,4,0,6,2,2


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
