# Advent of Code 2024

My solutions for Advent of Code 2024, some are manually solved, some are not optimized.

I used Python 3.12 for this year:
```sh
python3 src/01a.py # runs day 1 part 1
```

## File Naming Scheme

- `01b.py` means day 1 part 2
- `02b_old.py` means it's incorrect, but the code too long for me to justify deleting it
- `09a_slow.py` means this code is slow, but I'm persistent enough to wait
- `12a+.py` means a more optimized version of day 12 part 1
- `14b_manual.py` means this code only show the path which I had to get it by hand
- `15b_visual.py` means this code also visualize the problem before giving the answer
- `16b_nx.py` means I need to rely on [networkx](https://networkx.org/) library instead of reinventing the wheel
- `17b_forever.py` means my grand-grand-grandchild will die before this program finishes
- `19a_wrong.py` like `_old` postfix, the code is too clean for me to justify deleting it
- `24b_incomplete.py` means this code only let me break down the problem

## Random Questions

### Why show `test/` but not `input/`?

From [about page](https://adventofcode.com/2024/about) of Advent of Code:

> **Can I copy/redistribute part of Advent of Code?** Please don't. Advent of Code is free to use, not free to copy. If you're posting a code repository somewhere, please don't include parts of Advent of Code like the puzzle text or your inputs.

files inside `test/` directory are either from problem examples, myself, or [r/adventofcode](https://www.reddit.com/r/adventofcode/).

### Why Python?

I prefer writing code fast over writing fast code.

If it weren't for the competition, I would use other language to learn more about the language, using advent of code as learning platform. (Rust? Zig? *wink wink*)

### Did I use AI at all?

Yes, 3 instances in total.

1. Day 16, I used ChatGPT to help me write `visualization/16b_nx.ipynb` because I didn't want to bother relearning matplotlib.

2. Day 19, I used GitHub Copilot 4 hours into the problem to help find logic error in my code, and found out that I used cached functions from test input for actual input.

3. Day 24, I used ChatGPT to help me write html and javascript (deleted `visualization/24.html`) to visualize my input with MermaidJS and generate image of the big diagram (`visualization/24.png`).