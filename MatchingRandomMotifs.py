def nucleotide_probability(nucleotide, gc_content):
    if nucleotide == "G" or nucleotide == "C":
        return gc_content / 2
    if nucleotide == "A" or nucleotide == "T":
        return (1 - gc_content) / 2
    return 0


def probability_of_success(s, x):
    p = 1
    for c in s:
        p *= nucleotide_probability(c, x)
    return p


def probability_at_least_once(n, x, s):
    p = probability_of_success(s, x)
    return 1 - (1 - p)**n


with open("input.txt", 'r') as file:
    n, x = map(float, file.readline().strip().split())
    n = int(n)
    s = file.readline()

with open("output.txt", 'w') as out:
    out.write(str(probability_at_least_once(n, x, s)))