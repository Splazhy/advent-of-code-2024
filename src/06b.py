from copy import deepcopy
import timeit

INPUT_PATH = 'input/06.in'
TEST_MOD = [
    ('test/06.in', 6),
    ('test/06_edge.in', 1),
]


def find_obstacle_ahead(cur_pos: tuple, facing: tuple, obstacles: set) -> tuple:
    aligned_axis = 0 if facing[0] == 0 else 1  # 0 for x, 1 for y
    diff_axis = 0 if facing[0] != 0 else 1
    compare_func = (lambda a, b: a > b) if facing[diff_axis] < 0 else (lambda a, b: a < b)
    filtered_obstacles = set(
        filter(
            lambda x:
                x[aligned_axis] == cur_pos[aligned_axis] and
                compare_func(cur_pos[diff_axis], x[diff_axis]),
            obstacles
        )
    )
    obstacle_ahead = None
    min_dist = 0xffffffff
    for obs in filtered_obstacles:
        cur_dist = abs(cur_pos[diff_axis] - obs[diff_axis])
        if cur_dist < min_dist:
            min_dist = cur_dist
            obstacle_ahead = obs
    return obstacle_ahead


def is_looping(cur_pos, facing, lines, obstacles) -> bool:
    next_obstacle = find_obstacle_ahead(cur_pos, facing, obstacles)
    while True:
        if next_obstacle == None:
            return False
        next_pos = (next_obstacle[0]-facing[0], next_obstacle[1]-facing[1])
        if (cur_pos, next_pos) in lines:
            return True
        facing = (-facing[1], facing[0])
        if cur_pos != next_pos:
            lines.append((cur_pos, next_pos))
        cur_pos = next_pos
        next_obstacle = find_obstacle_ahead(cur_pos, facing, obstacles)


def get_ans(file_path: str):
    lines = list(map(lambda x: x.rstrip(), open(file_path).readlines()))
    traverse_map = []
    start_pos = (0, 0)
    cur_pos = (0, 0)
    facing = (0, -1)  # default up
    obstacles = set()
    for y, line in enumerate(lines):
        traverse_map.append([])
        for x, c in enumerate(line):
            if c == '^':
                cur_pos = (x, y)
                start_pos = cur_pos
                traverse_map[-1].append('.')
            elif c == '#':
                obstacles.add((x, y))
                traverse_map[-1].append(c)
            else:
                traverse_map[-1].append(c)
    original_map = deepcopy(traverse_map)

    loop_points = set()
    visited = set()
    lines = []
    step = 0
    last_turn_pos = cur_pos
    while True:
        # print(len(loop_points))
        visited.add(cur_pos)
        traverse_map[cur_pos[1]][cur_pos[0]] = step
        next_pos = (cur_pos[0] + facing[0], cur_pos[1] + facing[1])
        if next_pos[0] < 0 or next_pos[0] > len(traverse_map[0])-1 or next_pos[1] < 0 or next_pos[1] > len(traverse_map)-1:
            lines.append((last_turn_pos, cur_pos))
            break
        elif traverse_map[next_pos[1]][next_pos[0]] == '#':
            lines.append((last_turn_pos, cur_pos))
            facing = (-facing[1], facing[0])
            next_pos = (cur_pos[0] + facing[0], cur_pos[1] + facing[1])
            last_turn_pos = cur_pos

        if (
            next_pos not in visited and
            traverse_map[next_pos[1]][next_pos[0]] != '#'
        ):
            sim_obstacles = deepcopy(obstacles)
            sim_obstacles.add(next_pos)
            sim_lines = deepcopy(lines)
            sim_lines.append((last_turn_pos, cur_pos))
            sim_facing = (-facing[1], facing[0])
            if is_looping(cur_pos, sim_facing, sim_lines, sim_obstacles):
                loop_points.add(next_pos)


        cur_pos = next_pos
        step += 1

    for a, b in lines:
        char = '|' if a[0] == b[0] else '—'
        aligned_pos = a[0] if a[0] == b[0] else a[1]
        matching_axis = 0 if a[0] == b[0] else 1
        moving_axis = 0 if a[0] != b[0] else 1
        start = min(a[moving_axis], b[moving_axis])
        end = max(a[moving_axis], b[moving_axis])
        for i in range(start, end+1):
            p = [0, 0]
            p[moving_axis] = i
            p[matching_axis] = aligned_pos
            original_map[p[1]][p[0]] = char
        original_map[a[1]][a[0]] = '+'
        original_map[b[1]][b[0]] = '+'
    for l in loop_points:
        original_map[l[1]][l[0]] = 'O'
    original_map[start_pos[1]][start_pos[0]] = '^'
    for l in original_map:
        print(" ".join(l))

    return len(loop_points)


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"

    start = timeit.default_timer()
    print(get_ans(INPUT_PATH))
    stop = timeit.default_timer()
    print('Time: ', stop - start)
