from functools import cache
import networkx as nx

INPUT_PATH = 'input/21.in'
TEST_MOD = [
    ('test/21.in', 126384),
]

numpad_map = {
    'A': (2, 3),
    '0': (1, 3),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
}
dirpad_map = {
    'A': (2, 0),
    '^': (1, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}

numpad_graph = nx.DiGraph()
for v in numpad_map.values():
    x, y = v
    numpad_graph.add_node(v)
    for new_pos, label in [ ((x, y-1), '^'), ((x, y+1), 'v'), ((x-1, y), '<'), ((x+1, y), '>') ]:
        if new_pos in numpad_map.values():
            numpad_graph.add_edge(v, new_pos, label=label)

dirpad_graph = nx.DiGraph()
for v in dirpad_map.values():
    x, y = v
    dirpad_graph.add_node(v)
    for new_pos, label in [ ((x, y-1), '^'), ((x, y+1), 'v'), ((x-1, y), '<'), ((x+1, y), '>') ]:
        if new_pos in dirpad_map.values():
            dirpad_graph.add_edge(v, new_pos, label=label)


@cache
def num2dir(start: str, end: str) -> list[str]:
    paths = nx.all_shortest_paths(numpad_graph, numpad_map[start], numpad_map[end])
    possibilities = []
    for p in paths:
        possibilities.append('A')
        for u, v in zip(p, p[1:]):
            possibilities[-1] += numpad_graph.get_edge_data(u, v)['label']
        possibilities[-1] += 'A'
    return possibilities

@cache
def dir2dir(start: str, end: str) -> list[str]:
    paths = nx.all_shortest_paths(dirpad_graph, dirpad_map[start], dirpad_map[end])
    possibilities = []
    for p in paths:
        possibilities.append('A')
        for u, v in zip(p, p[1:]):
            possibilities[-1] += dirpad_graph.get_edge_data(u, v)['label']
        possibilities[-1] += 'A'
    return possibilities


def get_ans(file_path: str):
    codes = [line.rstrip() for line in open(file_path)]

    robot_cnt = 2
    if file_path == INPUT_PATH:
        robot_cnt = 25

    cur_weight_map = {
        'A': {'A': 1, '^': 1, 'v': 1, '<': 1, '>': 1},
        '^': {'A': 1, '^': 1, 'v': 1, '<': 1, '>': 1},
        'v': {'A': 1, '^': 1, 'v': 1, '<': 1, '>': 1},
        '<': {'A': 1, '^': 1, 'v': 1, '<': 1, '>': 1},
        '>': {'A': 1, '^': 1, 'v': 1, '<': 1, '>': 1},
    }
    for _ in range(robot_cnt):
        next_weight_map = {}
        for k, v in cur_weight_map.items():
            next_weight_map[k] = {}
            for kk in v.keys():
                min_weight = None
                for candidate in dir2dir(k, kk):
                    sum_weight = 0
                    for a, b in zip(candidate, candidate[1:]):
                        sum_weight += cur_weight_map[a][b]
                    if min_weight is None or sum_weight < min_weight:
                        min_weight = sum_weight
                next_weight_map[k][kk] = min_weight
        # for k, v in next_weight_map.items():
        #     print(k, v)
        # print()
        cur_weight_map = next_weight_map

    ans = 0
    for code in codes:
        code = 'A' + code
        # print(code)
        min_code_len = 0
        for k, kk in zip(code, code[1:]):
            min_weight = None
            for candidate in num2dir(k, kk):
                sum_weight = 0
                for a, b in zip(candidate, candidate[1:]):
                    sum_weight += cur_weight_map[a][b]
                if min_weight is None or sum_weight < min_weight:
                    min_weight = sum_weight
            min_code_len += min_weight
        ans += min_code_len * int(code[1:-1])
        # print(min_code_len, int(code[1:-1]))
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
