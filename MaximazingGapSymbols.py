def match(c1, c2):
    if c1 == c2:
        return 1
    return -3


def count_gaps(s1, s2, d):
    gaps = 0
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if d[i][j] == d[i-1][j-1] + match(s1[i-1], s2[j-1]):
            i -= 1
            j -= 1
        elif d[i][j] == d[i][j-1] - 1:
            gaps += 1
            j -= 1
        elif d[i][j] == d[i-1][j] - 1:
            gaps += 1
            i -= 1
    while i > 0:
        gaps += 1
        i -= 1
    while j > 0:
        gaps += 1
        j -= 1
    return gaps


def maximazing_gap_symbols(s1, s2):
    n, m = len(s1), len(s2)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        d[i][0] = -i
    for j in range(m+1):
        d[0][j] = -j

    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = max(d[i-1][j-1] + match(s1[i-1], s2[j-1]),
                          d[i-1][j] - 1,
                          d[i][j-1] - 1)

    return count_gaps(s1, s2, d)


def parse_fasta(lines):
    seqs = []
    cur_seq = ""
    for line in lines[1:]:
        if line[0] == ">":
            seqs.append(cur_seq)
            cur_seq = ""
        else:
            cur_seq += line.strip()
    seqs.append(cur_seq)
    return seqs


with open("input.txt", 'r') as f:
    s1, s2 = parse_fasta(f.readlines())

with open("output.txt", 'w') as out:
    out.write("\n".join(str(maximazing_gap_symbols(s1, s2))))