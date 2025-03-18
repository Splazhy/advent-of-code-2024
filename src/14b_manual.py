from PIL import Image


INPUT_PATH = 'input/14.in'
TEST_MOD = [
    # ('test/14.in', 12), # no test
]


class Robot:
    def __init__(self, data):
        p, v = data.split(" ")
        self.p = [int(x) for x in p[2:].split(",")]
        self.v = [int(x) for x in v[2:].split(",")]
        self.path = [self.p]

    def __repr__(self):
        return f'p:{self.p} v:{self.v}'

    def init_path(self, width, height):
        while True:
            self.traverse(width, height)
            if self.path[0] == self.p:
                break
            self.path.append(self.p)

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


def get_ans(file_path: str):
    lines = [line.rstrip() for line in open(file_path)]
    robots = []
    for line in lines:
        robots.append(Robot(line))

    width, height = 11, 7 # test space
    if file_path == 'input/14.in':
        width, height = 101, 103 # input space

    seconds = 0
    for robot in robots:
        robot.init_path(width, height)
    interval = len(robots[0].path)


    seconds = 0
    while seconds < interval:
        img = Image.new('1', (width, height))

        area = [[0 for _ in range(width)] for _ in range(height)]
        for robot in robots:
            area[robot.path[seconds][1]][robot.path[seconds][0]] = 1

        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixels[i, j] = area[j][i]

        img.save(f'images/{seconds}.jpg')
        seconds += 1



if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
