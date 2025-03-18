INPUT_PATH = 'input/10.in'
TEST_MOD = [
    ('test/10-1.in', 3),
    ('test/10-2.in', 13),
    ('test/10-3.in', 227),
    ('test/10.in', 81),
]


def out_of_bounds(pos, trail_map) -> bool:
    return (pos[0] < 0 or pos[1] < 0 or pos[0] >= len(trail_map[0]) or pos[1] >= len(trail_map)) or trail_map[pos[1]][pos[0]] == 420


def get_surroundings(pos) -> list:
    return [(pos[0],pos[1]-1),(pos[0],pos[1]+1),(pos[0]-1,pos[1]),(pos[0]+1,pos[1])]


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    trail_map = []
    ratings_map = []
    trailheads = set()
    summits = set()
    for y, line in enumerate(lines):
        trail_map.append([])
        ratings_map.append([0 for _ in range(len(line))])
        # handle '.' to test on more examples
        for x, height in enumerate([int(c) if c != '.' else 420 for c in [*line]]):
            if height == 9:
                summits.add((x, y))
            if height == 0:
                trailheads.add((x, y))
            trail_map[-1].append(height)

    for summit in summits:
        dfs_stack = [summit]
        while len(dfs_stack) > 0:
            cur_pos = dfs_stack.pop()
            cur_height = trail_map[cur_pos[1]][cur_pos[0]]
            to_add = []
            for other_pos in [x for x in get_surroundings(cur_pos) if not out_of_bounds(x, trail_map)]:
                other_height = trail_map[other_pos[1]][other_pos[0]]
                if cur_height - 1 == other_height:
                    to_add.append(other_pos)
            ratings_map[cur_pos[1]][cur_pos[0]] += 1
            dfs_stack += to_add
            # for l in ratings_map:
            #     print(l)
            # print()

    # for l in ratings_map:
    #     print(l)
    ratings = 0
    for x, y in trailheads:
        ratings += ratings_map[y][x]
    return ratings


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
