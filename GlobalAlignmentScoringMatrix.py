def match_score(c1, c2, scoring_matrix):
    amino_acids, substitution_scores = scoring_matrix
    i = amino_acids.index(c1)
    j = amino_acids.index(c2)
    return substitution_scores[i][j]


def alignment_score(s1, s2, scoring_matrix, gap_penalty):
    n, m = len(s1), len(s2)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        d[i][0] = gap_penalty * i
    for j in range(m+1):
        d[0][j] = gap_penalty * j

    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = max(d[i-1][j-1] + match_score(s1[i-1], s2[j-1], scoring_matrix),
                          d[i-1][j] + gap_penalty,
                          d[i][j-1] + gap_penalty)
    return d[n][m]


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


def global_alignment(raw_lines, s, t):
    #parsing scoring matrix from raw_lines
    amino_acids = raw_lines[0].strip().split()
    substitution_scores = []
    for line in raw_lines[1:]:
        substitution_scores.append(map(int, line.strip().split()[1:]))
    scoring_matrix = amino_acids, substitution_scores
    #linear gap penalty
    gap_penalty = -5
    return alignment_score(s, t, scoring_matrix, gap_penalty)


with open("blossum62.txt", 'r') as f:
    raw_substitution_matrix = f.readlines()

with open("input.txt", 'r') as f:
    s1, s2 = parse_fasta(f.readlines())

with open("output.txt", 'w') as out:
    out.write(str(global_alignment(raw_substitution_matrix, s1, s2)))