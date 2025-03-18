INPUT_PATH = 'input/12.in'
TEST_MOD = [
    ('test/12-1.in', 140),
    ('test/12-2.in', 772),
    ('test/12.in', 1930),
]


def get_perimeter(region) -> int:
    perimeter = 0
    for x, y in region:
        up = (x, y-1)
        down = (x, y+1)
        left = (x-1, y)
        right = (x+1, y)
        for surrounding in [up, down, left, right]:
            if surrounding not in region:
                perimeter += 1
    return perimeter


def out_of_bounds(pos, plant_map) -> bool:
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(plant_map[0]) or pos[1] >= len(plant_map)


def flood_fill(start, visited, plant_map):
    region = set()
    q = [start]
    plant_type = plant_map[start[1]][start[0]]
    while len(q) > 0:
        x, y = q.pop()
        if (
            out_of_bounds((x, y), plant_map) or
            plant_map[y][x] != plant_type or
            (x, y) in region or
            (x, y) in visited
        ):
            continue
        region.add((x, y))
        visited.add((x, y))
        up = (x, y-1)
        down = (x, y+1)
        left = (x-1, y)
        right = (x+1, y)
        for pos in [up, down, left, right]:
            q.append(pos)
    return list(region)


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]

    plant_map = []
    for line in lines:
        plant_map.append([*line])

    visited = set()
    regions = []
    for y, _ in enumerate(lines):
        for x, _ in enumerate(line):
            if (x, y) in visited:
                continue
            regions.append(flood_fill((x, y), visited, plant_map))

    price = 0
    for region in regions:
        # print(len(region), get_perimeter(region))
        price += len(region) * get_perimeter(region)
    return price

if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
