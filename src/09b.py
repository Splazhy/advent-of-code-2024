INPUT_PATH = 'input/09.in'
TEST_MOD = [
    ('test/09.in', 2858),
]


class Block:
    def __init__(self, idx, id, size):
        self.idx = idx
        self.id = id
        self.size = size

    def __repr__(self):
        return f'{self.id}@[{self.idx}]: {self.size}'


def insert(block: Block, smol_block: Block, free_blocks: list[Block]):
    assert block.size >= smol_block.size
    free_blocks.append(Block(smol_block.idx, -1, smol_block.size))
    smol_block.idx = block.idx
    block.idx += smol_block.size
    block.size -= smol_block.size


def get_ans(file_path: str):
    disk = [int(c) for c in [*open(file_path).read()]]
    alloc_blocks = []
    free_blocks = []
    idx = 0
    for id, (alloc_size, free_size) in enumerate(zip(disk[::2], disk[1::2] + [0])):
        if alloc_size > 0:
            alloc_blocks.append(Block(idx, id, alloc_size))
        if free_size > 0:
            free_blocks.append(Block(idx+alloc_size, -1, free_size))
        idx += alloc_size + free_size

    for block in alloc_blocks[::-1]:
        # for block_ in sorted(alloc_blocks + free_blocks, key=lambda x: x.idx):
        #     if block_.id != -1:
        #         print(f'{f'{block_.id}' * block_.size}',end='')
        #     else:
        #         print(f'{'.' * block_.size}',end='')
        # print()
        for free_block in free_blocks:
            # print(block.id, free_block.id, block.size, free_block.size)
            if block.idx > free_block.idx and block.size <= free_block.size:
                insert(free_block, block, free_blocks)
                break

    checksum = 0
    for block in alloc_blocks:
        assert block.id != -1
        for idx in range(block.idx, block.idx+block.size):
            checksum += block.id * idx
    # print(alloc_blocks)

    return checksum


if __name__ == '__main__':
    for path, ans in TEST_MOD:
        test_ans = get_ans(path)
        assert test_ans == ans, f"Test failed (got {test_ans}, expected {ans})"
    print(get_ans(INPUT_PATH))
