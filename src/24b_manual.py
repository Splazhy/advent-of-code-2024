# circuit.txt is the input file with only 2nd section (I deleted it)
f = [l.rstrip() for l in open("circuit.txt").readlines()]
cc = [(c1.split(), c2) for c1, c2 in [c.split(" -> ") for c in f]]
gate_cnt = {"AND": 0, "OR": 0, "XOR": 0}


# Prints into a markdown file that can be rendered by mermaid
# Run `python3 24b_manual.py > huge_flowchart.md` in the terminal
print("```mermaid")
print("flowchart")
for (a, op, b), out in cc:
    g = f"{op}{gate_cnt[op]}"
    gate_cnt[op] = gate_cnt[op] + 1
    print(f'{a} --> {g}')
    print(f'{b} --> {g}')
    print(f'{g} --> {out}')
print("```")


# After ~2 hours of manual work, the following pairs were found:
swap_pairs = [("z12", "djg"), ("z19", "sbg"), ("hjm", "mcq"), ("z37", "dsd")]
ans = []
for a, b in swap_pairs:
    ans.append(a)
    ans.append(b)
ans.sort()
print(','.join(ans))

# WRONG?? WHAT THE FUCK?
# djg,dsd,jrr,mcq,sbg,z12,z19,z37

# Human debugger FTW
# djg,dsd,hjm,mcq,sbg,z12,z19,z37
