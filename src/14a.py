INPUT_PATH = 'input/14.in'
TEST_MOD = [
    ('test/14.in', 12),
]


class Robot:
    def __init__(self, data):
        p, v = data.split(" ")
        self.p = [int(x) for x in p[2:].split(",")]
        self.v = [int(x) for x in v[2:].split(",")]

    def __repr__(self):
        return f'p:{self.p} v:{self.v}'

    def traverse(self, width, height):
        self.p = [self.p[0] + self.v[0], self.p[1] + self.v[1]]
        if self.p[0] < 0:
            self.p[0] += width
        if self.p[0] >= width:
            self.p[0] -= width
        if self.p[1] < 0:
            self.p[1] += height
        if self.p[1] >= height:
            self.p[1] -= height

    def get_quadrant(self, width, height) -> int:
        half_x = width // 2
        half_y = height // 2
        x, y = self.p
        if x == half_x or y == half_y:
            return -1
        elif x < half_x and y < half_y:
            return 0
        elif x > half_x and y < half_y:
            return 1
        elif x < half_x and y > half_y:
            return 2
        elif x > half_x and y > half_y:
            return 3


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    robots = []
    for line in lines:
        robots.append(Robot(line))

    width, height = 11, 7 # test space
    if file_path == 'input/14.in':
        width, height = 101, 103 # input space

    safety_factor = [0, 0, 0, 0]
    for robot in robots:
        for _ in range(100):
            robot.traverse(width, height)
        quadrant = robot.get_quadrant(width, height)
        if quadrant != -1:
            safety_factor[quadrant] += 1

    ans = 1
    for s in safety_factor:
        ans *= s
    return ans



if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
