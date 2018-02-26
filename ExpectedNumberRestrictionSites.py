def nucleotide_probability(nucleotide, gc_content):
    if nucleotide == "G" or nucleotide == "C":
        return gc_content / 2
    if nucleotide == "A" or nucleotide == "T":
        return (1 - gc_content) / 2
    return 0


def probability_of_success(s, gc_content):
    p = 1
    for c in s:
        p *= nucleotide_probability(c, gc_content)
    return p


def expected_restriction_sites(n, s, gc_content):
    return (n - len(s) + 1) * probability_of_success(s, gc_content)


with open("input.txt", 'r') as file:
    n = int(file.readline().strip())
    s = file.readline().strip()
    xs = map(float, file.readline().strip().split())

with open("output.txt", 'w') as out:
    out.write(" ".join([str(expected_restriction_sites(n, s, x)) for x in xs]))