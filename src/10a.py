INPUT_PATH = 'input/10.in'
TEST_MOD = [
    ('test/10.in', 36),
]


def out_of_bounds(pos, trail_map) -> bool:
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(trail_map[0]) or pos[1] >= len(trail_map)


def get_surroundings(pos) -> list:
    return [(pos[0],pos[1]-1),(pos[0],pos[1]+1),(pos[0]-1,pos[1]),(pos[0]+1,pos[1])]


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    trail_map = []
    score_map = []
    trailheads = set()
    summits = set()
    for y, line in enumerate(lines):
        trail_map.append([])
        score_map.append([0 for _ in range(len(line))])
        for x, height in enumerate([int(c) for c in [*line]]):
            if height == 9:
                summits.add((x, y))
            if height == 0:
                trailheads.add((x, y))
            trail_map[-1].append(height)

    for summit in summits:
        dfs_stack = [summit]
        visited = set()
        while len(dfs_stack) > 0:
            cur_pos = dfs_stack.pop()
            if cur_pos in visited:
                continue
            visited.add(cur_pos)
            score_map[cur_pos[1]][cur_pos[0]] += 1
            cur_height = trail_map[cur_pos[1]][cur_pos[0]]
            for other_pos in [x for x in get_surroundings(cur_pos) if not out_of_bounds(x, trail_map)]:
                other_height = trail_map[other_pos[1]][other_pos[0]]
                if cur_height - 1 == other_height:
                    dfs_stack.append(other_pos)

    score = 0
    for x, y in trailheads:
        score += score_map[y][x]
    return score


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
