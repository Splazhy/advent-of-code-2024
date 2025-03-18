INPUT_PATH = 'input/08.in'
TEST_MOD = [
    ('test/08.in', 34),
]


def out_of_bounds(bounds, pos) -> bool:
    return bounds[0][0] > pos[0] or bounds[0][1] > pos[1] or bounds[1][0] < pos[0] or bounds[1][1] < pos[1]


def get_ans(file_path: str):
    lines = [x.rstrip() for x in open(file_path)]
    antenna_map = []
    antennas = {}
    bounds = ((0, 0), (len(lines[0])-1, len(lines)-1))
    for y, line in enumerate(lines):
        antenna_map.append([])
        for x, c in enumerate(line):
            if c != '.':
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((x, y))
            antenna_map[-1].append(c)

    antinodes = set()

    for v in antennas.values():
        for i in range(len(v)):
            for j in range(i, len(v)):
                if i == j:
                    continue
                a1 = v[i]
                a2 = v[j]
                dist = (a1[0] - a2[0], a1[1] - a2[1])
                a1a = (a1[0] + dist[0], a1[1] + dist[1], dist)
                a1b = (a1[0] - dist[0], a1[1] - dist[1], (-dist[0], -dist[1]))
                a2a = (a2[0] + dist[0], a2[1] + dist[1], dist)
                a2b = (a2[0] - dist[0], a2[1] - dist[1], (-dist[0], -dist[1]))
                for x, y, dist in [a1a, a1b, a2a, a2b]:
                    cur_pos = (x, y)
                    while not out_of_bounds(bounds, cur_pos):
                        # LOL what the fuck did I write?
                        # if out_of_bounds(bounds, cur_pos):
                        #     break
                        antinodes.add((cur_pos[0], cur_pos[1]))
                        cur_pos = (cur_pos[0] + dist[0], cur_pos[1] + dist[1])
                        # print(cur_pos)

    # for anti in antinodes:
    #     if antenna_map[anti[1]][anti[0]] == '.':
    #         antenna_map[anti[1]][anti[0]] = '#'

    # for l in antenna_map:
    #     print(' '.join([str(c) for c in l]))

    return len(antinodes)


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
