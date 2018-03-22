def match_score(c1, c2, scoring_matrix):
    amino_acids, substitution_scores = scoring_matrix
    i = amino_acids.index(c1)
    j = amino_acids.index(c2)
    return substitution_scores[i][j]


def alignment(s1, s2, scoring_matrix, gap_opening, gap_extension):
    n, m = len(s1), len(s2)
    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    e = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    g = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        d[i][0] = gap_opening + (i - 1) * gap_extension
        e[i][0] = d[i][0]
    for j in range(1, m+1):
        d[0][j] = gap_opening + (j - 1) * gap_extension
        g[0][j] = d[0][j]

    # compute alignments scores matrices d, w1, w2
    for i in range(1, n+1):
        for j in range(1, m+1):
            e[i][j] = max(e[i][j - 1] + gap_extension, d[i][j - 1] + gap_opening)
            g[i][j] = max(g[i - 1][j] + gap_extension, d[i - 1][j] + gap_opening)
            d[i][j] = max(d[i - 1][j - 1] + match_score(s1[i - 1], s2[j - 1], scoring_matrix),
                          e[i][j], g[i][j])

    # retrace alignment
    s1_rev_aligned, s2_rev_aligned = "", ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if d[i][j] == e[i][j]:
            while j > 0 and (d[i][j - 1] + gap_opening) < (e[i][j - 1] + gap_extension):
                s1_rev_aligned += "-"
                s2_rev_aligned += s2[j - 1]
                j -= 1
            s1_rev_aligned += "-"
            s2_rev_aligned += s2[j - 1]
            j -= 1
        if d[i][j] == g[i][j]:
            while i > 0 and (d[i - 1][j] + gap_opening) < (g[i - 1][j] + gap_extension):
                s1_rev_aligned += s1[i - 1]
                s2_rev_aligned += "-"
                i -= 1
            s1_rev_aligned += s1[i - 1]
            s2_rev_aligned += "-"
            i -= 1
        if d[i][j] == d[i - 1][j - 1] + match_score(s1[i - 1], s2[j - 1], scoring_matrix):
            s1_rev_aligned += s1[i - 1]
            s2_rev_aligned += s2[j - 1]
            i -= 1
            j -= 1
    while i > 0:
        s1_rev_aligned += s1[i - 1]
        s2_rev_aligned += "-"
        i -= 1
    while j > 0:
        s1_rev_aligned += "-"
        s2_rev_aligned += s2[j - 1]
        j -= 1

    return d[n][m], s1_rev_aligned[::-1], s2_rev_aligned[::-1]


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


def global_alignment_affine_gap_penalty(raw_lines, s, t):
    # parsing scoring matrix from raw_lines
    amino_acids = raw_lines[0].strip().split()
    substitution_scores = []
    for line in raw_lines[1:]:
        substitution_scores.append(map(int, line.strip().split()[1:]))
    scoring_matrix = amino_acids, substitution_scores
    # affine gap penalty
    gap_opening = -11
    gap_extension = -1
    return alignment(s, t, scoring_matrix, gap_opening, gap_extension)


with open("blossum62.txt", 'r') as f:
    raw_substitution_matrix = f.readlines()

with open("input.txt", 'r') as f:
    s1, s2 = parse_fasta(f.readlines())

with open("output.txt", 'w') as out:
    out.write("\n".join(map(str, global_alignment_affine_gap_penalty(raw_substitution_matrix, s1, s2))))