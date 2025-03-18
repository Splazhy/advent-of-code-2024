INPUT_PATH = 'input/22.in'
TEST_MOD = [
    ('test/22-1.in', 6),
    ('test/22-2.in', 23),
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

def get_price_changes(secret, n):
    prev_price = secret % 10
    changes = []
    prices = []
    for _ in range(n):
        secret = process(secret)
        cur_price = secret % 10
        changes.append(cur_price - prev_price)
        prices.append(cur_price)
        prev_price = cur_price
    return changes, prices


def get_ans(file_path: str):
    lines = [int(line.rstrip()) for line in open(file_path)]

    max_n = 2000
    if file_path == 'test/22-1.in':
        max_n = 10

    window_dict = {}
    for secret in lines:
        changes, prices = get_price_changes(secret, max_n-1)
        visited_windows = set()
        for a, b, c, d, price in zip(changes, changes[1:], changes[2:], changes[3:], prices[3:]):
            k = (a,b,c,d)
            if k not in visited_windows:
                window_dict[k] = window_dict.get(k, 0) + price
                visited_windows.add(k)

    max_value = -1
    max_sequence = None
    for k, v in window_dict.items():
        if v > max_value:
            max_value = v
            max_sequence = k
    print(max_sequence, max_value)
    return max_value


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
