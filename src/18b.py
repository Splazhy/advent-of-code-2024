import networkx as nx

INPUT_PATH = 'input/18.in'
TEST_MOD = [
    ('test/18.in', "6,1"),
]


def out_of_bounds(pos, area) -> bool:
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(area[0]) or pos[1] >= len(area)


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    bytes_pos = [[int(n) for n in l.split(',')] for l in lines]
    max_x, max_y = -1, -1
    for x, y in bytes_pos:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    grid = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

    graph = nx.Graph()
    for y, l in enumerate(grid):
        for x, _ in enumerate(l):
            graph.add_node((x, y))
            surroundings = [
                (x, y-1),
                (x, y+1),
                (x-1, y),
                (x+1, y),
            ]
            for new_x, new_y in surroundings:
                if out_of_bounds((new_x, new_y), grid):
                    continue
                graph.add_node((new_x, new_y))
                graph.add_edge((x, y), (new_x, new_y), weight=1)

    for x, y in bytes_pos:
        graph.remove_node((x, y))
        try:
            nx.shortest_path_length(graph, (0, 0), (max_x, max_y), 'weight')
        except nx.NetworkXNoPath:
            return f'{x},{y}'


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
