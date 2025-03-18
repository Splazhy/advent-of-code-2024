import networkx as nx

INPUT_PATH = 'input/23.in'
TEST_MOD = [
    ('test/23.in', 7),
]


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    graph = nx.Graph()
    for line in lines:
        a, b = line.split('-')
        graph.add_node(a)
        graph.add_node(b)
        graph.add_edge(a, b)

    ans = 0
    for cycle in nx.simple_cycles(graph, 3):
        c = set(cycle)
        for node in c:
            if node.startswith('t'):
                ans += 1
                break
    return ans

if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
