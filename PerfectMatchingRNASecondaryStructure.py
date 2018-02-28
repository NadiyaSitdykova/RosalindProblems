import math


def number_of_perfect_matchings(rna):
    gc_count = 0
    au_count = 0
    for bp in rna:
        if bp == "C" or bp == "G":
            gc_count += 1
        if bp == "A" or bp == "U":
            au_count += 1
    if gc_count % 2 == 1 or au_count % 2 == 1:
        return 0
    return math.factorial(gc_count//2) * math.factorial(au_count//2)


with open("input.txt", 'r') as f:
    f.readline()
    s = f.readline().strip()

with open("output.txt", 'w') as out:
    out.write(str(number_of_perfect_matchings(s)))