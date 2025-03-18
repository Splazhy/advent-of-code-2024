from copy import deepcopy
import os
import time


INPUT_PATH = 'input/15.in'
TEST_MOD = [
    # ('test/15.in', 2028),
    ('test/15-1.in', 9021),
]


def map_dir_arrow(c):
    match c:
        case '^':
            return '↑'
        case 'v':
            return '↓'
        case '<':
            return '←'
        case '>':
            return '→'


def map_dir_char(c) -> tuple:
    match c:
        case '^':
            return (0, -1)
        case 'v':
            return (0, 1)
        case '<':
            return (-1, 0)
        case '>':
            return (1, 0)


def sort_dir(pos, dir):
    match dir:
        case (0, -1):
            return pos[1]
        case (0, 1):
            return -pos[1]
        case (-1, 0):
            return pos[0]
        case (1, 0):
            return -pos[0]


# Returns new position if `cur` can move there, return same position otherwise
def try_move(cur, warehouse, direction) -> tuple:
    dx, dy = direction
    stack = [cur]
    robot_target = (cur[0] + dx, cur[1] + dy)
    mem = []
    while len(stack) > 0:
        x, y = stack.pop()
        mem.append((x, y))
        new_x, new_y = x + dx, y + dy
        target_tile = warehouse[new_y][new_x]
        if target_tile == '#':
            return (cur, mem + stack)
        elif target_tile == '.':
            continue
        elif target_tile in ['[', ']']:
            stack.append((new_x, new_y))
            if dy != 0:
                if target_tile == ']':
                    stack.append((new_x-1, new_y))
                else:
                    stack.append((new_x+1, new_y))
    mem = sorted(set(mem), key=lambda a: sort_dir(a, direction))
    for x, y in mem:
        warehouse[y+dy][x+dx] = warehouse[y][x]
        warehouse[y][x] = '.'
    return (robot_target, mem)



def get_ans(file_path: str):
    map_, moveset = open(file_path).read().split("\n\n")
    warehouse = []
    for y, row in enumerate([[*l] for l in map_.split("\n")]):
        warehouse.append([])
        for c in row:
            if c in ['.', '#']:
                warehouse[-1] += [c, c]
            elif c == 'O':
                warehouse[-1] += ['[', ']']
            elif c == '@':
                warehouse[-1] += ['@', '.']

    robot = None
    for y, l in enumerate(warehouse):
        for x, c in enumerate(l):
            if c == '@':
                robot = (x, y)

    moveset_dir = [map_dir_char(m) for m in ''.join(moveset.split("\n"))]
    moveset = [map_dir_arrow(m) for m in ''.join(moveset.split("\n"))]
    for step, move in enumerate(moveset_dir):
        os.system('clear')
        old_robot = robot
        robot, report = try_move(robot, warehouse, move)
        warehouse_visual = deepcopy(warehouse)
        if report != None:
            for rx, ry in report:
                if robot != old_robot:
                    warehouse_visual[ry+move[1]][rx+move[0]] = '\33[32m' + warehouse_visual[ry+move[1]][rx+move[0]] + '\33[0m'
                else:
                    warehouse_visual[ry][rx] = '\33[31m' + warehouse_visual[ry][rx] + '\33[0m'
        for l in warehouse_visual:
            print(''.join(l))
        print(f'{step+1}/{len(moveset)} {' '.join(moveset[step:step+10])}')
        time.sleep(0.04)

    ans = 0
    for y, l in enumerate(warehouse):
        for x, c in enumerate(l):
            if c == '[':
                ans += (y * 100) + x
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    # print(get_ans(INPUT_PATH))
