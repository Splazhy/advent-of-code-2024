INPUT_PATH = 'input/11.in'
TEST_MOD = [
    ('test/11.in', None), # no test answer, so no test
]


def get_ans(file_path: str):
    rocks = [int(n) for n in open(file_path).read().split()]
    rock_map = {}
    for rock in rocks:
        rock_map[rock] = rock_map.get(rock, 0) + 1

    for _ in range(75): # blink
        next_rock_map = {}
        for k, v in rock_map.items():
            k_str = str(k)
            if len(k_str) % 2 == 0:
                left = int(k_str[:len(k_str)//2])
                right = int(k_str[len(k_str)//2:])
                next_rock_map[left] = next_rock_map.get(left, 0) + v
                next_rock_map[right] = next_rock_map.get(right, 0) + v
            elif k == 0:
                next_rock_map[1] = next_rock_map.get(1, 0) + v
            else:
                next_rock_map[k * 2024] = next_rock_map.get(k * 2024, 0) + v
        rock_map = next_rock_map

    return sum(rock_map.values())


if __name__ == '__main__':
    # No test answer, so no test :)
    # for path, ans in TEST_MOD:
    #     test_ans = get_ans(path)
    #     assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
