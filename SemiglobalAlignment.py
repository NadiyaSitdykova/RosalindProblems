def match(c1, c2):
    if c1 == c2:
        return 1
    return -1


def semiglobal_alignment(s1, s2, gap_penalty):
    n, m = len(s1), len(s2)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # compute score matrix d and find max_score
    max_score = 0
    argmax = (0, 0)
    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = max(d[i-1][j-1] + match(s1[i-1], s2[j-1]),
                          d[i-1][j] + gap_penalty,
                          d[i][j-1] + gap_penalty)
            if (i == n or j == m) and d[i][j] > max_score:
                max_score = d[i][j]
                argmax = (i, j)

    # retrace alignment
    s1_rev_aligned, s2_rev_aligned = "", ""
    i, j = argmax
    for k in range(1, n-i+1):
        s1_rev_aligned += s1[-k]
        s2_rev_aligned += "-"
    for k in range(1, m-j+1):
        s1_rev_aligned += "-"
        s2_rev_aligned += s2[-k]
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
    while i > 0:
        s1_rev_aligned += s1[i - 1]
        s2_rev_aligned += "-"
        i -= 1
    while j > 0:
        s1_rev_aligned += "-"
        s2_rev_aligned += s2[j - 1]
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
    out.write("\n".join(map(str, semiglobal_alignment(s1, s2, -1))))