import networkx as nx

INPUT_PATH = 'input/23.in'
TEST_MOD = [
    ('test/23.in', 'co,de,ka,ta'),
]

def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    graph = nx.Graph()
    for line in lines:
        a, b = line.split('-')
        graph.add_node(a)
        graph.add_node(b)
        graph.add_edge(a, b)

    cliques = max(list(nx.find_cliques(graph)), key=len)
    # print(cliques)
    return ','.join(sorted(cliques))

if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
