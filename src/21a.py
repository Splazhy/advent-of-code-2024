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


class KeypadAndGraph:
    def __init__(self, keypad, graph):
        self.keypad = keypad
        self.graph = graph

numpad = KeypadAndGraph(numpad_map, numpad_graph)
dirpad = KeypadAndGraph(dirpad_map, dirpad_graph)

class Robot:
    def __init__(self, kg: KeypadAndGraph):
        self.keypad = kg.keypad
        self.pos = kg.keypad['A']
        self.graph = kg.graph


    def get_best_path(self, start_pos, end_pos, robots):
        possibilities = []
        paths = nx.all_shortest_paths(self.graph, start_pos, end_pos)
        for p in paths:
            possibilities.append('')
            for u, v in zip(p, p[1:]):
                possibilities[-1] += self.graph.get_edge_data(u, v)['label']
            possibilities[-1] += 'A'
        candidates = possibilities
        if len(robots) == 0:
            return candidates[0]
        candidates = [(c, c) for c in candidates] # save original state
        while len(candidates) > 1:
            next_candidates = []
            # print(candidates)
            for o, c in candidates:
                t = robots[0].get_action_list(c, robots[1:], False)
                t = ''.join(t)
                # print(c, t)
                next_candidates.append((o, t))
            min_len = min(len(l) for _, l in next_candidates)
            candidates = [(o, l) for o, l in next_candidates if len(l) == min_len]

        chosen = candidates[0][0]
        # print(chosen, possibilities)
        return chosen

    # NOTE: this function modifies self.pos
    def get_action_list(self, code, robots, move=True):
        action_line = []
        start_pos = self.pos
        end_pos = None
        for c in code:
            end_pos = self.keypad[c]
            action_line.append(self.get_best_path(start_pos, end_pos, robots))
            start_pos = end_pos
        if move:
            self.pos = end_pos
        return action_line


def get_ans(file_path: str):
    codes = [line.rstrip() for line in open(file_path)]
    robots = [
        Robot(numpad),
        Robot(dirpad),
        Robot(dirpad),
    ]
    ans = 0
    for code in codes:
        cur_code = code
        for i, robot in enumerate(robots):
            action_line = robot.get_action_list(cur_code, robots[i+1:])
            new_code = ''.join(action_line)
            cur_code = new_code
            # print(new_code)
        # print(len(cur_code), int(code[:-1]))
        # print()
        ans += len(cur_code) * int(code[:-1])
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
