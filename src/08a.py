INPUT_PATH = 'input/08.in'
TEST_MOD = [
    ('test/08.in', 14),
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

    for k, v in antennas.items():
        for i in range(len(v)):
            for j in range(i, len(v)):
                if i == j:
                    continue
                a1 = v[i]
                a2 = v[j]
                dist = (a1[0]-a2[0], a1[1]-a2[1])
                a1a = (a1[0] + dist[0], a1[1] + dist[1])
                a1b = (a1[0] - dist[0], a1[1] - dist[1])
                a2a = (a2[0] + dist[0], a2[1] + dist[1])
                a2b = (a2[0] - dist[0], a2[1] - dist[1])
                # print(dist)
                for anti in [a1a, a1b, a2a, a2b]:
                    if out_of_bounds(bounds, anti) or antenna_map[anti[1]][anti[0]] == k:
                        continue
                    # print(a1, a2)
                    # antenna_map[anti[1]][anti[0]] = '#'
                    # for l in antenna_map:
                    #     print(l)
                    antinodes.add(anti)

    # for anti in antinodes:
    #     antenna_map[anti[1]][anti[0]] = '#'

    # for l in antenna_map:
    #     print(' '.join([str(c) for c in l]))

    return len(antinodes)


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
