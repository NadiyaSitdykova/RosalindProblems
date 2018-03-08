import math


def compute_counts(rna):
    bp_counts = {"C": 0, "G": 0, "A": 0, "U": 0}
    for bp in rna:
        bp_counts[bp] += 1
    return bp_counts


def maximum_matchings(rna):
    bp_counts = compute_counts(rna)
    cg_max = max(bp_counts["C"], bp_counts["G"])
    cg_min = min(bp_counts["C"], bp_counts["G"])
    au_max = max(bp_counts["A"], bp_counts["U"])
    au_min = min(bp_counts["A"], bp_counts["U"])
    if cg_min == 0 and au_min == 0:
        return 0
    return math.factorial(cg_max)/math.factorial(cg_max-cg_min) \
           * math.factorial(au_max)/math.factorial(au_max-au_min)


with open("input.txt", 'r') as f:
    f.readline()
    s = f.readline().strip()

with open("output.txt", 'w') as out:
    out.write(str(maximum_matchings(s)))