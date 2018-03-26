def match(c1, c2):
    if c1 == c2:
        return 1
    return -2


def overlap_alignment(s1, s2, gap_penalty):
    n, m = len(s1), len(s2)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for j in range(m+1):
        d[0][j] = j * gap_penalty

    # compute score matrix d
    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = max(d[i-1][j-1] + match(s1[i-1], s2[j-1]),
                          d[i-1][j] + gap_penalty,
                          d[i][j-1] + gap_penalty)

    # find max_score
    max_score = 0
    argmax = (0, 0)
    for j in range(m+1):
        if d[n][j] > max_score:
            max_score = d[n][j]
            argmax = (n, j)

    # retrace alignment
    s1_rev_aligned, s2_rev_aligned = "", ""
    i, j = argmax
    while i > 0 and j > 0:
        if d[i][j] == d[i-1][j-1] + match(s1[i-1], s2[j-1]):
            s1_rev_aligned += s1[i-1]
            s2_rev_aligned += s2[j-1]
            i -= 1
            j -= 1
        elif d[i][j] == d[i][j-1] + gap_penalty:
            s1_rev_aligned += "-"
            s2_rev_aligned += s2[j-1]
            j -= 1
        elif d[i][j] == d[i-1][j] + gap_penalty:
            s1_rev_aligned += s1[i-1]
            s2_rev_aligned += "-"
            i -= 1
    while j > 0:
        s1_rev_aligned += '-'
        s2_rev_aligned += s2[j-1]
        j -= 1
    return max_score, s1_rev_aligned[::-1], s2_rev_aligned[::-1]


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
    out.write("\n".join(map(str, overlap_alignment(s1, s2, -2))))