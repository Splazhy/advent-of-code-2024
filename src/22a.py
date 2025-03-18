INPUT_PATH = 'input/22.in'
TEST_MOD = [
    ('test/22.in', 37327623),
]


def prune(n) -> int:
    return n % 16777216

def mix(value, secret) -> int:
    return value ^ secret

def process(secret) -> int:
    secret = mix(secret * 64, secret)
    secret = prune(secret)
    secret = mix(secret // 32, secret)
    secret = prune(secret)
    secret = mix(secret * 2048, secret)
    secret = prune(secret)
    return secret


def get_ans(file_path: str):
    lines = [int(line.rstrip()) for line in open(file_path)]
    ans = 0
    for secret in lines:
        for _ in range(2000):
            secret = process(secret)
        ans += secret
    return ans


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
