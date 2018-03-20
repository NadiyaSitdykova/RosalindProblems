def match_score(c1, c2, scoring_matrix):
    amino_acids, substitution_scores = scoring_matrix
    i = amino_acids.index(c1)
    j = amino_acids.index(c2)
    return substitution_scores[i][j]


def alignment_score(s1, s2, scoring_matrix, gap_penalty):
    n, m = len(s1), len(s2)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        d[i][0] = 0
    for j in range(m+1):
        d[0][j] = 0

    #compute alignments scores matrix d and find max_score
    max_score = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = max(d[i-1][j-1] + match_score(s1[i-1], s2[j-1], scoring_matrix),
                          d[i-1][j] + gap_penalty,
                          d[i][j-1] + gap_penalty,
                          0)
            if d[i][j] > max_score:
                argmax = (i, j)
                max_score = d[i][j]

    #retrace alignment of substrings with max_score
    i, j = argmax
    while i > 0 and j > 0 and d[i][j] > 0:
        if d[i][j] == d[i-1][j-1] + match_score(s1[i-1], s2[j-1], scoring_matrix):
            i -= 1
            j -= 1
        elif d[i][j] == d[i][j-1] + gap_penalty:
            j -= 1
        elif d[i][j] == d[i-1][j] + gap_penalty:
            i -= 1

    return max_score, s1[i: argmax[0]], s2[j: argmax[1]]


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


def local_alignment(raw_lines, s1, s2):
    #parsing scoring matrix from raw_lines
    amino_acids = raw_lines[0].strip().split()
    substitution_scores = []
    for line in raw_lines[1:]:
        substitution_scores.append(map(int, line.strip().split()[1:]))
    scoring_matrix = amino_acids, substitution_scores
    #linear gap penalty
    gap_penalty = -5
    return alignment_score(s1, s2, scoring_matrix, gap_penalty)


with open("pam250.txt", 'r') as f:
    raw_substitution_matrix = f.readlines()

with open("input.txt", 'r') as f:
    s1, s2 = parse_fasta(f.readlines())

with open("output.txt", 'w') as out:
    out.write("\n".join(map(str, local_alignment(raw_substitution_matrix, s1, s2))))