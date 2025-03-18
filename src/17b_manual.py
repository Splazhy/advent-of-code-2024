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

program = [2,4,1,7,7,5,0,3,4,0,1,7,5,5,3,0]

step = 6
section = step
a_stack = [0]
while (section // step) * 2 <= len(program):
    new_a_stack = []
    while len(a_stack) > 0:
        a_prefix = a_stack.pop(0)
        for a_postfix in range(0, 1 << section):
            a_test = (a_prefix << step) + a_postfix
            result = run_program(program, a_test, 0, 0)
            if result == program[((-section)//step)*2:]:
                print(bin(a_test), result)
                new_a_stack.append(a_test)
                break
    a_stack = new_a_stack
    section += step
# 0b111010110000001001000101010010110010001110011011
# 258394985014171
a, b, c = 258394985014171, 0, 0
result = run_program(program, a, b, c)
print(result)
print(program)
print(a)